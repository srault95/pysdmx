# -*- coding: utf-8 -*-

import os
import unittest
import httpretty
from pprint import pprint

from sdmx_tests import resources
from sdmx_tests.resources import json_2_1
from sdmx_tests.resources import xml_2_0
from sdmx_tests.resources import xml_2_1
from sdmx import Repository

#TODELETE
import requests

RESOURCES = os.path.abspath(os.path.dirname(resources.__file__))
RESOURCES_JSON_2_1 = os.path.abspath(os.path.dirname(json_2_1.__file__))
RESOURCES_XML_2_0 = os.path.abspath(os.path.dirname(xml_2_0.__file__))
RESOURCES_XML_2_1 = os.path.abspath(os.path.dirname(xml_2_1.__file__))

class SDMXTestCase(unittest.TestCase):
    """Tests des fonctions de base - Hors implémentations SDMX
    """
    
    # nosetests -s -v sdmx_tests.base:SDMXTestCase

    def test_url(self):

        with self.assertRaises(ValueError) as err:
            Repository()

        self.assertEquals(str(err.exception), "Require sdmx_url parameter")

        repo = Repository(sdmx_url="http://example.org", 
                          format="xml",                          
                          version="2_1",
                          agencyID="X1")

        repo = Repository(sdmx_url="http://example.org", 
                          format="json",                          
                          version="2_1",
                          agencyID=None)


    def test_format(self):

        with self.assertRaises(ValueError) as err:
            Repository(sdmx_url="http://example.org", format="BAD")
                
        self.assertEquals(str(err.exception), 
                          "Not implemented SDMX format [BAD]")
        
    def test_version(self):
        
        with self.assertRaises(ValueError) as err:
            Repository(sdmx_url="http://example.org", 
                       format="xml", version="0")
                
        self.assertEquals(str(err.exception), 
                          "Not implemented SDMX ML version [0]")

        with self.assertRaises(ValueError) as err:
            Repository(sdmx_url="http://example.org", 
                       format="json", version="2_0")

        self.assertEquals(str(err.exception), 
                          "Not implemented SDMX JSON version [2_0]")

    #@httpretty.activate
    @unittest.skipIf(True, "TODO")
    def test_query_rest_json(self):
        pass    
        #TODO: erreurs 4xx et 5xx
        #TODO: redirect 3xx
        #TODO: json error
        #TODO: orderedDict
        #TODO: client request custom

    #@httpretty.activate
    @unittest.skipIf(True, "TODO")
    def test_query_rest_xml(self):
        pass
        #TODO: erreurs 4xx et 5xx
        #TODO: redirect 3xx
        #TODO: parse xml    
        #TODO: client request custom

class SDMX_XML_2_0_TestCase(unittest.TestCase):
    """Tests of SDMX ML 2.0
    
    @see: https://github.com/sdmx-twg/sdmx-ml-v2_0
    
    http://sdw-ws.ecb.europa.eu/CategoryScheme
    
    Sur upsert_categories: 1 fois par dataset:
        http://sdw-ws.ecb.europa.eu/Dataflow/8157814
    """

    @unittest.skipIf(True, "TODO")
    def test_categories(self):
        pass

    @unittest.skipIf(True, "TODO")
    def test_dataflows(self):
        pass

    @unittest.skipIf(True, "TODO")
    def test_codes(self):
        pass

    @unittest.skipIf(True, "TODO")
    def test_raw_data(self):
        pass

