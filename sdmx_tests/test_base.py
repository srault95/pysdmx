# -*- coding: utf-8 -*-

import os
import unittest
import httpretty
import pprint

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

    @httpretty.activate
    def test_raw_data(self):
        #https://sdw-wsrest.ecb.europa.eu/service/categoryscheme
        data_fp = os.path.abspath(os.path.join(RESOURCES_XML_2_0, 
                                                   "GenericSample.xml"))

        body = None
        with open(data_fp) as fp:
            body = fp.read()

        httpretty.register_uri(httpretty.GET, 
                               "https://sdw-wsrest.ecb.europa.eu/GenericData?dataflow=EXR",
                               body=body,
                               status=200,
                               content_type="application/xml"
                               )

        sdmx_client = Repository(sdmx_url='https://sdw-wsrest.ecb.europa.eu', 
                                 format="xml", 
                                 version="2_0",
                                 agencyID='ECB',
                                 namespace_style='short'
                                )



        model = ({'A.P.A.MX': ['3.14'],
                  'M.P.A.MX': ['3.14',
                               '3.14',
                               '4.29',
                               '6.04',
                               '5.18',
                               '5.07',
                               '3.13',
                               '1.17',
                               '1.14',
                               '3.04',
                               '1.14',
                               '3.24']},
                 {'A.P.A.MX': ['2000-01'],
                  'M.P.A.MX': ['2000-01',
                               '2000-02',
                               '2000-03',
                               '2000-04',
                               '2000-05',
                               '2000-06',
                               '2000-07',
                               '2000-08',
                               '2000-09',
                               '2000-10',
                               '2000-11',
                               '2000-12']},
                 {'A.P.A.MX': [{'OBS_STATUS': 'A'}],
                  'M.P.A.MX': [{'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'},
                               {'OBS_STATUS': 'A'}]},
                 {'A.P.A.MX': {'FREQ': 'A',
                               'JD_TYPE': 'P',
                               'JD_CATEGORY': 'A',
                               'VIS_CTY': 'MX'},
                  'M.P.A.MX': {'FREQ': 'M',
                               'JD_TYPE': 'P',
                               'JD_CATEGORY': 'A',
                               'VIS_CTY': 'MX'}})

        result = sdmx_client.raw_data('EXR', {})

        self.assertEqual(result,model)

