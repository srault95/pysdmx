#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. module:: pysdmx
    :platform: Unix, Windows
    :synopsis: Python interface for SDMX

.. :moduleauthor :: Widukind team <widukind-dev@cepremap.org>
.. :doctest::

    >>> df = eurostat.data('ei_bsco_q','.BS-IBC-NTY.SA..FR',startperiod="2008",endperiod="2009")
    >>> df[1] == {'FREQ': 'Q', 'UNIT': 'BAL', 'INDIC': 'BS-IBC-NTY', 'GEO': 'FR', 'S_ADJ': 'SA'}
    True
    >>> df[0]
    [2009-Q4   -77.8
    2009-Q3   -78.2
    2009-Q2   -74.5
    2009-Q1   -77.9
    2008-Q4   -76.4
    2008-Q3   -80.1
    2008-Q2   -73.6
    2008-Q1   -76.0
    Name: (), dtype: float64]
    >>> eurostat.raw_data('ei_bsco_q','.BS-IBC-NTY.SA..FR',startperiod="2008",endperiod="2009")
    ({'BAL.BS-IBC-NTY.SA.FR.Q': ['-77.8', '-78.2', '-74.5', '-77.9', '-76.4', '-80.1', '-73.6', '-76.0']}, {'BAL.BS-IBC-NTY.SA.FR.Q': ['2009-Q4', '2009-Q3', '2009-Q2', '2009-Q1', '2008-Q4', '2008-Q3', '2008-Q2', '2008-Q1']}, {'BAL.BS-IBC-NTY.SA.FR.Q': defaultdict(<class 'list'>, {})}, {'BAL.BS-IBC-NTY.SA.FR.Q': OrderedDict([('UNIT', 'BAL'), ('INDIC', 'BS-IBC-NTY'), ('S_ADJ', 'SA'), ('GEO', 'FR'), ('FREQ', 'Q')])})