class SDMX_XML_2_1_TestCase(unittest.TestCase):
    """Tests of SDMX ML 2.1
    
    @see: https://github.com/sdmx-twg/sdmx-ml-v2_1
    """

    @unittest.skipIf(True, "TODO")
    def test_categories(self):
        pass

    @unittest.skipIf(True, "TODO")
    def test_dataflows(self):
        pass

    #@unittest.skipIf(True, "TODO")
    @httpretty.activate
    def test_codes(self):
        #https://raw.githubusercontent.com/sdmx-twg/sdmx-ml-v2_1/master/samples/common/common.xml
        codes_fp = os.path.abspath(os.path.join(RESOURCES_XML_2_1, 
                                                   "common.xml"))

        body = None
        with open(codes_fp) as fp:
            body = fp.read()

        httpretty.register_uri(httpretty.GET, 
                               "http://ec.europa.eu/eurostat/SDMX/diss-web/rest/datastructure/ESTAT/DSD_nama_gdp_c",
                               body=body,
                               status=200,
                               content_type="application/xml"
                               )

        sdmx_client = Repository(sdmx_url='http://ec.europa.eu/eurostat/SDMX/diss-web/rest', 
                                 format="xml", 
                                 version="2_1",
                                 agencyID='ESTAT',
                                 namespace_style='long'
                                )

        model = {'Code list for Decimals (DECIMALS)': {'0': 'Zero',
                                       '1': 'One',
                                       '2': 'Two',
                                       '3': 'Three',
                                       '4': 'Four',
                                       '5': 'Five',
                                       '6': 'Six',
                                       '7': 'Seven',
                                       '8': 'Eight',
                                       '9': 'Nine'},
                 'Code list for Frequency (FREQ)': {'A': 'Annual',
                                                    'B': 'Daily - business week',
                                                    'D': 'Daily',
                                                    'M': 'Monthly',
                                                    'N': 'Minutely',
                                                    'Q': 'Quarterly',
                                                    'S': 'Half Yearly, semester',
                                                    'W': 'Weekly'},
                 'Observation status': {'A': 'Normal',
                                        'B': 'Break',
                                        'E': 'Estimated value',
                                        'F': 'Forecast value',
                                        'I': 'Imputed value (CCSA definition)',
                                        'M': 'Missing value',
                                        'P': 'Provisional value',
                                        'S': 'Strike'},
                 'code list for Confidentiality Status (CONF_STATUS)': {'C': 'Confidential '
                                                                             'statistical '
                                                                             'information',
                                                                        'D': 'Secondary '
                                                                             'confidentiality '
                                                                             'set by the '
                                                                             'sender, not '
                                                                             'for\t'
                                                                             'publication',
                                                                        'F': 'Free',
                                                                        'N': 'Not for '
                                                                             'publication, '
                                                                             'restricted '
                                                                             'for internal '
                                                                             'use only',
                                                                        'S': 'Secondary '
                                                                             'confidentiality '
                                                                             'set and '
                                                                             'managed by '
                                                                             'the receiver, '
                                                                             'not for '
                                                                             'publication'},
                 'code list for the Unit Multiplier (UNIT_MULT)': {'0': 'Units',
                                                                   '1': 'Tens',
                                                                   '2': 'Hundreds',
                                                                   '3': 'Thousands',
                                                                   '4': 'Tens of thousands',
                                                                   '6': 'Millions',
                                                                   '9': 'Billions',
                                                                   '12': 'Trillions',
                                                                   '15': 'Quadrillions'}}
        result = sdmx_client.codes("DSD_nama_gdp_c")
        self.assertEqual(result,model)

    @unittest.skipIf(True, "TODO")
    def test_raw_data(self):
        pass

