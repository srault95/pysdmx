#! /usr/bin/env python3
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

import requests
import pandas
import lxml.etree
import datetime, time
from io import BytesIO,StringIO
import re
import zipfile
from collections import OrderedDict, namedtuple, defaultdict
import logging
from pprint import pprint
import json


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
    


class Repository(object):
    """Data provider. This is the main class that allows practical access to all the data.

    :ivar sdmx_url: The URL of the SDMX endpoint, the webservice employed to access the data.
    :type sdmx_url: str
    :ivar agencyID: An identifier of the statistical provider.
    :type agencyID: str
    """
    def __init__(self, sdmx_url, format, version, agencyID):
        self.lgr = logging.getLogger('pysdmx')
        self.lgr.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler('pysdmx.log')
        self.fh.setLevel(logging.DEBUG)
        self.frmt = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.frmt)
        self.lgr.addHandler(self.fh)
        self.sdmx_url = sdmx_url
        self.format = format
        self.agencyID = agencyID
        self._dataflows = None
        self.version = version
        if self.format == 'xml':
            self.dataflow_url = '/'.join([self.sdmx_url, 'dataflow', self.agencyID, 'all', 'latest'])
            self.category_scheme_url = '/'.join([self.sdmx_url, 'CategoryScheme'])
        if self.format == 'json':
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
        self.lgr.info('Requesting %s', url)
        request = requests.get(url, timeout= 50)
        return json.load(StringIO(request.text), object_pairs_hook=OrderedDict)
    
    def query_rest(self, url):
        """Retrieve SDMX messages.

        :param url: The URL of the message.
        :type url: str
        :return: An lxml.etree.ElementTree() of the SDMX message
        """
        # Fetch data from the provider    
        self.lgr.info('Requesting %s', url)
        request = requests.get(url, timeout= 20)
        if request.status_code == requests.codes.ok:
            response_str = request.text.encode('utf-8')
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
                        response_str = file.read(filename)
                        break
                        if not response_str :
                            raise Exception("The provider has not delivered the file you are looking for.")
            else:
                raise ValueError("Error getting client({})".format(request.status_code))      
        else:
            raise ValueError("Error getting client({})".format(request.status_code))
        return lxml.etree.fromstring(response_str)

    @property
    def categories(self):
        """Index of available categories

        :type: dict"""
        def walk_category(category):
            category_ = {}
            if self.version == '2_0':
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
            elif self.version == '2_1':
                name = category.xpath("./com:Name[@xml:lang='en']",namespaces=category.nsmap)
                category_['name'] = name[0].text
                category_['id'] = category.attrib['id']
                subcategories = []
                for subcategory in category.xpath('./str:Category',
                                                  namespaces=category.nsmap):
                    subcategories.append(walk_category(subcategory))
                if subcategories != []:
                    category_['subcategories'] = subcategories
            return category_

        if self.version == '2_0':
            tree = self.query_rest(self.category_scheme_url)
            xml_categories = tree.xpath('.//structure:CategoryScheme',
                                        namespaces=tree.nsmap)
        elif self.version == '2_1':
            tree = self.query_rest(self.sdmx_url + '/categoryscheme')
            xml_categories = tree.xpath('.//str:CategoryScheme',
                                        namespaces=tree.nsmap)
            
        return walk_category(xml_categories[0])
    
    def dataflows(self, flowref=None):
        """Index of available dataflows

        :type: dict"""
        if self.version == '2_1':
            tree = self.query_rest(self.dataflow_url)
            dataflow_path = ".//str:Dataflow"
            name_path = ".//com:Name"
            self._dataflows = {}
            for dataflow in tree.iterfind(dataflow_path,
                                               namespaces=tree.nsmap):
                id = dataflow.get('id')
                agencyID = dataflow.get('agencyID')
                version = dataflow.get('version')
                titles = {}
                for title in dataflow.iterfind(name_path,
                                               namespaces=tree.nsmap):
                    language = title.values()
                    language = language[0]
                    titles[language] = title.text
                self._dataflows[id] = (agencyID, version, titles)
        if self.version == '2_0':
            tree = self.query_rest(self.dataflow_url+'/'+str(flowref))
            dataflow_path = ".//structure:Dataflow"
            name_path = ".//structure:Name"
            keyid_path = ".//structure:KeyFamilyID"
            self._dataflows = {}
            for dataflow in tree.iterfind(dataflow_path,
                                               namespaces=tree.nsmap):
                for id in dataflow.iterfind(keyid_path,
                                               namespaces=tree.nsmap):
                    id = id.text
                agencyID = dataflow.get('agencyID')
                version = dataflow.get('version')
                titles = {}
                for title in dataflow.iterfind(name_path,
                                               namespaces=tree.nsmap):
                    titles['en'] = title.text
                self._dataflows[id] = (agencyID, version, titles)
        return self._dataflows

    def codes(self, flowRef):
        """Data definitions

        Returns a dictionnary describing the available dimensions for a specific flowRef.

        :param flowRef: Identifier of the dataflow
        :type flowRef: str
        :return: dict"""
        if self.version == '2_1':
            url = '/'.join([self.sdmx_url, 'datastructure', self.agencyID, 'DSD_' + flowRef])
            tree = self.query_rest(url)
            codelists_path = ".//str:Codelists"
            codelist_path = ".//str:Codelist"
            name_path = ".//com:Name"
            code_path = ".//str:Code"
            self._codes = {}
            codelists = tree.xpath(codelists_path,
                                          namespaces=tree.nsmap)
            for codelists_ in codelists:
                for codelist in codelists_.iterfind(codelist_path,
                                                    namespaces=tree.nsmap):
                    name = codelist.xpath(name_path, namespaces=tree.nsmap)
                    name = name[0]
                    name = name.text
                    # a dot "." can't be part of a JSON field name
                    name = re.sub(r"\.","",name)
                    code = OrderedDict()
                    for code_ in codelist.iterfind(code_path,
                                                   namespaces=tree.nsmap):
                        code_key = code_.get('id')
                        code_name = code_.xpath(name_path,
                                                namespaces=tree.nsmap)
                        code_name = code_name[0]
                        code[code_key] = code_name.text
                    self._codes[name] = code
        if self.version == '2_0':
            codelists_path = ".//message:CodeLists"
            codelist_path = ".//structure:CodeList"
            code_path = ".//structure:Code"
            description_path = ".//structure:Description"
            url = '/'.join([self.sdmx_url, 'KeyFamily', self.agencyID + '_' + flowRef])
            tree = self.query_rest(url)
            self._codes = {}
            codelists = tree.xpath(codelists_path,
                                          namespaces=tree.nsmap)
            for codelists_ in codelists:
                for codelist in codelists_.iterfind(codelist_path,
                                                    namespaces=tree.nsmap):
                    name = codelist.get('id')
                    name = name[3:]
                    # a dot "." can't be part of a JSON field name
                    name = re.sub(r"\.","",name)
                    code = {}
                    for code_ in codelist.iterfind(code_path,
                                                   namespaces=tree.nsmap):
                        code_key = code_.get('value')
                        code_name = code_.xpath(description_path,
                                                namespaces=tree.nsmap)
                        code_name = code_name[0]
                        code[code_key] = code_name.text
                    self._codes[name] = code
        return self._codes


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
       
        series_list = [] 
        
        if self.format == "xml":
            if self.version == '2_1':
                resource = 'data'
                if startperiod and endperiod:
                    query = '/'.join([resource, flowRef, key
                            + '?startperiod=' + startperiod
                            + '&endPeriod=' + endperiod])
                else:
                    query = '/'.join([resource, flowRef, key])
                url = '/'.join([self.sdmx_url,query])
                tree = self.query_rest(url)
                #parser = lxml.etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8') 
                #tree = lxml.etree.fromstring(tree, parser=parser)
                GENERIC = '{'+tree.nsmap['generic']+'}'
                
                raw_codes = {}
                raw_dates = {}
                raw_values = {}
                raw_attributes = {}
                for series in tree.iterfind(".//generic:Series",
                                            namespaces=tree.nsmap):
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

                                if elem1.tag == GENERIC + 'ObsDimension':
                                    dimensions.append(elem1.get('value'))
                                elif elem1.tag == GENERIC + 'ObsValue':
                                    value = elem1.get('value')
                                    values.append(value)
                                elif elem1.tag == GENERIC + 'Attributes':
                                    for elem2 in elem1.iterchildren():
                                        key = elem2.get('id') 
                                        a[key] = elem2.get('value')
                                        a_keys.add(key)
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
            elif self.version == '2_0':
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
                tree = self.query_rest(url)

                raw_codes = {}
                raw_dates = {}
                raw_values = {}
                raw_attributes = {}
                for series in tree.iterfind(".//generic:Series",
                                                 namespaces=tree.nsmap):
                    self.lgr.debug('Extracting the series from the SDMX message')
                    attributes = {}
                    values = []
                    dimensions = []
                    for codes_ in series.iterfind(".//generic:SeriesKey",
                                                  namespaces=tree.nsmap):
                        codes = OrderedDict()
                        for key in codes_.iterfind(".//generic:Value",
                                                   namespaces=tree.nsmap):
                            codes[key.get('concept')] = key.get('value')
                        self.lgr.debug('Code %s', codes)
                    for observation in series.iterfind(".//generic:Obs",
                                                       namespaces=tree.nsmap):
                        time = observation.xpath(".//generic:Time",
                                                       namespaces=tree.nsmap)
                        time = time[0].text
                        self.lgr.debug('Time vector %s', time)
                        dimensions.append(time)
                        # I've commented this out as pandas.to_dates seems to do a better job.
                        # dimension = date_parser(dimensions[0].text, codes['FREQ'])
                        obsvalue = observation.xpath(".//generic:ObsValue",
                                                   namespaces=tree.nsmap)
                        value = obsvalue[0].get('value')
                        values.append(value)
                        attributes = {}
                        for attribute in \
                            observation.iterfind(".//generic:Attributes",
                                                 namespaces=tree.nsmap):
                            for value_ in \
                                attribute.xpath(
                                    ".//generic:Value",
                                    namespaces=tree.nsmap):
                                attributes[value_.get('concept')] = value_.get('value')
                    key = ".".join(codes.values())
                    raw_codes[key] = codes
                    raw_dates[key] = dimensions
                    raw_values[key] = values
                    raw_attributes[key] = attributes
            else: raise ValueError("SDMX version must be either '2_0' or '2_1'. %s given." % self.version)
        elif self.format == "json":
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
            code_lists = []
            for key in series:
                dims = key.split(':')
                code = ''
                for dimension, position in zip(dimensions['series'],dims):
                    code = code + '.' + dimension['values'][int(position)]['id']
                code_lists.append((key, code))
            raw_dates = {}
            raw_values = {}
            raw_attributes = {}
            raw_codes = {}
            for key,code in code_lists:
                observations = message_dict['dataSets'][0]['series'][key]['observations']
                series_dates = [int(point) for point in list(observations.keys())]
                raw_dates[code] = [dates[position] for position in series_dates]
                raw_values[code] = [observations[key][0] for key in list(observations.keys())]
                raw_attributes[code] = [observations[key][1] for key in list(observations.keys())]
                print(key.split(':'))
                print(message_dict['structure']['dimensions']['series'])
                print([i for i in zip(key.split(':'),message_dict['structure']['dimensions']['series'])])
                raw_codes[code] = {}
                for code_,dim in zip(key.split(':'),message_dict['structure']['dimensions']['series']):
                    raw_codes[code][dim['values'][int(code_)]['id']] = dim['name'] 
        return (raw_values, raw_dates, raw_attributes, raw_codes)

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
                     'xml', '2_0','ECB')
ecb.dataflow_url = 'http://sdw-ws.ecb.europa.eu/Dataflow'
ecb2_1 = Repository('https://sdw-wsrest.ecb.europa.eu/service/', 'xml', '2_1', 'ECB')
ilo = Repository('http://www.ilo.org/ilostat/sdmx/ws/rest/',
                     'xml', '2_1','ILO')
fao = Repository('http://data.fao.org/sdmx',
                     'xml', '2_1','FAO')
insee = Repository('http://www.bdm.insee.fr/series/sdmx','xml', '2_1','INSEE')
insee.category_scheme_url = 'http://www.bdm.insee.fr/series/sdmx/categoryscheme'

oecd = Repository('http://stats.oecd.org/sdmx-json','json', '2_1','OECD')

__all__ = ('ecb','ilo','fao','eurostat','insee','Repository')

if __name__ == "__main__":
    eurostat_test.raw_data('ei_bsco_q','....')
    eurostat_test.data('ei_bsco_q','....')