class SDMX_XML_2_1_TestCase(unittest.TestCase):
    """Tests of SDMX ML 2.1
    
    @see: https://github.com/sdmx-twg/sdmx-ml-v2_1
    """

    @httpretty.activate
    def test_categories(self):
        #https://sdw-wsrest.ecb.europa.eu/service/categoryscheme
        codes_fp = os.path.abspath(os.path.join(RESOURCES_XML_2_1, 
                                                   "categoryscheme.xml"))

        body = None
        with open(codes_fp) as fp:
            body = fp.read()

        httpretty.register_uri(httpretty.GET, 
                               "https://sdw-wsrest.ecb.europa.eu/service/categoryscheme",
                               body=body,
                               status=200,
                               content_type="application/xml"
                               )

        sdmx_client = Repository(sdmx_url='https://sdw-wsrest.ecb.europa.eu/service', 
                                 format="xml", 
                                 version="2_1",
                                 agencyID='ECB',
                                 namespace_style='short'
                                )


        model = [{'id': '01', 'name': {'en': 'Monetary operations'}},
                 {'id': '02', 'name': {'en': 'Prices, output, demand and labour market'}},
                 {'id': '03', 'name': {'en': 'Monetary and financial statistics'}},
                 {'id': '04', 'name': {'en': 'Euro area accounts'}},
                 {'id': '05', 'name': {'en': 'Government finance'}},
                 {'id': '06', 'name': {'en': 'External transactions and positions'}},
                 {'id': '07', 'name': {'en': 'Exchange rates'}},
                 {'id': '08',
                  'name': {'en': 'Payments and securities trading, clearing, settlement'}},
                 {'id': '09', 'name': {'en': 'Banknotes and Coins'}},
                 {'id': '10', 'name': {'en': 'Indicators of Financial Integration'}},
                 {'id': '11', 'name': {'en': 'Real Time Database (research database)'}},
                 {'id': '01', 'name': {'en': 'Key euro area indicators'}},
                 {'id': '02', 'name': {'en': 'Exchange rates'}},
                 {'id': '03', 'name': {'en': 'Monetary aggregates'}},
                 {'id': '04', 'name': {'en': 'Bank interest rates'}},
                 {'id': '05', 'name': {'en': 'Prices'}},
                 {'id': '06', 'name': {'en': 'Government finance'}},
                 {'id': '01', 'name': {'en': 'Monetary operations'}},
                 {'id': '02', 'name': {'en': 'Prices, output, demand and labour market'}},
                 {'id': '03', 'name': {'en': 'Monetary and financial statistics'}},
                 {'id': '06', 'name': {'en': 'External transactions and positions'}},
                 {'id': '07', 'name': {'en': 'Exchange rates'}},
                 {'id': '08',
                  'name': {'en': 'Payments and securities trading, clearing, settlement'}},
                 {'id': '09', 'name': {'en': 'Banknotes and Coins'}}]
        result = sdmx_client.categories
        self.assertEqual(result,model)

    @httpretty.activate
    def test_categories_insee(self):
        #https://sdw-wsrest.ecb.europa.eu/service/categoryscheme
        codes_fp = os.path.abspath(os.path.join(RESOURCES_XML_2_1, 
                                                   "categoryscheme_insee.xml"))

        body = None
        with open(codes_fp) as fp:
            body = fp.read()

        httpretty.register_uri(httpretty.GET, 
                               "http://www.bdm.insee.fr/series/sdmx/categoryscheme",
                               body=body,
                               status=200,
                               content_type="application/xml"
                               )

        sdmx_client = Repository(sdmx_url='http://www.bdm.insee.fr/series/sdmx', 
                                 format="xml", 
                                 version="2_1",
                                 agencyID='INSEE',
                                 namespace_style='short'
                                )


        model = [{'id': 'COMPTA-NAT',
                  'name': {'en': 'National accounts (GDP, consumption...)',
                           'fr': 'Comptabilité nationale (PIB, consommation...)'},
                  'subcategories': [{'id': 'CRA',
                                     'name': {'en': 'Annual regional accounts',
                                              'fr': 'Comptes régionaux annuels'},
                                     'subcategories': [{'id': 'CRA-2005',
                                                        'name': {'en': 'Base year 2005',
                                                                 'fr': 'Base 2005'}},
                                                       {'id': 'CRA-2010',
                                                        'name': {'en': 'Base 2010',
                                                                 'fr': 'Base 2010'}}]},
                                    {'id': 'FINANCES-PUBLIQUES',
                                     'name': {'en': 'Government finance',
                                              'fr': 'Finances publiques'},
                                     'subcategories': [{'id': 'COMPTES-PUBLICS',
                                                        'name': {'en': 'Public Accounts',
                                                                 'fr': 'Comptes publics'}},
                                                       {'id': 'DEPENSES-APU',
                                                        'name': {'en': 'General '
                                                                       'government '
                                                                       'expenditure',
                                                                 'fr': 'Dépenses des '
                                                                       'administrations '
                                                                       'publiques (APU)'}},
                                                       {'id': 'COMPTES-APU-MAASTRICHT',
                                                        'name': {'en': 'General '
                                                                       'government '
                                                                       'debt and '
                                                                       'deficit as '
                                                                       'defined by '
                                                                       'Maastricht',
                                                                 'fr': 'Dette et '
                                                                       'déficit des '
                                                                       'administrations '
                                                                       'publiques au '
                                                                       'sens de '
                                                                       'Maastricht'}}]},
                                    {'id': 'CNT',
                                     'name': {'en': 'Quaterly national accounts',
                                              'fr': 'Comptes nationaux trimestriels'},
                                     'subcategories': [{'id': 'CONSO-MENAGES',
                                                        'name': {'en': 'Household '
                                                                       'consumption',
                                                                 'fr': 'Consommation '
                                                                       'des ménages'}},
                                                       {'id': 'CNT-CSI',
                                                        'name': {'en': 'Institutional '
                                                                       'sector accounts',
                                                                 'fr': 'Comptes des '
                                                                       'secteurs '
                                                                       'institutionnels'},
                                                        'subcategories': [{'id': 'CNT-CSI-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNT-CSI-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNT-COMPTES-BRANCHES',
                                                        'name': {'en': 'Branch accounts',
                                                                 'fr': 'Comptes des '
                                                                       'branches'},
                                                        'subcategories': [{'id': 'CNT-COMPTES-BRANCHES-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNT-COMPTES-BRANCHES-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNT-OPERATIONS',
                                                        'name': {'en': 'Operations on '
                                                                       'goods and '
                                                                       'services',
                                                                 'fr': 'Opérations sur '
                                                                       'biens et '
                                                                       'services'},
                                                        'subcategories': [{'id': 'CNT-OPERATIONS-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNT-OPERATIONS-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNT-PIB',
                                                        'name': {'en': 'Gross domestic '
                                                                       'product balance',
                                                                 'fr': 'Équilibre du '
                                                                       'produit '
                                                                       'intérieur brut'},
                                                        'subcategories': [{'id': 'CNT-PIB-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNT-PIB-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]}]},
                                    {'id': 'CNA',
                                     'name': {'en': 'Annual national accounts',
                                              'fr': 'Comptes nationaux annuels'},
                                     'subcategories': [{'id': 'CNA-PAT',
                                                        'name': {'en': 'Balance sheet '
                                                                       'accounts',
                                                                 'fr': 'Comptes de '
                                                                       'patrimoine'},
                                                        'subcategories': [{'id': 'CNA-PAT-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-PAT-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNA-TOF',
                                                        'name': {'en': 'Financial '
                                                                       'accounts',
                                                                 'fr': 'Comptes '
                                                                       'financiers'},
                                                        'subcategories': [{'id': 'CNA-TOF-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-TOF-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNA-CSI',
                                                        'name': {'en': 'Institutional '
                                                                       'sectors '
                                                                       'accounts',
                                                                 'fr': 'Comptes de '
                                                                       'secteurs '
                                                                       'institutionnels'},
                                                        'subcategories': [{'id': 'CNA-CSI-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-CSI-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNA-EMP',
                                                        'name': {'en': 'Domestic '
                                                                       'employment and '
                                                                       'hours worked',
                                                                 'fr': 'Emploi '
                                                                       'intérieur et '
                                                                       'heures '
                                                                       'travaillées'},
                                                        'subcategories': [{'id': 'CNA-EMP-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-EMP-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNA-TEI',
                                                        'name': {'en': 'Intermediate '
                                                                       'input table '
                                                                       '(IIT)',
                                                                 'fr': 'Tableau des '
                                                                       'entrées '
                                                                       'intermédiaires '
                                                                       '(TEI)'},
                                                        'subcategories': [{'id': 'CNA-TEI-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-TEI-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNA-CPE-FBCF',
                                                        'name': {'en': 'Production and '
                                                                       'operating '
                                                                       'accounts by '
                                                                       'branch, gross '
                                                                       'fixed capital '
                                                                       'formation of '
                                                                       'branches',
                                                                 'fr': 'Compte de '
                                                                       'production, '
                                                                       'compte '
                                                                       "d'exploitation "
                                                                       'et FBCF par '
                                                                       'branche'},
                                                        'subcategories': [{'id': 'CNA-CPE-FBCF-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-CPE-FBCF-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNA-CONSO',
                                                        'name': {'en': 'Detailed '
                                                                       'actual final '
                                                                       'consumption of '
                                                                       'households',
                                                                 'fr': 'Consommation '
                                                                       'effective '
                                                                       'détaillée des '
                                                                       'ménages'},
                                                        'subcategories': [{'id': 'CNA-CONSO-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-CONSO-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNA-ERE',
                                                        'name': {'en': 'Resources-uses '
                                                                       'balance by '
                                                                       'product',
                                                                 'fr': 'Équilibre '
                                                                       'ressources-emplois '
                                                                       'par produit'},
                                                        'subcategories': [{'id': 'CNA-ERE-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-ERE-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNA-RDB',
                                                        'name': {'en': "Households' "
                                                                       'gross '
                                                                       'disposable '
                                                                       'income and '
                                                                       'purchasing '
                                                                       'power',
                                                                 'fr': 'Revenu '
                                                                       'disponible '
                                                                       'brut et '
                                                                       'pouvoir '
                                                                       "d'achat des "
                                                                       'ménages'},
                                                        'subcategories': [{'id': 'CNA-RDB-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-RDB-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'CNA-PIB',
                                                        'name': {'en': 'Gross Domestic '
                                                                       'Product (GDP)',
                                                                 'fr': 'Produit '
                                                                       'intérieur brut '
                                                                       '(PIB)'},
                                                        'subcategories': [{'id': 'CNA-PIB-2005',
                                                                           'name': {'en': 'Base '
                                                                                          '2005',
                                                                                    'fr': 'Base '
                                                                                          '2005'}},
                                                                          {'id': 'CNA-PIB-2010',
                                                                           'name': {'en': 'Base '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]}]}]},
                 {'id': 'ENQ-CONJ',
                  'name': {'en': 'Economic outlook surveys', 'fr': 'Enquêtes de conjoncture'},
                  'subcategories': [{'id': 'ENQ-CONJ-SERVICES',
                                     'name': {'en': 'Services', 'fr': 'Services'}},
                                    {'id': 'ENQ-CONJ-COMMERCE',
                                     'name': {'en': 'Trade', 'fr': 'Commerce'},
                                     'subcategories': [{'id': 'ENQ-CONJ-COMMERCE-DETAIL',
                                                        'name': {'en': 'Retail trade '
                                                                       'and trade and '
                                                                       'repair of '
                                                                       'motor vehicles',
                                                                 'fr': 'Commerce de '
                                                                       'détail et '
                                                                       'commerce et '
                                                                       'réparation '
                                                                       'automobiles'}},
                                                       {'id': 'ENQ-CONJ-COMMERCE-GROS',
                                                        'name': {'en': 'Wholesale trade',
                                                                 'fr': 'Commerce de '
                                                                       'gros'}}]},
                                    {'id': 'ENQ-CONJ-BTP',
                                     'name': {'en': 'Construction and real estate',
                                              'fr': 'Construction et immobilier'},
                                     'subcategories': [{'id': 'ENQ-CONJ-PROMO-IMMO',
                                                        'name': {'en': 'Real estate '
                                                                       'development',
                                                                 'fr': 'Promotion '
                                                                       'immobilière'}},
                                                       {'id': 'ENQ-CONJ-TP',
                                                        'name': {'en': 'Public works',
                                                                 'fr': 'Travaux publics'}},
                                                       {'id': 'ENQ-CONJ-ART-BAT',
                                                        'name': {'en': 'Building trades',
                                                                 'fr': 'Artisanat du '
                                                                       'bâtiment'}},
                                                       {'id': 'ENQ-CONJ-IND-BAT',
                                                        'name': {'en': 'Building '
                                                                       'industry',
                                                                 'fr': 'Industrie du '
                                                                       'bâtiment'}}]},
                                    {'id': 'ENQ-CONJ-INDUSTRIE',
                                     'name': {'en': 'Industry', 'fr': 'Industrie'},
                                     'subcategories': [{'id': 'ENQ-CONJ-TRESORERIE-IND',
                                                        'name': {'en': 'Cash flow',
                                                                 'fr': 'Trésorerie'}},
                                                       {'id': 'ENQ-CONJ-INVESTISSEMENT-IND',
                                                        'name': {'en': 'Investment',
                                                                 'fr': 'Investissement'}},
                                                       {'id': 'ENQ-CONJ-ACTIVITE-IND',
                                                        'name': {'en': 'Activity and '
                                                                       'demand',
                                                                 'fr': 'Activité et '
                                                                       'demande'}}]},
                                    {'id': 'ENQ-CONJ-MENAGES',
                                     'name': {'en': 'Households', 'fr': 'Ménages'}},
                                    {'id': 'ENQ-CONJ-ENS',
                                     'name': {'en': 'Business climate and turning-point',
                                              'fr': 'Climat des affaires et retournement '
                                                    'conjoncturel'}}]},
                 {'id': 'PRIX',
                  'name': {'en': 'Prices and price indices', 'fr': 'Prix et indices de prix'},
                  'subcategories': [{'id': 'MAT-PREM',
                                     'name': {'en': 'Raw materials prices',
                                              'fr': 'Prix et cours des matières premières'}},
                                    {'id': 'PRIX-REV-IMMO',
                                     'name': {'en': 'Price and revision of leases '
                                                    'indices in the real estate sector',
                                              'fr': 'Indices des prix et de révision des '
                                                    'baux dans le secteur immobilier'},
                                     'subcategories': [{'id': 'IND-REVISION-IMMO',
                                                        'name': {'en': 'Indices for '
                                                                       'revision of '
                                                                       'leases '
                                                                       '(contract '
                                                                       'escalation)',
                                                                 'fr': 'Indices de '
                                                                       'révision des '
                                                                       'baux '
                                                                       '(indexation de '
                                                                       'contrats)'}},
                                                       {'id': 'IND-PRIX-IMMO',
                                                        'name': {'en': 'Housing price '
                                                                       'indices',
                                                                 'fr': 'Indices des '
                                                                       'prix des '
                                                                       'logements'}}]},
                                    {'id': 'PRIX-PRODUCTION',
                                     'name': {'en': 'Producer price or cost indices and '
                                                    'import price indices',
                                              'fr': 'Indices de prix ou de coût de '
                                                    'production et indices de prix '
                                                    "d'importation"},
                                     'subcategories': [{'id': 'IPPS',
                                                        'name': {'en': 'Services',
                                                                 'fr': 'Services'},
                                                        'subcategories': [{'id': 'PVS-ANC',
                                                                           'name': {'en': 'Old '
                                                                                          'base '
                                                                                          'years',
                                                                                    'fr': 'Anciennes '
                                                                                          'bases'}},
                                                                          {'id': 'IPPS-BtoE',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          'for '
                                                                                          'foreign '
                                                                                          'markets '
                                                                                          '(BtoE) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          'pour '
                                                                                          'les '
                                                                                          'marchés '
                                                                                          'extérieurs '
                                                                                          '(BtoE) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010'}},
                                                                          {'id': 'IPPS-BtoC',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          'for '
                                                                                          'French '
                                                                                          'market '
                                                                                          '- '
                                                                                          'households '
                                                                                          '(BtoC) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          'pour '
                                                                                          'le '
                                                                                          'marché '
                                                                                          'français '
                                                                                          '- '
                                                                                          'ménages '
                                                                                          '(BtoC) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010'}},
                                                                          {'id': 'IPPS-BtoB-PM',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          'for '
                                                                                          'French '
                                                                                          'market '
                                                                                          '- '
                                                                                          'businesses '
                                                                                          '(BtoB) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '- '
                                                                                          "Purchaser's "
                                                                                          'price '
                                                                                          'for '
                                                                                          'contract '
                                                                                          'escalation',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          'pour '
                                                                                          'le '
                                                                                          'marché '
                                                                                          'français '
                                                                                          '- '
                                                                                          'entreprises '
                                                                                          '(BtoB) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '- '
                                                                                          'Prix '
                                                                                          'de '
                                                                                          'marché '
                                                                                          '(indexation '
                                                                                          'de '
                                                                                          'contrats)'}},
                                                                          {'id': 'IPPS-BtoB-PB',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          'for '
                                                                                          'French '
                                                                                          'market '
                                                                                          '- '
                                                                                          'businesses '
                                                                                          '(BtoB) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '- '
                                                                                          'Basic '
                                                                                          'price',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          'pour '
                                                                                          'le '
                                                                                          'marché '
                                                                                          'français '
                                                                                          '- '
                                                                                          'entreprises '
                                                                                          '(BtoB) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '- '
                                                                                          'Prix '
                                                                                          'de '
                                                                                          'base'}},
                                                                          {'id': 'IPPS-BtoALL',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          'for '
                                                                                          'all '
                                                                                          'markets '
                                                                                          '(BtoAll) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          'pour '
                                                                                          "l'ensemble "
                                                                                          'des '
                                                                                          'marchés '
                                                                                          '(BtoAll) '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'IPPCC',
                                                        'name': {'en': 'Construction',
                                                                 'fr': 'Construction'},
                                                        'subcategories': [{'id': 'IPP-CONS-ANC',
                                                                           'name': {'en': 'Old '
                                                                                          'base '
                                                                                          'years',
                                                                                    'fr': 'Anciennes '
                                                                                          'bases'}},
                                                                          {'id': 'ICPC-2010',
                                                                           'name': {'en': 'Producer '
                                                                                          'costs '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010',
                                                                                    'fr': 'Coûts '
                                                                                          'de '
                                                                                          'production '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010'}},
                                                                          {'id': 'IPPC-2010',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'IPPI',
                                                        'name': {'en': 'Industry',
                                                                 'fr': 'Industrie'},
                                                        'subcategories': [{'id': 'PVI-ANC',
                                                                           'name': {'en': 'Old '
                                                                                          'base '
                                                                                          'years',
                                                                                    'fr': 'Anciennes '
                                                                                          'bases'},
                                                                           'subcategories': [{'id': 'IPPI-2000',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2000',
                                                                                                       'fr': 'Base '
                                                                                                             '2000'}},
                                                                                             {'id': 'IPPI-2005',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2005',
                                                                                                       'fr': 'Base '
                                                                                                             '2005'}}]},
                                                                          {'id': 'IPPI-INT-2010',
                                                                           'name': {'en': 'Total '
                                                                                          'supply '
                                                                                          'of '
                                                                                          'industrial '
                                                                                          'products '
                                                                                          'prices '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '(contract '
                                                                                          'escalation)',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          "l'offre "
                                                                                          'intérieure '
                                                                                          'de '
                                                                                          'produits '
                                                                                          'industriels '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '(indexation '
                                                                                          'de '
                                                                                          'contrats)'}},
                                                                          {'id': 'IPPI-IMP-2010',
                                                                           'name': {'en': 'Import '
                                                                                          'prices '
                                                                                          'of '
                                                                                          'industrial '
                                                                                          'products '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010',
                                                                                    'fr': 'Prix '
                                                                                          "d'importation "
                                                                                          'des '
                                                                                          'produits '
                                                                                          'industriels '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010'}},
                                                                          {'id': 'IPPI-EXT-2010',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          'for '
                                                                                          'foreign '
                                                                                          'markets '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          'pour '
                                                                                          'les '
                                                                                          'marchés '
                                                                                          'extérieurs '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010'}},
                                                                          {'id': 'IPPI-FR-PM-2010',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          'for '
                                                                                          'the '
                                                                                          'French '
                                                                                          'market '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '- '
                                                                                          "Purchaser's "
                                                                                          'price '
                                                                                          'for '
                                                                                          'contract '
                                                                                          'escalation',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          'pour '
                                                                                          'le '
                                                                                          'marché '
                                                                                          'français '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '- '
                                                                                          'Prix '
                                                                                          'de '
                                                                                          'marché '
                                                                                          '(indexation '
                                                                                          'de '
                                                                                          'contrats)'}},
                                                                          {'id': 'IPPI-FR-PB-2010',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          'for '
                                                                                          'the '
                                                                                          'French '
                                                                                          'market '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '- '
                                                                                          'Basic '
                                                                                          'price',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          'pour '
                                                                                          'le '
                                                                                          'marché '
                                                                                          'français '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010 '
                                                                                          '- '
                                                                                          'Prix '
                                                                                          'de '
                                                                                          'base'}},
                                                                          {'id': 'IPPI-ENS-2010',
                                                                           'name': {'en': 'Producer '
                                                                                          'prices '
                                                                                          'for '
                                                                                          'all '
                                                                                          'markets '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'production '
                                                                                          'pour '
                                                                                          "l'ensemble "
                                                                                          'des '
                                                                                          'marchés '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'IPPA',
                                                        'name': {'en': 'Agriculture',
                                                                 'fr': 'Agriculture'},
                                                        'subcategories': [{'id': 'IPP-AGR-ANC',
                                                                           'name': {'en': 'Old '
                                                                                          'base '
                                                                                          'years',
                                                                                    'fr': 'Anciennes '
                                                                                          'bases'},
                                                                           'subcategories': [{'id': 'IPP-AGR-1995',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1995',
                                                                                                       'fr': 'Base '
                                                                                                             '1995'}},
                                                                                             {'id': 'IPP-AGR-2000',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2000',
                                                                                                       'fr': 'Base '
                                                                                                             '2000'}},
                                                                                             {'id': 'IPP-AGR-2005',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2005',
                                                                                                       'fr': 'Base '
                                                                                                             '2005'}}]},
                                                                          {'id': 'IPAMPA',
                                                                           'name': {'en': 'Agricultural '
                                                                                          'means '
                                                                                          'of '
                                                                                          'production '
                                                                                          'purchasing '
                                                                                          'price '
                                                                                          '(IPAMPA)',
                                                                                    'fr': 'Prix '
                                                                                          'des '
                                                                                          'moyens '
                                                                                          'de '
                                                                                          'production '
                                                                                          'agricole '
                                                                                          '(IPAMPA)'}},
                                                                          {'id': 'IPGA',
                                                                           'name': {'en': 'Food '
                                                                                          'wholesale '
                                                                                          'price '
                                                                                          'indices '
                                                                                          '(contract '
                                                                                          'escalation)',
                                                                                    'fr': 'Prix '
                                                                                          'de '
                                                                                          'gros '
                                                                                          'alimentaires '
                                                                                          '(indexation '
                                                                                          'de '
                                                                                          'contrats)'}},
                                                                          {'id': 'IPPAP',
                                                                           'name': {'en': 'Agricultural '
                                                                                          'producer '
                                                                                          'prices '
                                                                                          '(IPPAP)',
                                                                                    'fr': 'Prix '
                                                                                          'agricoles '
                                                                                          'à '
                                                                                          'la '
                                                                                          'production '
                                                                                          '(IPPAP)'}}]}]},
                                    {'id': 'PRIX-CONSO',
                                     'name': {'en': 'Retail prices and consumer price '
                                                    'indices',
                                              'fr': 'Prix et indices de prix à la '
                                                    'consommation'},
                                     'subcategories': [{'id': 'COEFF-TRANSFO',
                                                        'name': {'en': 'Coefficient '
                                                                       'for the '
                                                                       'conversion of '
                                                                       'currency',
                                                                 'fr': 'Coefficient de '
                                                                       'transformation '
                                                                       'de la monnaie'}},
                                                       {'id': 'PRIX-VENTE-DETAIL',
                                                        'name': {'en': 'Average retail '
                                                                       'prices',
                                                                 'fr': 'Prix moyens de '
                                                                       'vente de détail'}},
                                                       {'id': 'IPC',
                                                        'name': {'en': 'Household '
                                                                       'consumer price '
                                                                       'indices',
                                                                 'fr': 'Indices des '
                                                                       'prix à la '
                                                                       'consommation '
                                                                       'des ménages'},
                                                        'subcategories': [{'id': 'IPC-ANC',
                                                                           'name': {'en': 'Old '
                                                                                          'base '
                                                                                          'years',
                                                                                    'fr': 'Anciennes '
                                                                                          'bases'},
                                                                           'subcategories': [{'id': 'IPC-1980',
                                                                                              'name': {'en': 'Base '
                                                                                                             'years '
                                                                                                             '1970 '
                                                                                                             'and '
                                                                                                             '1980',
                                                                                                       'fr': 'Bases '
                                                                                                             '1970 '
                                                                                                             'et '
                                                                                                             '1980'}},
                                                                                             {'id': 'IPC-1990',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1990',
                                                                                                       'fr': 'Base '
                                                                                                             '1990'}}]},
                                                                          {'id': 'IPCH',
                                                                           'name': {'en': 'Harmonised '
                                                                                          'consumer '
                                                                                          'price '
                                                                                          'index',
                                                                                    'fr': 'Indices '
                                                                                          'des '
                                                                                          'prix '
                                                                                          'à '
                                                                                          'la '
                                                                                          'consommation '
                                                                                          'harmonisés'}},
                                                                          {'id': 'IPC-1998',
                                                                           'name': {'en': 'Consumer '
                                                                                          'price '
                                                                                          'indices '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '1998',
                                                                                    'fr': 'Indices '
                                                                                          'des '
                                                                                          'prix '
                                                                                          'à '
                                                                                          'la '
                                                                                          'consommation '
                                                                                          '- '
                                                                                          'Base '
                                                                                          '1998'}}]}]}]},
                 {'id': 'PRODUCTION-ENT',
                  'name': {'en': 'Companies output',
                           'fr': 'Activité productrice des entreprises'},
                  'subcategories': [{'id': 'COMMERCE-SERV',
                                     'name': {'en': 'Trade and services',
                                              'fr': 'Commerce et services'},
                                     'subcategories': [{'id': 'CA-EMAGSA',
                                                        'name': {'en': 'Large food '
                                                                       'stores '
                                                                       'turnover '
                                                                       'indices '
                                                                       '(EMAGSA)',
                                                                 'fr': 'Indices de '
                                                                       'chiffre '
                                                                       "d'affaires des "
                                                                       'grandes '
                                                                       'surfaces '
                                                                       'alimentaires '
                                                                       '(source EMAGSA)'}},
                                                       {'id': 'CA-COM-SER',
                                                        'name': {'en': 'Turnover '
                                                                       'indices (VAT)',
                                                                 'fr': 'Indices de '
                                                                       'chiffre '
                                                                       "d'affaires "
                                                                       '(source TVA)'},
                                                        'subcategories': [{'id': 'ICA-CS-ANC',
                                                                           'name': {'en': 'Old '
                                                                                          'base '
                                                                                          'years',
                                                                                    'fr': 'Anciennes '
                                                                                          'bases'},
                                                                           'subcategories': [{'id': 'ICA-CS-1990',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1990',
                                                                                                       'fr': 'Base '
                                                                                                             '1990'}},
                                                                                             {'id': 'ICA-CS-1995',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1995',
                                                                                                       'fr': 'Base '
                                                                                                             '1995'}},
                                                                                             {'id': 'ICA-CS-2000',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2000',
                                                                                                       'fr': 'Base '
                                                                                                             '2000'}},
                                                                                             {'id': 'ICA-CS-2005',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2005',
                                                                                                       'fr': 'Base '
                                                                                                             '2005'}}]},
                                                                          {'id': 'ICA-CS-2010',
                                                                           'name': {'en': 'Base '
                                                                                          'year '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]}]},
                                    {'id': 'INDUSTRIE-CONST',
                                     'name': {'en': 'Industry and construction',
                                              'fr': 'Industrie et construction'},
                                     'subcategories': [{'id': 'CONSTRUCTION',
                                                        'name': {'en': 'Construction '
                                                                       'of residential '
                                                                       'and '
                                                                       'non-residential '
                                                                       'buildings',
                                                                 'fr': 'Construction '
                                                                       'de logements '
                                                                       'et de locaux'}},
                                                       {'id': 'ICA-IND-CONS',
                                                        'name': {'en': 'Turnover '
                                                                       'indices',
                                                                 'fr': 'Indices de '
                                                                       'chiffre '
                                                                       "d'affaires"},
                                                        'subcategories': [{'id': 'ICA-IC-ANC',
                                                                           'name': {'en': 'Old '
                                                                                          'base '
                                                                                          'years',
                                                                                    'fr': 'Anciennes '
                                                                                          'bases'},
                                                                           'subcategories': [{'id': 'ICA-IC-1990',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1990',
                                                                                                       'fr': 'Base '
                                                                                                             '1990'}},
                                                                                             {'id': 'ICA-IC-1995',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1995',
                                                                                                       'fr': 'Base '
                                                                                                             '1995'}},
                                                                                             {'id': 'ICA-IC-2000',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2000',
                                                                                                       'fr': 'Base '
                                                                                                             '2000'}},
                                                                                             {'id': 'ICA-IC-2005',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2005',
                                                                                                       'fr': 'Base '
                                                                                                             '2005'}}]},
                                                                          {'id': 'ICA-IC-2010',
                                                                           'name': {'en': 'Base '
                                                                                          'year '
                                                                                          '2010',
                                                                                    'fr': 'Base '
                                                                                          '2010'}}]},
                                                       {'id': 'PRODUCTION-IND',
                                                        'name': {'en': 'Industrial '
                                                                       'output',
                                                                 'fr': 'Production '
                                                                       'industrielle'},
                                                        'subcategories': [{'id': 'IPI-ANC',
                                                                           'name': {'en': 'Old '
                                                                                          'base '
                                                                                          'years',
                                                                                    'fr': 'Anciennes '
                                                                                          'bases'},
                                                                           'subcategories': [{'id': 'IPI-1970',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1970',
                                                                                                       'fr': 'Base '
                                                                                                             '1970'}},
                                                                                             {'id': 'IPI-1985',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1985',
                                                                                                       'fr': 'Base '
                                                                                                             '1985'}},
                                                                                             {'id': 'IPI-1990',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1990',
                                                                                                       'fr': 'Base '
                                                                                                             '1990'}},
                                                                                             {'id': 'IPI-1995',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '1995',
                                                                                                       'fr': 'Base '
                                                                                                             '1995'}},
                                                                                             {'id': 'IPI-2000',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2000',
                                                                                                       'fr': 'Base '
                                                                                                             '2000'}},
                                                                                             {'id': 'IPI-2005',
                                                                                              'name': {'en': 'Base '
                                                                                                             'year '
                                                                                                             '2005',
                                                                                                       'fr': 'Base '
                                                                                                             '2005'}}]},
                                                                          {'id': 'EBPI-2010',
                                                                           'name': {'en': 'Branch '
                                                                                          'survey '
                                                                                          'of '
                                                                                          'industrial '
                                                                                          'production '
                                                                                          '(base '
                                                                                          '2010)',
                                                                                    'fr': 'Enquête '
                                                                                          'de '
                                                                                          'branche '
                                                                                          'de '
                                                                                          'la '
                                                                                          'production '
                                                                                          'industrielle '
                                                                                          '(base '
                                                                                          '2010)'}},
                                                                          {'id': 'IPI-2010',
                                                                           'name': {'en': 'Industrial '
                                                                                          'production '
                                                                                          'index '
                                                                                          '(base '
                                                                                          '2010)',
                                                                                    'fr': 'Indice '
                                                                                          'de '
                                                                                          'la '
                                                                                          'production '
                                                                                          'industrielle '
                                                                                          '(base '
                                                                                          '2010)'}}]}]}]},
                 {'id': 'DEMO-ENT',
                  'name': {'en': 'Business demography', 'fr': 'Démographie des entreprises'},
                  'subcategories': [{'id': 'DEMO-ENT-ANC',
                                     'name': {'en': 'Stopped series',
                                              'fr': 'Anciennes séries'},
                                     'subcategories': [{'id': 'CESSATIONS-ENT',
                                                        'name': {'en': 'Company '
                                                                       'closure indices',
                                                                 'fr': 'Cessations '
                                                                       "d'activité des "
                                                                       'entreprises'}},
                                                       {'id': 'DEFAILLANCES-ENT-ANC',
                                                        'name': {'en': 'Business '
                                                                       'failures',
                                                                 'fr': 'Défaillances '
                                                                       "d'entreprises"}},
                                                       {'id': 'CREATIONS-ENT-ANC',
                                                        'name': {'en': 'Enterprises '
                                                                       'births',
                                                                 'fr': 'Créations '
                                                                       "d'entreprises"}}]},
                                    {'id': 'DEFAILLANCES-ENT',
                                     'name': {'en': 'Business failures',
                                              'fr': "Défaillances d'entreprises"}},
                                    {'id': 'CREATIONS-ENT',
                                     'name': {'en': 'Enterprises births',
                                              'fr': "Créations d'entreprises"}}]},
                 {'id': 'POPULATION',
                  'name': {'en': 'Demography', 'fr': 'Population'},
                  'subcategories': [{'id': 'ETRANGERS-IMMIGRES',
                                     'name': {'en': 'Foreigners - Immigrants',
                                              'fr': 'Étrangers - Immigrés'}},
                                    {'id': 'COUPLES-FAM-MEN',
                                     'name': {'en': 'Couples - Families - Households',
                                              'fr': 'Couples - Familles - Ménages'}},
                                    {'id': 'ETAT-CIVIL',
                                     'name': {'en': 'Registry office and demographic '
                                                    'trends',
                                              'fr': 'État civil et mouvements '
                                                    'démographiques'},
                                     'subcategories': [{'id': 'DEMO-DEP-REG',
                                                        'name': {'en': 'Departmental '
                                                                       'and regional '
                                                                       'data',
                                                                 'fr': 'Données '
                                                                       'départementales '
                                                                       'et régionales'}},
                                                       {'id': 'DEMO-NAT',
                                                        'name': {'en': 'National data',
                                                                 'fr': 'Données '
                                                                       'nationales'}}]},
                                    {'id': 'POP-RP',
                                     'name': {'en': 'Census population',
                                              'fr': 'Population aux recensements'}}]},
                 {'id': 'MARCHE-TRAVAIL',
                  'name': {'en': 'Labour market', 'fr': 'Marché du travail'},
                  'subcategories': [{'id': 'CHOMAGE',
                                     'name': {'en': 'Unemployment', 'fr': 'Chômage'},
                                     'subcategories': [{'id': 'OFFRES-EMP',
                                                        'name': {'en': 'Job offers '
                                                                       'collected at '
                                                                       'Pôle Emploi',
                                                                 'fr': 'Offres '
                                                                       "d'emploi "
                                                                       'collectées à '
                                                                       'Pôle emploi'}},
                                                       {'id': 'DEMANDES-EMP',
                                                        'name': {'en': 'Job seekers '
                                                                       'registered at '
                                                                       'Pôle emploi',
                                                                 'fr': 'Demandeurs '
                                                                       "d'emploi "
                                                                       'inscrits à '
                                                                       'Pôle emploi'}},
                                                       {'id': 'CHOMAGE-TRIM',
                                                        'name': {'en': 'Quarterly '
                                                                       'unemployment',
                                                                 'fr': 'Chômage '
                                                                       'trimestriel'}},
                                                       {'id': 'CHOMAGE-MOY-AN',
                                                        'name': {'en': 'Annual average '
                                                                       'unemployment',
                                                                 'fr': 'Chômage en '
                                                                       'moyenne '
                                                                       'annuelle'}}]},
                                    {'id': 'EMPLOI-POP-ACT',
                                     'name': {'en': 'Employment - Labour force',
                                              'fr': 'Emploi - Population active'},
                                     'subcategories': [{'id': 'EMP-TRIM',
                                                        'name': {'en': 'Quarterly '
                                                                       'employment',
                                                                 'fr': 'Emploi '
                                                                       'trimestriel'}},
                                                       {'id': 'EMP-MOY-AN',
                                                        'name': {'en': 'Annual average '
                                                                       'employment',
                                                                 'fr': 'Emploi en '
                                                                       'moyenne '
                                                                       'annuelle'}},
                                                       {'id': 'EMP-SAL',
                                                        'name': {'en': 'Quarterly '
                                                                       'payroll '
                                                                       'employment by '
                                                                       'sector',
                                                                 'fr': 'Emploi salarié '
                                                                       'trimestriel '
                                                                       'par secteur'}},
                                                       {'id': 'EMP-TOT',
                                                        'name': {'en': 'Total '
                                                                       'employment on '
                                                                       'December 31',
                                                                 'fr': 'Emploi total '
                                                                       'au 31 décembre'}}]}]},
                 {'id': 'SALAIRES-REVENUS',
                  'name': {'en': 'Wages, labour cost, living standard',
                           'fr': 'Salaires, coût du travail, niveau de vie'},
                  'subcategories': [{'id': 'NIVEAU-VIE-PAUVRETE',
                                     'name': {'en': 'Living standard - Poverty',
                                              'fr': 'Niveau de vie - Pauvreté'}},
                                    {'id': 'COUT-TRAVAIL',
                                     'name': {'en': 'Labour cost', 'fr': 'Coût du travail'},
                                     'subcategories': [{'id': 'COUT-TRAVAIL-ICT',
                                                        'name': {'en': 'Labour cost '
                                                                       'index in '
                                                                       'industry, '
                                                                       'construction '
                                                                       'and services',
                                                                 'fr': 'Indice du coût '
                                                                       'du travail '
                                                                       'dans '
                                                                       "l'industrie, "
                                                                       'la '
                                                                       'construction '
                                                                       'et le tertiaire'}},
                                                       {'id': 'COUT-HORAIRE-TRAVAIL',
                                                        'name': {'en': 'Hourly labour '
                                                                       'cost index',
                                                                 'fr': 'Indice du coût '
                                                                       'horaire du '
                                                                       'travail'}}]},
                                    {'id': 'SALAIRES',
                                     'name': {'en': 'Wages', 'fr': 'Salaires'},
                                     'subcategories': [{'id': 'SAL-MIN-FP-COTIS',
                                                        'name': {'en': 'Minimum wages '
                                                                       '- Social '
                                                                       'contributions '
                                                                       '- Indices '
                                                                       'Civil service',
                                                                 'fr': 'SMIC - Taux de '
                                                                       'cotisations '
                                                                       'sociales - '
                                                                       'Indices '
                                                                       'Fonction '
                                                                       'publique'}},
                                                       {'id': 'INDICES-SAL-ACEMO',
                                                        'name': {'en': 'Quarterly wage '
                                                                       'indices in the '
                                                                       'private sector',
                                                                 'fr': 'Indices '
                                                                       'trimestriels '
                                                                       'de salaire '
                                                                       'dans le '
                                                                       'secteur privé'}},
                                                       {'id': 'SAL-ANNUELS',
                                                        'name': {'en': 'Annual wages',
                                                                 'fr': 'Salaires '
                                                                       'annuels'}}]}]},
                 {'id': 'ECHANGES-EXT',
                  'name': {'en': 'Foreign trade', 'fr': 'Échanges extérieurs'},
                  'subcategories': [{'id': 'ICE',
                                     'name': {'en': 'Foreign trade indices',
                                              'fr': 'Indices du commerce extérieur'},
                                     'subcategories': [{'id': 'ICE-ANC',
                                                        'name': {'en': 'Old base years',
                                                                 'fr': 'Anciennes bases'},
                                                        'subcategories': [{'id': 'ICE-1980',
                                                                           'name': {'en': 'Base '
                                                                                          'year '
                                                                                          '1980',
                                                                                    'fr': 'Base '
                                                                                          '1980'}},
                                                                          {'id': 'ICE-1995',
                                                                           'name': {'en': 'Base '
                                                                                          'year '
                                                                                          '1995 '
                                                                                          '(CPA '
                                                                                          '1993)',
                                                                                    'fr': 'Base '
                                                                                          '1995 '
                                                                                          '(CPF '
                                                                                          'rév.1)'}}]},
                                                       {'id': 'ICE-2005',
                                                        'name': {'en': 'Base year 2005',
                                                                 'fr': 'Base 2005'}}]},
                                    {'id': 'BALANCE-PAIEMENTS',
                                     'name': {'en': 'Balance of payments',
                                              'fr': 'Balance des paiements'}},
                                    {'id': 'COM-EXT-VA',
                                     'name': {'en': 'Foreign trade in value',
                                              'fr': 'Commerce extérieur en valeur'}}]},
                 {'id': 'CONDITIONS-VIE-SOCIETE',
                  'name': {'en': 'Living standards - Society',
                           'fr': 'Conditions de vie - Société'},
                  'subcategories': [{'id': 'LOGEMENT',
                                     'name': {'en': 'Housing', 'fr': 'Logement'}},
                                    {'id': 'VACANCES-LOISIRS-CULTURE',
                                     'name': {'en': 'Holidays - Leisure - Culture',
                                              'fr': 'Vacances - Loisirs - Culture'}}]},
                 {'id': 'SERVICES-TOURISME-TRANSPORT',
                  'name': {'en': 'Services - Tourism - Transportation',
                           'fr': 'Services - Tourisme - Transport'},
                  'subcategories': [{'id': 'TRANSPORTS',
                                     'name': {'en': 'Transports', 'fr': 'Transports'}},
                                    {'id': 'TOURISME',
                                     'name': {'en': 'Tourism', 'fr': 'Tourisme'}}]}]
        result = sdmx_client.categories
        self.assertEqual(result,model)


    @httpretty.activate
    def test_dataflows(self):
        dataflows_fp = os.path.abspath(os.path.join(RESOURCES_XML_2_1, 
                                                    "nama_gdp_c.xml"))

        body = None
        with open(dataflows_fp) as fp:
            body = fp.read()

        httpretty.register_uri(httpretty.GET, 
                               "http://ec.europa.eu/eurostat/SDMX/diss-web/rest/dataflow/ESTAT/nama_gdp_c",
                               body=body,
                               status=200,
                               content_type="application/xml"
                               )

        sdmx_client = Repository(sdmx_url='http://ec.europa.eu/eurostat/SDMX/diss-web/rest', 
                                 format="xml", 
                                 version="2_1",
                                 agencyID='ESTAT',
                                 namespace_style='short'
                                )

        result = sdmx_client.dataflows("nama_gdp_c")
        model = {'nama_gdp_c':
                 ('ESTAT', '1.0',
                  {'en': 'GDP and main components - Current prices',
                   'fr': 'PIB et principales composantes - Prix courants',
                   'de': 'BIP und Hauptkomponenten - Jeweilige Preise'})}

        self.assertEqual(result,model)

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

    @httpretty.activate
    def test_raw_data(self):
        #https://raw.githubusercontent.com/sdmx-twg/sdmx-ml-v2_1/master/samples/exr/ecb_exr_ng/generic/ecb_exr_ng_ts.xml
        data_fp = os.path.abspath(os.path.join(RESOURCES_XML_2_1, 
                                                   "ecb_exr_ng_ts.xml"))

        body = None
        with open(data_fp) as fp:
            body = fp.read()

        httpretty.register_uri(httpretty.GET, 
                               "https://sdw-wsrest.ecb.europa.eu/service/data/exr/....",
                               body=body,
                               status=200,
                               content_type="application/xml"
                               )

        sdmx_client = Repository(sdmx_url="https://sdw-wsrest.ecb.europa.eu/service", 
                                 format="xml", 
                                 version="2_1",
                                 agencyID='ECB',
                                 namespace_style='short'
                                )

        model = ({'M.CHF.EUR.SP00.E': ['1.3413', '1.3089', '1.3452'],
                  'M.GBP.EUR.SP00.E': ['0.82363', '0.83987', '0.87637'],
                  'M.JPY.EUR.SP00.E': ['110.04', '110.26', '113.67'],
                  'M.USD.EUR.SP00.E': ['1.2894', '1.3067', '1.3898']},
                 {'M.CHF.EUR.SP00.E': ['2010-08', '2010-09', '2010-10'],
                  'M.GBP.EUR.SP00.E': ['2010-08', '2010-09', '2010-10'],
                  'M.JPY.EUR.SP00.E': ['2010-08', '2010-09', '2010-10'],
                  'M.USD.EUR.SP00.E': ['2010-08', '2010-09', '2010-10']},
                 {'M.CHF.EUR.SP00.E': {'CONF_STATUS_OBS': ['F', 'F', 'F'],
                                       'OBS_STATUS': ['A', 'A', 'A']},
                  'M.GBP.EUR.SP00.E': {'CONF_STATUS_OBS': ['F', 'F', 'F'],
                                       'OBS_STATUS': ['A', 'A', 'A']},
                  'M.JPY.EUR.SP00.E': {'CONF_STATUS_OBS': ['F', 'F', 'F'],
                                       'OBS_STATUS': ['A', 'A', 'A']},
                  'M.USD.EUR.SP00.E': {'CONF_STATUS_OBS': ['F', 'F', 'F'],
                                       'OBS_STATUS': ['A', 'A', 'A']}},
                 {'M.CHF.EUR.SP00.E': {'FREQ': 'M',
                                       'CURRENCY': 'CHF',
                                       'CURRENCY_DENOM': 'EUR',
                                       'EXR_TYPE': 'SP00',
                                       'EXR_VAR': 'E'},
                  'M.GBP.EUR.SP00.E': {'FREQ': 'M',
                                       'CURRENCY': 'GBP',
                                       'CURRENCY_DENOM': 'EUR',
                                       'EXR_TYPE': 'SP00',
                                       'EXR_VAR': 'E'},
                  'M.JPY.EUR.SP00.E': {'FREQ': 'M',
                                       'CURRENCY': 'JPY',
                                       'CURRENCY_DENOM': 'EUR',
                                       'EXR_TYPE': 'SP00',
                                       'EXR_VAR': 'E'},
                  'M.USD.EUR.SP00.E': {'FREQ': 'M',
                                       'CURRENCY': 'USD',
                                       'CURRENCY_DENOM': 'EUR',
                                       'EXR_TYPE': 'SP00',
                                       'EXR_VAR': 'E'}})

        result = sdmx_client.raw_data("exr",'....')

        self.assertEqual(result,model)

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