class SDMX_JSON_2_1_TestCase(unittest.TestCase):
    """Tests of SDMX JSON 2.1
    
    @see: https://github.com/sdmx-twg/sdmx-json
    """
    
    # nosetests -s -v sdmx_tests.base:SDMX_JSON_2_1_TestCase    

    @httpretty.activate
    def test_codes(self):

        # nosetests -s -v sdmx_tests.base:SDMX_JSON_2_1_TestCase.test_codes
        
        #TODO: trouver exemple metadata standard
        #TODO: vérifier implémentation metadata OECD ailleurs
        
        metadata_fp = os.path.abspath(os.path.join(RESOURCES_JSON_2_1, 
                                                   "oecd_mei_metadata.json"))

        body = None
        with open(metadata_fp) as fp:
            body = fp.read()       

        httpretty.register_uri(httpretty.GET, 
                               "http://stats.oecd.org/sdmx-json/metadata/MEI",
                               body=body,
                               status=200,
                               content_type="application/json"
                               )

        sdmx_client = Repository(sdmx_url='http://stats.oecd.org/sdmx-json', 
                                 format="json", 
                                 version="2_1")
        
        codes1 = sdmx_client.codes("MEI")
        codes2 = sdmx_client._codes_json_2_1("MEI")
                
        self.assertDictEqual(codes1, codes2)
        
        self.assertTrue("header" in codes1.keys())
        
        #pprint(codes1)
        
        """
        {'Country': [('TEST', 'Test')],
         'Frequency': [('A', 'Annual'), ('Q', 'Quarterly'), ('M', 'Monthly')],
         'Measure': [('MEI', 'Main Economic Indicators')],
         'Subject': [('BPFAFD01',
                      'Balance of Payments > Financial Account > Financial '
                      'derivatives > Net financial derivatives')],
         'Time': [('1955', '1955'), ('1955-Q1', 'Q1-1955'), ('1961-08', 'Aug-1961')],
         'header': {'id': 'fca64b8f-cd96-4464-8839-2ca1018474c6',
                    'test': False,
                    'prepared': '2015-10-29T06:39:18.634125Z',
                    'sender': {'id': 'OECD',
                               'name': 'Organisation for Economic Co-operation and '
                                       'Development'},
                    'links': [{'href': 'http://stats.oecd.org:80/sdmx-json/metadata/MEI',
                               'rel': 'request'}]}}        
        """
        
    @httpretty.activate
    def test_raw_data(self):

        # nosetests -s -v sdmx_tests.base:SDMX_JSON_2_1_TestCase.test_raw_data

        #https://github.com/sdmx-twg/sdmx-json/blob/master/data-message/samples/exr/exr-time-series.json
        series_fp = os.path.abspath(os.path.join(RESOURCES_JSON_2_1, 
                                                   "exr-time-series.json"))

        body = None
        with open(series_fp) as fp:
            body = fp.read()       

        #http://stats.oecd.org/sdmx-json/data/MEI/all/all
        #http://stats.oecd.org/sdmx-json/data/MEI/NZD.../all
        httpretty.register_uri(httpretty.GET, 
                               "http://stats.oecd.org/sdmx-json/data/MEI/all/all",
                               body=body,
                               status=200,
                               content_type="application/json"
                               )

        sdmx_client = Repository(sdmx_url='http://stats.oecd.org/sdmx-json', 
                                 format="json", 
                                 version="2_1")
        

        #TODO: country
        #raw_values, raw_dates, raw_attributes, raw_codes = \
        #    sdmx_client.raw_data("MEI", "NZD...")
        
        raw_values, raw_dates, raw_attributes, raw_codes = \
            sdmx_client.raw_data("MEI")

        raw_values2, raw_dates2, raw_attributes2, raw_codes2 = \
            sdmx_client._raw_data_json_2_1("MEI")

        self.assertDictEqual(raw_values, raw_values2)        
        self.assertDictEqual(raw_dates, raw_dates2)        
        self.assertDictEqual(raw_attributes, raw_attributes2)        
        self.assertDictEqual(raw_codes, raw_codes2)        

        """
        print("-----------------")        
        pprint(raw_codes)
        pprint(raw_values)
        pprint(raw_dates)
        pprint(raw_attributes)
        -----------------
        {'.NZD': {'Currency': 'NZD'}, '.RUB': {'Currency': 'RUB'}}
        {'.NZD': [1.5931, 1.5925], '.RUB': [40.3426, 40.3]}
        {'.NZD': ['2013-01-18', '2013-01-21'], '.RUB': ['2013-01-18', '2013-01-21']}
        {'.NZD': [0, 0], '.RUB': [0, 0]}        
        """    
        
    @unittest.skipIf(True, "TODO")
    def test_categories(self):
        pass