"""
import os
import tempfile
import requests
import pandas
import lxml.etree
import datetime, time
from io import BytesIO,StringIO
import re
import zipfile
from collections import OrderedDict, namedtuple, defaultdict
import logging
import json
import pprint

logger = logging.getLogger("sdmx")

# Allow easy checking for existing namedtuple classes that can be reused for column metadata  
tuple_classes = []

def to_namedtuple(mapping):
    """
    Convert a list of (key,value) tuples into a namedtuple. If there is not already 
    a suitable class in 'tuple_classes', Create a new class first and append it to the list.
        
    return a namedtuple instance
    """
    # convert to OrderedDict
    codes = OrderedDict()
    for k,v in mapping: 
        codes[k] = v
    # Check if there is already a suitable class
    for t in tuple_classes:
        try:
            code_tuple = t(**codes)
            break
        except TypeError:
            if t is tuple_classes[-1]: 
                tuple_classes.append(namedtuple(
                'CodeTuple' + str(len(tuple_classes)), codes.keys()))
                code_tuple = tuple_classes[-1](**codes)
    else:
        tuple_classes.append(namedtuple(
            'CodeTuple' + str(len(tuple_classes)), codes.keys()))
        code_tuple = tuple_classes[0](**codes)
    return code_tuple
            
        
        # This function is no longer used as pandas.to_dates seems to be much faster and powerful. 
        # Remove it after more testing if it is really not needed. 
def date_parser(date, frequency):
    """Generate proper index for pandas

    :param date: A date
    :type date: str
    :param frequency: A frequency as specified in SDMX, A for Annual, Q for Quarterly, M for Monthly and D for Daily
    :type frequency: str
    :return: datetime.datetime()

    >>> date_parser('1987-02-02','D')
    datetime.datetime(1987, 2, 2, 0, 0)
    """

    if frequency == 'A':
        return datetime.datetime.strptime(date, '%Y')
    if frequency == 'Q':
        date = date.split('-Q')
        date = str(int(date[1])*3) + date[0]
        return datetime.datetime.strptime(date, '%m%Y')
    if frequency == 'M':
        return datetime.datetime.strptime(date, '%Y-%m')
    if frequency == 'D':
        return datetime.datetime.strptime(date, '%Y-%m-%d')


class query_rest_xml(object):
    """Retrieve SDMX messages.

    :param url: The URL of the message.
    :type url: str
    :param requests_client: A requests object used for connection pooling
    :type requests_client: requests.sessions.Session
    :return: An lxml.etree.ElementTree() of the SDMX message
    """
    def __init__(self, url, requests_client = requests, timeout = None):
        self.url = url
        self.requests_client = requests_client
        self.temporary_xml = tempfile.TemporaryFile()
        self.timeout = timeout
    def __enter__(self):
        logger.info('Requesting %s', self.url)
        client = self.requests_client or requests
        request = client.get(self.url, timeout=self.timeout)
        if request.status_code == requests.codes.ok:
            for chunk in request.iter_content():
                self.temporary_xml.write(chunk)
        elif request.status_code == 430:
            #Sometimes, eurostat creates a zipfile when the query is too large. We have to wait for the file to be generated.
            messages = response.XPath('.//footer:Message/common:Text',
                                      namespaces=response.nsmap)
            regex_ = re.compile("Due to the large query the response will be written "
                                "to a file which will be located under URL: (.*)")
            matches = [element.text for element in messages 
                           if element.text.startswith('Due to the large query the response will be written')]
            if matches:
                response_ = None
                i = 30
                while i<101:
                    time.sleep(i)
                    i = i+10
                    pos = matches[0].find('http://') 
                    url = matches[0][pos:]  
                    request = requests.get(url)
                    if request.headers['content-type'] == "application/octet-stream":
                        buffer = BytesIO(request.content)
                        file = zipfile.ZipFile(buffer)
                        filename = file.namelist()[0]
                        with file.open(filename) as file_result:
                            for chunk in file_result.readlines():
                                self.temporary_xml.write(file_result.read())
                        break
                        if not file:
                            raise Exception("The provider has not delivered the file you are looking for.")
            else:
                raise ValueError("Error getting client({})".format(request.status_code))
        else:
            raise ValueError("Error getting client({})".format(request.status_code))
        self.temporary_xml.seek(0)
        return self.temporary_xml
    def __exit__(self, exception_type, exception_value, traceback):
        self.temporary_xml.close()

    
class Repository(object):
    """Data provider. This is the main class that allows practical access to all the data.

    :ivar sdmx_url: The URL of the SDMX endpoint, the webservice employed to access the data.
    :type sdmx_url: str
    :ivar agencyID: An identifier of the statistical provider.
    :type agencyID: str
    """
    def __init__(self, sdmx_url=None, format=None, version=None, agencyID=None, 
                 timeout=20, requests_client=None, namespace_style='small'):
        
        self.sdmx_url = sdmx_url
        self.format = format
        self.version = version

        self.agencyID = agencyID
        self.timeout = timeout
        self.requests_client = requests_client
        self.namespace_style=namespace_style
        if namespace_style == 'short':
            # TODO: use these everywhere
            self.structure = 'str'
            self.message = 'mes'
            self.common = 'com'
        elif namespace_style == 'long':
            self.structure = 'structure'
            self.message = 'message'
            self.common = 'common'
        self._dataflows = None

        if not self.sdmx_url:
            raise ValueError("Require sdmx_url parameter")

        if not self.format in ['xml', 'json']:
            raise ValueError("Not implemented SDMX format [%s]" % self.format)

        if self.format == "xml" and not self.version in ['2_0', '2_1']:
            raise ValueError("Not implemented SDMX ML version [%s]" % self.version)
        elif self.format == "json" and not self.version in ['2_1']:
            raise ValueError("Not implemented SDMX JSON version [%s]" % self.version)

        if self.format == 'xml':
            if not self.agencyID:
                raise ValueError("Require agencyID parameter")

            self.dataflow_url = '/'.join([self.sdmx_url, 'dataflow', self.agencyID])
            self.category_scheme_url = '/'.join([self.sdmx_url, 'CategoryScheme'])

        elif self.format == 'json':
            #The list of dataflows and categories have yet to be implemented in sdmx-json.
            self.dataflow_url = None
            self.category_scheme_url = None


    def query_rest_json(self,url):
        """Retrieve SDMX-json messages.

        :param url: The URL of the message.
        :type url: str
        :return: A dictionnary of the SDMX message
        """
        # Fetch data from the provider    
        logger.info('Requesting %s', url)
        client = self.requests_client or requests
        request = client.get(url, timeout=self.timeout)
        return json.load(StringIO(request.text), object_pairs_hook=OrderedDict)
    
    def _categories_xml_2_0(self):

        def walk_category(category):
            category_ = {}
            name = category.xpath('./structure:Name',namespaces=category.nsmap)
            category_['name'] = name[0].text
            flowrefs = category.xpath(
                './structure:DataflowRef/structure:DataflowID',
                namespaces=category.nsmap)
            if flowrefs != []:
                category_['flowrefs'] = [ flowref.text for flowref in flowrefs ]
            subcategories = []
            for subcategory in category.xpath('./structure:Category',
                                              namespaces=category.nsmap):
                subcategories.append(walk_category(subcategory))
            if subcategories != []:
                category_['subcategories'] = subcategories
            
            return category_
                    
        with query_rest_xml(self.category_scheme_url) as file:
            tree = lxml.etree.parse(file)
            namespaces = tree.getroot().nsmap
            xml_categories = tree.xpath('.//structure:CategoryScheme',
                                        namespaces=namespaces)
            return walk_category(xml_categories[0])                            

    def _categories_xml_2_1(self):
        def walk_category(category):
            category_ = {}
            name = category.xpath("./"+self.common+":Name[@xml:lang='en']",namespaces=category.nsmap)
            category_['name'] = name[0].text
            category_['id'] = category.attrib['id']
            subcategories = []
            for subcategory in category.xpath('./'+self.structure+':Category',
                                              namespaces=category.nsmap):
                subcategories.append(walk_category(subcategory))
            if subcategories != []:
                category_['subcategories'] = subcategories
            return category_


        with query_rest_xml(self.sdmx_url + '/categoryscheme') as file:
            categories = []
            subcategories = []
            counter = 0
            for event, element in lxml.etree.iterparse(file):
                if lxml.etree.QName(element.tag).localname == "Category":
                    category_ = {}
                    category_['name'] = {}
                    category_['id'] = element.attrib['id']
                    children_categories = 0
                    for children in element:
                        if lxml.etree.QName(children.tag).localname == "Name":
                            for item in children.items():
                                if item[0][-4:] == 'lang':
                                    category_['name'][item[1]] = children.text
                        elif lxml.etree.QName(children.tag).localname == "Category":
                            children_categories += 1
                            children.clear()
                    if children_categories == 0:
                        categories.append(category_)
                    else:
                        category_['subcategories'] = []
                        for i in range(children_categories):
                            category_['subcategories'].append(categories.pop())
                        categories.append(category_)
            return categories                            


    @property
    def categories(self):
        """Index of available categories

        :type: dict"""

        if not self.format == "xml":
            raise ValueError("categories() function is not available for %s format" % self.format)

        if self.version == '2_0':
            return self._categories_xml_2_0()
        elif self.version == '2_1':
            return self._categories_xml_2_1()

    @property
    def categorisation(self):
        """Links categories and dataflows"""

        categories = defaultdict(list)
        with query_rest_xml(self.sdmx_url + '/categorisation') as file:
            tree = lxml.etree.parse(file)
        namespaces = tree.getroot().nsmap
        categorisations = tree.xpath('.//str:Categorisation',namespaces=namespaces)
        for categorisation in categorisations:
            source = categorisation.xpath('str:Source',namespaces=namespaces)
            ref = source[0].xpath('Ref',namespaces=namespaces)
            source_id = ref[0].attrib['id']
            target = categorisation.xpath('str:Target',namespaces=namespaces)
            ref = target[0].xpath('Ref',namespaces=namespaces)
            target_id = ref[0].attrib['id']
            categories[target_id].append(source_id)
        return(categories)

    def _dataflows_xml_2_0(self, flowref=None):

        self._dataflows = {}
        with query_rest_xml(self.dataflow_url+'/'+str(flowref)) as file:
            tree = lxml.etree.parse(file)
        namespaces = tree.getroot().nsmap
        dataflow_path = ".//structure:Dataflow"
        name_path = ".//structure:Name"
        keyid_path = ".//structure:KeyFamilyID"
        for dataflow in tree.iterfind(dataflow_path,
                                           namespaces=namespaces):
            for id in dataflow.iterfind(keyid_path,
                                           namespaces=namespaces):
                id = id.text
            agencyID = dataflow.get('agencyID')
            version = dataflow.get('version')
            titles = {}
            for title in dataflow.iterfind(name_path,
                                           namespaces=namespaces):
                titles['en'] = title.text

            self._dataflows[id] = (agencyID, version, titles)

        return self._dataflows

    def _dataflows_xml_2_1(self, flowref=None):

        self._dataflows = {}
        with query_rest_xml('/'.join([self.dataflow_url, flowref])) as file:
            tree = lxml.etree.parse(file)
        dataflow_path = ".//str:Dataflow"
        name_path = ".//com:Name"

        namespaces = tree.getroot().nsmap

        for dataflow in tree.iterfind(dataflow_path,
                                           namespaces=namespaces):
            id = dataflow.get('id')
            agencyID = dataflow.get('agencyID')
            version = dataflow.get('version')
            titles = {}
            for title in dataflow.iterfind(name_path,
                                           namespaces=namespaces):
                language = title.values()
                language = language[0]
                titles[language] = title.text

            self._dataflows[id] = (agencyID, version, titles)

        return self._dataflows
    
    def dataflows(self, flowref=None):
        """Index of available dataflows

        :type: dict"""

        if not self.format == "xml":
            raise ValueError("dataflows() function is not available for %s format" % self.format)

        if self.version == '2_1':
            return self._dataflows_xml_2_1(flowref)
        elif self.version == '2_0':
            return self._dataflows_xml_2_0(flowref)


    def _codes_xml_2_0(self, flowRef):

        self._codes = {}

        codelists_path = ".//message:CodeLists"
        codelist_path = ".//structure:CodeList"
        code_path = ".//structure:Code"
        description_path = ".//structure:Description"
        dimension_path = ".//structure:Dimension"

        url = '/'.join([self.sdmx_url, 'KeyFamily', flowRef])
        with query_rest_xml(url) as file:
            tree = lxml.etree.parse(file)

        namespaces = tree.getroot().nsmap

        codelists = tree.xpath(codelists_path,
                                      namespaces=namespaces)
        for codelists_ in codelists:
            for codelist in codelists_.iterfind(codelist_path,
                                                namespaces=namespaces):
                name = codelist.get('id')
                name = name[3:]
                # a dot "." can't be part of a JSON field name
                name = re.sub(r"\.","",name)
                code = {}
                for code_ in codelist.iterfind(code_path,
                                               namespaces=namespaces):
                    code_key = code_.get('value')
                    code_name = code_.xpath(description_path,
                                            namespaces=namespaces)
                    code_name = code_name[0]
                    code[code_key] = code_name.text
                self._codes[name] = code

        dimension_list = tree.xpath(dimension_path,
                                   namespaces=tree.nsmap)
        self.dimensions = {}
        for dimension in dimension_list:
            name = dimension.get('conceptRef')
            values = dimension.get('codelist')
            self.dimensions[name] = self._codes[values[3:]]

        return self.dimensions

    def _codes_xml_2_1(self, flowRef):

        self._codes = {}
        url = '/'.join([self.sdmx_url, 'datastructure', self.agencyID, flowRef])
        with query_rest_xml(url) as file:
            tree = lxml.etree.parse(file)
        namespaces = tree.getroot().nsmap
        codelists_path = ".//"+self.structure+":Codelists"
        codelist_path = ".//"+self.structure+":Codelist"
        name_path = ".//"+self.common+":Name"
        code_path = ".//"+self.structure+":Code"

        codelists = tree.xpath(codelists_path,
                                      namespaces=namespaces)
        for codelists_ in codelists:
            for codelist in codelists_.iterfind(codelist_path,
                                                namespaces=namespaces):
                name = codelist.xpath(name_path, namespaces=namespaces)
                name = name[0]
                name = name.text
                # a dot "." can't be part of a JSON field name
                name = re.sub(r"\.","",name)
                code = OrderedDict()
                for code_ in codelist.iterfind(code_path,
                                               namespaces=namespaces):
                    code_key = code_.get('id')
                    code_name = code_.xpath(name_path,
                                            namespaces=namespaces)
                    code_name = code_name[0]
                    code[code_key] = code_name.text
                    
                self._codes[name] = code

        return self._codes

    def _codes_json_2_1(self, flowRef):
        
        self._codes = {}
        resource = 'metadata'
        url = '/'.join([self.sdmx_url, resource, flowRef])
        message_dict = self.query_rest_json(url)
        #message_dict['structure']['dimensions']['observation']
        self._codes['header'] = message_dict.pop('header', None)
        for code in message_dict['structure']['dimensions']['observation']:
            self._codes[code['name']] = [(x['id'],x['name']) for x in code['values']]
            
        return self._codes

    def codes(self, flowRef):
        """Data definitions

        Returns a dictionnary describing the available dimensions for a specific flowRef.

        :param flowRef: Identifier of the dataflow
        :type flowRef: str
        :return: dict"""
        
        if self.format == 'xml':            
            if self.version == '2_1':
                return self._codes_xml_2_1(flowRef)
            elif self.version == '2_0':
                return self._codes_xml_2_0(flowRef)
                
        elif self.format == 'json':
            
            if self.version == '2_1':
                return self._codes_json_2_1(flowRef)
                

    def _raw_data_xml_2_0(self, flowRef, key=None, startperiod=None, endperiod=None):

        series_list = [] 
        raw_dates = {}
        raw_values = {}
        raw_attributes = {}
        raw_codes = {}

        resource = 'GenericData'
        key__ = ''
        for key_, value_ in key.items():
            key__ += '&' + key_ + '=' + value_
        key = key__

        if startperiod and endperiod:
            query = (resource + '?dataflow=' + flowRef + key
                    + 'startperiod=' + startperiod
                    + '&endPeriod=' + endperiod)
        else:
            query = resource + '?dataflow=' + flowRef + key
        url = '/'.join([self.sdmx_url,query])
        with query_rest_xml(url) as file:
            tree = lxml.etree.parse(file)
        namespaces = tree.getroot().nsmap

        for series in tree.iterfind(".//generic:Series",
                                         namespaces=namespaces):
            logger.debug('Extracting the series from the SDMX message')
            attributes = []
            values = []
            dimensions = []
            for codes_ in series.iterfind(".//generic:SeriesKey",
                                          namespaces=namespaces):
                codes = OrderedDict()
                for key in codes_.iterfind(".//generic:Value",
                                           namespaces=namespaces):
                    codes[key.get('concept')] = key.get('value')
                logger.debug('Code %s', codes)
            for observation in series.iterfind(".//generic:Obs",
                                               namespaces=namespaces):
                time = observation.xpath(".//generic:Time",
                                               namespaces=namespaces)
                time = time[0].text
                logger.debug('Time vector %s', time)
                dimensions.append(time)
                # I've commented this out as pandas.to_dates seems to do a better job.
                # dimension = date_parser(dimensions[0].text, codes['FREQ'])
                obsvalue = observation.xpath(".//generic:ObsValue",
                                           namespaces=namespaces)
                if obsvalue:
                    value = obsvalue[0].get('value')
                    values.append(value)
                else:
                    # missing value
                    values.append('')
                _attributes = {}
                for attribute in \
                    observation.iterfind(".//generic:Attributes",
                                         namespaces=namespaces):
                    for value_ in \
                        attribute.xpath(
                            ".//generic:Value",
                            namespaces=namespaces):
                        _attributes[value_.get('concept')] = value_.get('value')
                attributes.append(_attributes)
            key = ".".join(codes.values())
            raw_codes[key] = codes
            raw_dates[key] = dimensions
            raw_values[key] = values
            raw_attributes[key] = attributes

        return (raw_values, raw_dates, raw_attributes, raw_codes)

    def _raw_data_xml_2_1(self, flowRef, key=None, startperiod=None, endperiod=None):

        series_list = [] 
        raw_dates = {}
        raw_values = {}
        raw_attributes = {}
        raw_codes = {}

        resource = 'data'
        if startperiod and endperiod:
            query = '/'.join([resource, flowRef, key
                    + '?startperiod=' + startperiod
                    + '&endPeriod=' + endperiod])
        else:
            query = '/'.join([resource, flowRef, key])
        url = '/'.join([self.sdmx_url,query])
        with query_rest_xml(url) as file:
            tree = lxml.etree.parse(file)

        namespaces = tree.getroot().nsmap
        #parser = lxml.etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8') 
        #tree = lxml.etree.fromstring(tree, parser=parser)
        GENERIC = '{'+namespaces['generic']+'}'
        
        for series in tree.iterfind(".//generic:Series",
                                    namespaces=namespaces):
            attributes = {}
            values = []
            dimensions = []
            a_keys = set()
            obs_nbr = 0
            
            for elem in series.iterchildren():
                a = {}
                if elem.tag == GENERIC + 'SeriesKey':
                    codes = OrderedDict()
                    for value in elem.iter(GENERIC + "Value"):
                        codes[value.get('id')] = value.get('value')
                elif elem.tag == GENERIC + 'Obs':
                    a = {}
                    for elem1 in elem.iterchildren():
                        obs_value = False
                        if elem1.tag == GENERIC + 'ObsDimension':
                            dimensions.append(elem1.get('value'))
                        elif elem1.tag == GENERIC + 'ObsValue':
                            value = elem1.get('value')
                            values.append(value)
                            obs_value = True
                        elif elem1.tag == GENERIC + 'Attributes':
                            for elem2 in elem1.iterchildren():
                                key = elem2.get('id') 
                                a[key] = elem2.get('value')
                                a_keys.add(key)
                    if not obs_value:
                        # missing observation
                        values.append('')
                    if len(a):
                        attributes[obs_nbr] = a
                    obs_nbr += 1
            key = ".".join(codes.values())
            raw_codes[key] = codes
            raw_dates[key] = dimensions
            raw_values[key] = values
            a = defaultdict(list)
            for k in a_keys:
                a[k] = [None for v in values]
            for i in attributes:
                for k in attributes[i]:
                    a[k][i] = attributes[i][k]
            raw_attributes[key] = a 

        return (raw_values, raw_dates, raw_attributes, raw_codes)

    def _raw_data_json_2_1(self, flowRef, key=None, startperiod=None, endperiod=None):

        series_list = []
        code_lists = []         
        raw_dates = {}
        raw_values = {}
        raw_attributes = {}
        raw_codes = {}

        if key is None:
            key = 'all'
        resource = 'data'
        if startperiod and endperiod:
            query = '/'.join([resource, flowRef, key
                    + 'all?startperiod=' + startperiod
                    + '&endPeriod=' + endperiod
                    + '&dimensionAtObservation=TIME'])
        else:
            query = '/'.join([resource, flowRef, key,'all'])
        url = '/'.join([self.sdmx_url,query])
        message_dict = self.query_rest_json(url)
        
        dates = message_dict['structure']['dimensions']['observation'][0]
        dates = [node['name'] for node in dates['values']]
        series = message_dict['dataSets'][0]['series']
        dimensions = message_dict['structure']['dimensions']
        
        for dimension in dimensions['series']:
            dimension['keyPosition']
            dimension['id']
            dimension['name']
            dimension['values']

        for key in series:
            dims = key.split(':')
            code = ''
            for dimension, position in zip(dimensions['series'],dims):
                code = code + '.' + dimension['values'][int(position)]['id']
            code_lists.append((key, code))

        for key,code in code_lists:
            observations = message_dict['dataSets'][0]['series'][key]['observations']
            series_dates = [int(point) for point in list(observations.keys())]
            raw_dates[code] = [dates[position] for position in series_dates]
            raw_values[code] = [observations[key][0] for key in list(observations.keys())]
            raw_attributes[code] = [observations[key][1] for key in list(observations.keys())]
            raw_codes[code] = {}
            for code_,dim in zip(key.split(':'),message_dict['structure']['dimensions']['series']):
                raw_codes[code][dim['name']] = dim['values'][int(code_)]['id']

        return (raw_values, raw_dates, raw_attributes, raw_codes)

    def raw_data(self, flowRef, key=None, startperiod=None, endperiod=None):
        """Get data

        :param flowRef: an identifier of the data
        :type flowRef: str
        :param key: a filter using codes (for example, .... for no filter ...BE for all the series related to Belgium) if using v2_1. In 2_0, you should be providing a dict following that syntax {dimension:value}
        :type key: str or dict
        :param startperiod: the starting date of the time series that will be downloaded (optional, default: None)
        :type startperiod: datetime.datetime()
        :param endperiod: the ending date of the time series that will be downloaded (optional, default: None)
        :type endperiod: datetime.datetime()
        :param d: a dict of global metadata.    

        :return: tuple of the form (l, d) or (df, d) depending on the value of 'concat'.
        """
       
        if self.format == "xml":
            if self.version == '2_1':
                return self._raw_data_xml_2_1(flowRef, key=key, 
                                              startperiod=startperiod, 
                                              endperiod=endperiod)
                
            elif self.version == '2_0':
                return self._raw_data_xml_2_0(flowRef, key=key, 
                                              startperiod=startperiod, 
                                              endperiod=endperiod)
                
        elif self.format == "json":
            if self.version == '2_1':
                return self._raw_data_json_2_1(flowRef, key=key, 
                                              startperiod=startperiod, 
                                              endperiod=endperiod)
            

    def data(self, flowRef, key, startperiod=None, endperiod=None, 
        concat = False):
        """Get data in a format that is easy to use interactively
        
        :param flowRef: an identifier of the data
        :type flowRef: str
        :param key: a filter using codes (for example, .... for no filter ...BE for all the series related to Belgium) if using v2_1. In 2_0, you should be providing a dict following that syntax {dimension:value}
        :type key: str or dict
        :param startperiod: the starting date of the time series that will be downloaded (optional, default: None)
        :type startperiod: datetime.datetime()
        :param endperiod: the ending date of the time series that will be downloaded (optional, default: None)
        :type endperiod: datetime.datetime()
        :param concat: If False, return a tuple (l, d) where l is a list of the series whose name attributes contain  the metadata as namedtuple, and d is a dict containing any global metadata. If True: return a tuple (df, d) where df is a pandas.DataFrame with hierarchical index generated from the metadata. Explore the structure by issuing 'df.columns.names' and 'df.columns.levels' The order of index levels is determined by the number of actual values found in the series' metadata for each key. If concat is a list of metadata keys, they determine the order of index levels.
        :param d: a dict of global metadata.    

        :return: tuple of the form (l, d) or (df, d) depending on the value of 'concat'.
        """
        (raw_values, raw_dates, raw_attributes, raw_codes) = self.raw_data(flowRef,key,startperiod,endperiod)  

        # make pandas
        series_list = []
        for key in raw_values:
            dates = pandas.to_datetime(raw_dates[key])
            value_series = pandas.TimeSeries(raw_values[key], index = dates, dtype = 'float64', name = raw_codes[key])
            series_list.append(value_series)

        # Handle empty lists
        if series_list == []: 
            if concat:
                return pandas.DataFrame(), {}
            else:
                return [], {}
            
        # Prepare the codes, remove global codes applying to all series.
        code_sets = {k : list(set([s.name[k] for s in series_list])) 
                     for k in series_list[0].name}
            
        global_codes = {k : code_sets[k][0] for k in code_sets 
                            if len(code_sets[k]) == 1}
        # Remove global codes as they should not lead to index levels in the DataFrame 
        for k in global_codes: code_sets.pop(k)
        
        if type(concat) == bool:
            # Sort the keys with llargest set first unless concat defines the order through a list. 
            lengths = [(len(code_sets[k]), k) for k in code_sets]
            lengths.sort(reverse = True)
            sorted_keys = [k[1] for k in lengths]
        else: # so concat must be a list containing exactly the non-global keys in the desired order
            # Remove any global codes from the list
            sorted_keys = [k for k in concat if k not in global_codes.keys()] 
        if concat:    
            # Construct the multi-index from the Cartesian product of the sets.
            # This may generate too many columns if not all possible 
            # tuples are needed. But it seems very difficult to construct a
            # minimal multi-index from the series_list.
            
            column_index = pandas.MultiIndex.from_product(
                [code_sets[k] for k in sorted_keys])
            column_index.names = sorted_keys 
            df = pandas.DataFrame(columns = column_index, index = series_list[0].index)
                # Add the series to the DataFrame. Generate column keys from the metadata        
            for s in series_list:
                column_pos = [s.name[k] for k in sorted_keys]
                # s.name = None 
                df[tuple(column_pos)] = s
            return df, global_codes
            
        else:
            # Create a list of Series
            # Prepare the sorted metadata of each series
            for s in series_list:
                for k in global_codes: s.name.pop(k)
                s.name = to_namedtuple([(k, s.name[k]) for k in sorted_keys])             
            return series_list, global_codes


eurostat = Repository('http://www.ec.europa.eu/eurostat/SDMX/diss-web/rest',
                     'xml', '2_1','ESTAT')
eurostat.category_scheme_url = 'http://sdw-ws.ecb.europa.eu/Dataflow'
eurostat_test = Repository('http://localhost:8800/eurostat',
                     'xml', '2_1','ESTAT')
ecb = Repository('http://sdw-ws.ecb.europa.eu',
                     'xml', '2_0','ECB', timeout=190)
ecb.dataflow_url = 'http://sdw-ws.ecb.europa.eu/Dataflow'
ecb2_1 = Repository('https://sdw-wsrest.ecb.europa.eu/service/', 'xml', '2_1', 'ECB', timeout=190)
ilo = Repository('http://www.ilo.org/ilostat/sdmx/ws/rest/',
                     'xml', '2_1','ILO')
fao = Repository('http://data.fao.org/sdmx',
                     'xml', '2_1','FAO')
insee = Repository('http://www.bdm.insee.fr/series/sdmx','xml', '2_1','INSEE')
insee.category_scheme_url = 'http://www.bdm.insee.fr/series/sdmx/categoryscheme'

oecd = Repository('http://stats.oecd.org/sdmx-json','json', '2_1','OECD', timeout=120)

__all__ = ('ecb','ilo','fao','eurostat','insee','Repository')

if __name__ == "__main__":
    eurostat_test.raw_data('ei_bsco_q','....')
    eurostat_test.data('ei_bsco_q','....')
