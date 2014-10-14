import unittest
import sdmx

class EcbTest(unittest.TestCase):
    def test_codes(self):
        model = {'COLLECTION': {'A': 'Average of observations through period',
                                'B': 'Beginning of period',
                                'E': 'End of period',
                                'H': 'Highest in period',
                                'L': 'Lowest in period',
                                'M': 'Middle of period',
                                'S': 'Summed through period',
                                'U': 'Unknown',
                                'V': 'Other',
                                'Y': 'Annualised summed'},
                 'CURRENCY': {'ADF': 'Andorran Franc (1-1 peg to the French franc)',
                              'ADP': 'Andorran Peseta (1-1 peg to the Spanish peseta)',
                              'AED': 'United Arab Emirates dirham',
                              'AFA': 'Afghanistan afghani (old)',
                              'AFN': 'Afghanistan, Afghanis',
                              'ALL': 'Albanian lek',
                              'AMD': 'Armenian dram',
                              'ANG': 'Netherlands Antillean guilder',
                              'AOA': 'Angola, Kwanza',
                              'AON': 'Angolan kwanza (old)',
                              'AOR': 'Angolan kwanza readjustado',
                              'ARS': 'Argentine peso',
                              'ATS': 'Austrian schilling',
                              'AUD': 'Australian dollar',
                              'AWG': 'Aruban florin/guilder',
                              'AZM': 'Azerbaijanian manat (old)',
                              'AZN': 'Azerbaijan, manats',
                              'BAM': 'Bosnia-Hezergovinian convertible mark',
                              'BBD': 'Barbados dollar',
                              'BDT': 'Bangladesh taka',
                              'BEF': 'Belgian franc',
                              'BEL': 'Belgian franc (financial)',
                              'BGL': 'Bulgarian lev (old)',
                              'BGN': 'Bulgarian lev',
                              'BHD': 'Bahraini dinar',
                              'BIF': 'Burundi franc',
                              'BMD': 'Bermudian dollar',
                              'BND': 'Brunei dollar',
                              'BOB': 'Bolivian boliviano',
                              'BRE': 'Brasilian cruzeiro (old)',
                              'BRL': 'Brazilian real',
                              'BSD': 'Bahamas dollar',
                              'BTN': 'Bhutan ngultrum',
                              'BWP': 'Botswana pula',
                              'BYB': 'Belarussian rouble (old)',
                              'BYR': 'Belarus, Rubles',
                              'BZD': 'Belize dollar',
                              'C36': 'European Commission IC-36 group of currencies '
                                     '(European Union 27 Member States, i.e. BE, DE, EE, '
                                     'GR, ES, FR, IE, IT, CY, LU, NL, MT, AT, PT, SI, SK, '
                                     'FI, BG, CZ, DK, LV, LT, HU, PL, RO, SE, GB, and US, '
                                     'AU, CA, JP, MX, NZ, NO, CH, TR)',
                              'CAD': 'Canadian dollar',
                              'CDF': 'Congo franc (ex Zaire)',
                              'CHE': 'WIR Euro',
                              'CHF': 'Swiss franc',
                              'CHW': 'WIR Franc',
                              'CLF': 'Chile Unidades de fomento',
                              'CLP': 'Chilean peso',
                              'CNH': 'Chinese yuan offshore',
                              'CNY': 'Chinese yuan renminbi',
                              'COP': 'Colombian peso',
                              'COU': 'Unidad de Valor Real',
                              'CRC': 'Costa Rican colon',
                              'CSD': 'Serbian dinar',
                              'CUC': 'Cuban convertible peso',
                              'CUP': 'Cuban peso',
                              'CVE': 'Cape Verde escudo',
                              'CYP': 'Cyprus pound',
                              'CZK': 'Czech koruna',
                              'DEM': 'German mark',
                              'DJF': 'Djibouti franc',
                              'DKK': 'Danish krone',
                              'DOP': 'Dominican peso',
                              'DZD': 'Algerian dinar',
                              'E0': 'Euro area changing composition vis-a-vis the EER-12 '
                                    'group of trading partners (AU, CA, DK, HK, JP, NO, SG, '
                                    'KR, SE, CH, GB and US)',
                              'E1': 'Euro area-18 countries vis-a-vis the EER-20 group of '
                                    'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                    'CH, GB, US, BG, CZ, LT, HU, PL, RO, HR and CN)',
                              'E2': 'Euro area-18 countries vis-a-vis the EER-19 group of '
                                    'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                    'CH, GB, US, BG, CZ, LT, HU, PL, RO, and CN)',
                              'E3': 'Euro area-18 countries vis-a-vis the EER-39 group of '
                                    'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                    'CH, GB, US, BG, CZ, LT, HU, PL, RO, CN, DZ, AR, BR, '
                                    'CL, HR, IS, IN, ID, IL, MY, MX, MA, NZ, PH, RU, ZA, '
                                    'TW, TH, TR and VE)',
                              'E4': 'Euro area-18 countries vis-a-vis the EER-12 group of '
                                    'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                    'CH, GB and US)',
                              'E5': 'Euro area-19 countries vis-a-vis the EER-19 group of '
                                    'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                    'CH, GB, US, BG, CZ, HU, PL, RO, HR and CN)',
                              'E6': 'Euro area-19 countries vis-a-vis the EER-18 group of '
                                    'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                    'CH, GB, US, BG, CZ, HU, PL, RO, and CN)',
                              'E7': 'Euro area-19 countries vis-a-vis the EER-38 group of '
                                    'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                    'CH, GB, US, BG, CZ, HU, PL, RO, CN, DZ, AR, BR, CL, '
                                    'HR, IS, IN, ID, IL, MY, MX, MA, NZ, PH, RU, ZA, TW, '
                                    'TH, TR and VE)',
                              'E8': 'Euro area-19 countries vis-a-vis the EER-12 group of '
                                    'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                    'CH, GB and US)',
                              'ECS': 'Ecuador sucre',
                              'EEK': 'Estonian kroon',
                              'EGP': 'Egyptian pound',
                              'ERN': 'Erytrean nafka',
                              'ESP': 'Spanish peseta',
                              'ETB': 'Ethiopian birr',
                              'EUR': 'Euro',
                              'FIM': 'Finnish markka',
                              'FJD': 'Fiji dollar',
                              'FKP': 'Falkland Islands pound',
                              'FRF': 'French franc',
                              'GBP': 'UK pound sterling',
                              'GEL': 'Georgian lari',
                              'GGP': 'Guernsey, Pounds',
                              'GHC': 'Ghana Cedi (old)',
                              'GHS': 'Ghana Cedi',
                              'GIP': 'Gibraltar pound',
                              'GMD': 'Gambian dalasi',
                              'GNF': 'Guinea franc',
                              'GRD': 'Greek drachma',
                              'GTQ': 'Guatemalan quetzal',
                              'GWP': 'Guinea-Bissau peso (old)',
                              'GYD': 'Guyanan dollar',
                              'H1': 'Euro area 18 currencies (FR, BE, LU, NL, DE, IT, IE, '
                                    'PT, ES, FI, AT, GR, SI, CY, EE, LV, MT, SK)',
                              'H10': 'ECB EER-38 group of currencies and Euro area (latest '
                                     'composition) currencies '
                                     '(FR,BE,LU,NL,DE,IT,IE,PT,ES,FI,AT,GR,SI,AU,CA,CN,DK,HK,JP,NO,SG,KR,SE,CH,GB,US,CY,CZ,EE,HU,LV,LT,MT,PL,SK,BG,RO,NZ,DZ,AR,BR,HR,IN,ID,IL,MY,MX,MA,PH,RU,ZA,TW,TH,TR,IS,CL,VE)',
                              'H11': 'ECB EER-19 group of currencies and Euro area (latest '
                                     'composition) currencies (FR, BE, LU, NL, DE, IT, IE, '
                                     'PT, ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, '
                                     'SG, KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, '
                                     'PL, SK, BG, RO, HR)',
                              'H2': 'ECB EER-12 group of currencies and Euro area (latest '
                                    'composition) currencies (FR, BE, LU, NL, DE, IT, IE, '
                                    'PT, ES, FI, AT, GR, SI, CY, EE, LV, MT, SK, AU, CA, '
                                    'CN, DK, HK, JP, NO, SG, KR, SE, CH, GB, US)',
                              'H3': 'ECB EER-19 group of currencies and Euro area (latest '
                                    'composition) currencies (FR, BE, LU, NL, DE, IT, IE, '
                                    'PT, ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, '
                                    'SG, KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, '
                                    'PL, SK, BG, RO)',
                              'H36': 'European Commission IC-36 group of currencies '
                                     '(European Union 27 Member States, i.e. BE, DE, EE, '
                                     'GR, ES, FR, IE, IT, CY, LU, NL, MT, AT, PT, SI, SK, '
                                     'FI, BG, CZ, DK, LV, LT, HU, PL, RO, SE, GB, and US, '
                                     'AU, CA, JP, MX, NZ, NO, CH, TR)',
                              'H37': 'European Commission IC-37 group of currencies '
                                     '(European Union 28 Member States, i.e. BE, DE, EE, '
                                     'GR, ES, FR, IE, IT, CY, LU, NL, MT, AT, PT, SI, SK, '
                                     'FI, BG, CZ, DK, HR, LV, LT, HU, PL, RO, SE, GB, and '
                                     'US, AU, CA, JP, MX, NZ, NO, CH, TR)',
                              'H4': 'ECB EER-39 group of currencies and Euro area (latest '
                                    'composition) currencies '
                                    '(FR,BE,LU,NL,DE,IT,IE,PT,ES,FI,AT,GR,SI,AU,CA,CN,DK,HK,JP,NO,SG,KR,SE,CH,GB,US,CY,CZ,EE,HU,LV,LT,MT,PL,SK,BG,RO,NZ,DZ,AR,BR,HR,IN,ID,IL,MY,MX,MA,PH,RU,ZA,TW,TH,TR,IS,CL,VE)',
                              'H42': 'European Commission IC-42 group of currencies '
                                     '(European Union 28 Member States, i.e. '
                                     'BE,DE,EE,GR,ES,FR,IE,IT,CY,LU,NL,MT,AT,PT,SI,SK,FI,BG,CZ,DK,HR,LV,LT,HU,PL,RO,SE,GB, '
                                     'and US,AU,CA,JP,MX,NZ,NO,CH,TR,KR,CN,HK,RU,BR)',
                              'H5': 'ECB EER-20 group of currencies and Euro area (latest '
                                    'composition) currencies (FR, BE, LU, NL, DE, IT, IE, '
                                    'PT, ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, '
                                    'SG, KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, '
                                    'PL, SK, BG, RO, HR)',
                              'H6': 'ECB EER-12 group of currencies and Euro area (latest '
                                    'composition) currencies (FR, BE, LU, NL, DE, IT, IE, '
                                    'PT, ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, '
                                    'SG, KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, '
                                    'PL, SK, BG, RO, HR, TR and RU)',
                              'H7': 'Euro area 19 currencies (FR, BE, LU, NL, DE, IT, IE, '
                                    'PT, ES, FI, AT, GR, SI, CY, EE, LT, LV, MT, SK)',
                              'H8': 'ECB EER-12 group of currencies and Euro area (latest '
                                    'composition) currencies (FR, BE, LU, NL, DE, IT, IE, '
                                    'PT, ES, FI, AT, GR, SI, CY, EE, LT, LV, MT, SK, AU, '
                                    'CA, CN, DK, HK, JP, NO, SG, KR, SE, CH, GB, US)',
                              'H9': 'ECB EER-18 group of currencies and Euro area (latest '
                                    'composition) currencies (FR, BE, LU, NL, DE, IT, IE, '
                                    'PT, ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, '
                                    'SG, KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, '
                                    'PL, SK, BG, RO)',
                              'HKD': 'Hong Kong dollar',
                              'HKQ': 'Hong Kong dollar (old)',
                              'HNL': 'Honduran lempira',
                              'HRK': 'Croatian kuna',
                              'HTG': 'Haitian gourde',
                              'HUF': 'Hungarian forint',
                              'IDR': 'Indonesian rupiah',
                              'IEP': 'Irish pound',
                              'ILS': 'Israeli shekel',
                              'IMP': 'Isle of Man, Pounds',
                              'INR': 'Indian rupee',
                              'IQD': 'Iraqi dinar',
                              'IRR': 'Iranian rial',
                              'ISK': 'Iceland krona',
                              'ITL': 'Italian lira',
                              'JEP': 'Jersey, Pounds',
                              'JMD': 'Jamaican dollar',
                              'JOD': 'Jordanian dinar',
                              'JPY': 'Japanese yen',
                              'KES': 'Kenyan shilling',
                              'KGS': 'Kyrgyzstan som',
                              'KHR': 'Kampuchean real (Cambodian)',
                              'KMF': 'Comoros franc',
                              'KPW': 'Korean won (North)',
                              'KRW': 'Korean won (Republic)',
                              'KWD': 'Kuwait dinar',
                              'KYD': 'Cayman Islands dollar',
                              'KZT': 'Kazakstan tenge',
                              'LAK': 'Lao kip',
                              'LBP': 'Lebanese pound',
                              'LKR': 'Sri Lanka rupee',
                              'LRD': 'Liberian dollar',
                              'LSL': 'Lesotho loti',
                              'LTL': 'Lithuanian litas',
                              'LUF': 'Luxembourg franc',
                              'LVL': 'Latvian lats',
                              'LYD': 'Libyan dinar',
                              'MAD': 'Moroccan dirham',
                              'MDL': 'Moldovian leu',
                              'MGA': 'Madagascar, Ariary',
                              'MGF': 'Malagasy franc',
                              'MKD': 'Macedonian denar',
                              'MMK': 'Myanmar kyat',
                              'MNT': 'Mongolian tugrik',
                              'MOP': 'Macau pataca',
                              'MRO': 'Mauritanian ouguiya',
                              'MTL': 'Maltese lira',
                              'MUR': 'Mauritius rupee',
                              'MVR': 'Maldive rufiyaa',
                              'MWK': 'Malawi kwacha',
                              'MXN': 'Mexican peso',
                              'MXP': 'Mexican peso (old)',
                              'MXV': 'Mexican Unidad de Inversion (UDI)',
                              'MYR': 'Malaysian ringgit',
                              'MZM': 'Mozambique metical (old)',
                              'MZN': 'Mozambique, Meticais',
                              'NAD': 'Namibian dollar',
                              'NGN': 'Nigerian naira',
                              'NIO': 'Nicaraguan cordoba',
                              'NLG': 'Netherlands guilder',
                              'NOK': 'Norwegian krone',
                              'NPR': 'Nepaleese rupee',
                              'NZD': 'New Zealand dollar',
                              'OMR': 'Oman Sul rial',
                              'PAB': 'Panama balboa',
                              'PEN': 'Peru nuevo sol',
                              'PGK': 'Papua New Guinea kina',
                              'PHP': 'Philippine peso',
                              'PKR': 'Pakistan rupee',
                              'PLN': 'Polish zloty',
                              'PLZ': 'Polish zloty (old)',
                              'PTE': 'Portugese escudo',
                              'PYG': 'Paraguay guarani',
                              'QAR': 'Qatari rial',
                              'ROL': 'Romanian leu (old)',
                              'RON': 'Romanian leu',
                              'RSD': 'Serbian dinar',
                              'RUB': 'Rouble',
                              'RUR': 'Russian ruble (old)',
                              'RWF': 'Rwanda franc',
                              'SAR': 'Saudi riyal',
                              'SBD': 'Solomon Islands dollar',
                              'SCR': 'Seychelles rupee',
                              'SDD': 'Sudanese dinar',
                              'SDG': 'Sudan, Dinars',
                              'SDP': 'Sudanese pound (old)',
                              'SEK': 'Swedish krona',
                              'SGD': 'Singapore dollar',
                              'SHP': 'St. Helena pound',
                              'SIT': 'Slovenian tolar',
                              'SKK': 'Slovak koruna',
                              'SLL': 'Sierra Leone leone',
                              'SOS': 'Somali shilling',
                              'SPL': 'Seborga, Luigini',
                              'SRD': 'Suriname, Dollars',
                              'SRG': 'Suriname guilder',
                              'SSP': 'South sudanese pound',
                              'STD': 'Sao Tome and Principe dobra',
                              'SVC': 'El Salvador colon',
                              'SYP': 'Syrian pound',
                              'SZL': 'Swaziland lilangeni',
                              'THB': 'Thai bhat',
                              'TJR': 'Tajikistan rouble',
                              'TJS': 'Tajikistan, Somoni',
                              'TMM': 'Turkmenistan manat (old)',
                              'TMT': 'Turkmenistan manat',
                              'TND': 'Tunisian dinar',
                              'TOP': 'Tongan paanga',
                              'TPE': 'East Timor escudo',
                              'TRL': 'Turkish lira (old)',
                              'TRY': 'Turkish lira',
                              'TTD': 'Trinidad and Tobago dollar',
                              'TVD': 'Tuvalu, Tuvalu Dollars',
                              'TWD': 'New Taiwan dollar',
                              'TZS': 'Tanzania shilling',
                              'U1': 'Euro and domestic currency',
                              'UAH': 'Ukraine hryvnia',
                              'UGX': 'Uganda Shilling',
                              'USD': 'US dollar',
                              'UYI': 'Uruguay Peso en Unidades Indexadas',
                              'UYU': 'Uruguayan peso',
                              'UZS': 'Uzbekistan sum',
                              'VEB': 'Venezuela bolivar (old)',
                              'VEF': 'Venezuela bolivar',
                              'VND': 'Vietnamese dong',
                              'VUV': 'Vanuatu vatu',
                              'WST': 'Samoan tala',
                              'X1': 'All currencies except national currency',
                              'X2': 'All currencies except USD',
                              'X3': 'All currencies except EUR',
                              'X4': 'All currencies except EUR, USD',
                              'X5': 'All currencies except EUR, JPY, USD',
                              'X6': 'All currencies except EUR, CHF, GBP, JPY, USD',
                              'X7': 'All currencies except EUR, USD, JPY, GBP, CHF, '
                                    'domestic currency',
                              'XAF': 'CFA franc / BEAC',
                              'XAG': 'Silver',
                              'XAU': 'Gold in units of grams',
                              'XBA': 'European composite unit',
                              'XBB': 'European Monetary unit EC-6',
                              'XBC': 'European Unit of Account 9 (E.U.A.-9)',
                              'XBD': 'European Unit of Account 17 (E.U.A.-17)',
                              'XCD': 'Eastern Caribbean dollar',
                              'XDB': 'Currencies included in the SDR basket, gold and SDRs',
                              'XDC': 'Domestic currency (incl. conversion to current '
                                     'currency made using a fixed parity)',
                              'XDM': 'Domestic currency (incl. conversion to current '
                                     'currency made using market exchange rate)',
                              'XDO': 'Other currencies not included in the SDR basket, exc. '
                                     'gold and SDRs',
                              'XDR': 'Special Drawing Rights (SDR)',
                              'XEU': 'European Currency Unit (E.C.U.)',
                              'XFO': 'Gold-Franc',
                              'XFU': 'UIC-Franc',
                              'XGO': 'Gold fine troy ounces',
                              'XNC': 'Euro area non-participating foreign currency',
                              'XOF': 'CFA franc / BCEAO',
                              'XPC': 'Euro area participating foreign currency',
                              'XPD': 'Palladium Ounces',
                              'XPF': 'Pacific franc',
                              'XPT': 'Platinum, Ounces',
                              'XRH': 'Rhodium',
                              'XSU': 'Sucre',
                              'XTS': 'Codes specifically reserved for testing purposes',
                              'XUA': 'ADB Unit of Account',
                              'XXX': 'Transactions where no currency is involved',
                              'YER': 'Yemeni rial',
                              'YUM': 'Yugoslav dinar',
                              'Z01': 'All currencies combined',
                              'Z02': 'Euro and euro area national currencies',
                              'Z03': 'Other EU currencies combined',
                              'Z04': 'Other currencies than EU combined',
                              'Z05': 'All currencies other than EU, EUR, USD, CHF, JPY',
                              'Z06': 'Non-Euro and non-euro area currencies combined',
                              'Z07': 'All currencies other than domestic, Euro and euro '
                                     'area currencies',
                              'Z08': 'ECB EER-12 group of currencies (AU, CA, DK, HK, JP, '
                                     'NO, SG, KR, SE, CH, GB, US), changing composition of '
                                     'the euro area',
                              'Z09': 'EER broad group of currencies including also Greece '
                                     'until 01 january 2001',
                              'Z0Z': 'Not applicable',
                              'Z10': 'EER-12 group of currencies (AU, CA, DK, HK, JP, NO, '
                                     'SG, KR, SE, CH, GB, US)',
                              'Z11': 'EER broad group of currencies (excluding Greece)',
                              'Z12': 'Euro and Euro Area countries currencies (including '
                                     'Greece)',
                              'Z13': 'Other EU currencies combined (MU12; excluding GRD)',
                              'Z14': 'Other currencies than EU15 and EUR combined',
                              'Z15': 'All currencies other than EU15, EUR, USD, CHF, JPY',
                              'Z16': 'Non-MU12 currencies combined',
                              'Z17': 'ECB EER-12 group of currencies and Euro Area '
                                     'countries currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                     'ES, FI, AT, GR, AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                     'CH, GB, US)',
                              'Z18': 'ECB EER broad group of currencies and Euro Area '
                                     'countries currencies',
                              'Z19': 'ECB EER-12 group of currencies and Euro area 11 '
                                     'countries currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                     'ES, FI, AT, AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                     'GB, US)',
                              'Z20': 'ECB EER-12 group of currencies (AU, CA, DK, HK, JP, '
                                     'NO, SG, KR, SE, CH, GB, US) - Euro area 15',
                              'Z21': 'ECB EER broad group, regional breakdown, '
                                     'industrialised countries',
                              'Z22': 'ECB EER broad group, regional breakdown, non-Japan '
                                     'Asia',
                              'Z23': 'ECB EER broad group, regional breakdown, Latin America',
                              'Z24': 'ECB EER broad group, regional breakdown, Central and '
                                     'Eastern Europe (CEEC)',
                              'Z25': 'ECB EER broad group, regional breakdown, other '
                                     'countries',
                              'Z26': 'Euro area 15 countries currencies (FR, BE, LU, NL, '
                                     'DE, IT, IE, PT, ES, FI, AT, GR, SI, MT and CY)',
                              'Z27': 'ECB EER-12 group of currencies and Euro area 15 '
                                     'country currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                     'ES, FI, AT, GR, SI, CY, MT, AU, CA, DK, HK, JP, NO, '
                                     'SG, KR, SE, CH, GB, US)',
                              'Z28': 'Euro area-16 countries (BE, DE, IE, GR, ES, FR, IT, '
                                     'CY, LU, MT, NL, AT, PT, SI, SK and FI)',
                              'Z29': 'Euro area-16 countries vis-a-vis the EER-12 group of '
                                     'trading partners and other euro area countries (AU, '
                                     'CA, DK, HK, JP, NO, SG, KR, SE, CH, GB, US, BE, DE, '
                                     'IE, GR, ES, FR, IT, CY, LU, MT, NL, AT, PT, SI, SK '
                                     'and FI)',
                              'Z30': 'EER-23 group of currencies (CZ, CY, DK, EE, LV, LT, '
                                     'HU, MT, PL, SI, SK, SE, GB, AU, CA, CN, HK, JP, NO, '
                                     'SG, KR, CH, US)',
                              'Z31': 'EER-42 group of currencies (CZ, CY, DK, EE, LV, LT, '
                                     'HU, MT, PL, SI, SK, SE, GB, AU, CA, CN, HK, JP, NO, '
                                     'SG, KR, CH, US, DZ, AR, BR, BG, HR, IN, ID, IL, MY, '
                                     'MX, MA, NZ, PH, RO, RU, ZA, TW, TH, TR)',
                              'Z32': 'Euro area-17 countries (BE, DE, EE, IE, GR, ES, FR, '
                                     'IT, CY, LU, MT, NL, AT, PT, SI, SK and FI)',
                              'Z33': 'Euro area-17 countries vis-a-vis the EER-12 group of '
                                     'trading partners and other euro area countries (AU, '
                                     'CA, DK, HK, JP, NO, SG, KR, SE, CH, GB, US, BE, DE, '
                                     'EE, IE, GR, ES, FR, IT, CY, LU, MT, NL, AT, PT, SI, '
                                     'SK and FI)',
                              'Z37': 'ECB EER-23 group of currencies and Euro Area '
                                     'countries currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                     'ES, FI, AT, GR, CZ, CY, DK, EE, LV, LT, HU, MT, PL, '
                                     'SI, SK, SE, GB, AU, CA, CN, HK, JP, NO, SG, KR, CH, '
                                     'US)',
                              'Z38': 'ECB EER-42 group of currencies and Euro Area '
                                     'countries currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                     'ES, FI, AT, GR, CZ, CY, DK, EE, LV, LT, HU, MT, PL, '
                                     'SI, SK, SE, GB, AU, CA, CN, HK, JP, NO, SG, KR, CH, '
                                     'US, DZ, AR, BR, BG, HR, IN, ID, IL, MY, MX, MA, NZ, '
                                     'PH, RO, RU, ZA, TW, TH, TR)',
                              'Z40': 'ECB EER-12 group of currencies (AU, CA, DK, HK, JP, '
                                     'NO, SG, KR, SE, CH, GB, US)',
                              'Z41': 'All currencies other than domestic',
                              'Z42': 'All currencies other than EUR, USD, GBP, CHF, JPY and '
                                     'domestic',
                              'Z44': 'Other currencies than EU15, EUR and domestic',
                              'Z45': 'All currencies other than EU15, EUR, USD, CHF, JPY '
                                     'and domestic',
                              'Z46': 'All currencies other than EUR, USD, GBP and JPY',
                              'Z50': 'ECB EER-24 group of currencies (AU, CA, CN, DK, HK, '
                                     'JP, NO, SG, KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, '
                                     'LT, MT, PL, SK, BG, RO)',
                              'Z51': 'ECB EER-44 group of currencies (AU, CA, CN, DK, HK, '
                                     'JP, NO, SG, KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, '
                                     'LT, MT, PL, SK, BG, RO, NZ, DZ, AR, BR, HR, IN, ID, '
                                     'IL, MY, MX, MA, PH, RU, ZA, TW, TH, TR, IS, CL, VE)',
                              'Z52': 'Euro and Euro area 13 country currencies (FR, BE, LU, '
                                     'NL, DE, IT, IE, PT, ES, FI, AT, GR, SI)',
                              'Z53': 'Non-euro area 13 currencies combined (all currencies '
                                     'other than those related to FR, BE, LU, NL, DE, IT, '
                                     'IE, PT, ES, FI, AT, GR, SI)',
                              'Z54': 'ECB EER-22 group of currencies (AU, CA, CN, DK, HK, '
                                     'JP, NO, SG, KR, SE, CH, GB, US,CZ, EE, HU, LV, LT, '
                                     'PL, SK, BG, RO) - Euro area 15',
                              'Z55': 'ECB EER-42 group of currencies (AU, CA, CN, DK, HK, '
                                     'JP, NO, SG, KR, SE, CH, GB, US, CZ, EE, HU, LV, LT, '
                                     'PL, SK, BG, RO, NZ, DZ, AR, BR, HR, IN, ID, IL, MY, '
                                     'MX, MA, PH, RU, ZA, TW, TH, TR, IS, CL, VE) - Euro '
                                     'area 15',
                              'Z56': 'ECB EER-12 group of currencies and Euro area country '
                                     'currencies (FR, BE, LU, NL, DE, IT, IE, PT, ES, FI, '
                                     'AT, GR, SI, AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                     'GB, US)',
                              'Z57': 'ECB EER-20 group of currencies and Euro area 17 '
                                     'country currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                     'ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, SG, '
                                     'KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, PL, '
                                     'SK, BG, RO)',
                              'Z58': 'ECB EER-40 group of currencies and Euro area 17 '
                                     'country currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                     'ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, SG, '
                                     'KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, PL, '
                                     'SK, BG, RO, NZ, DZ, AR, BR, HR, IN, ID, IL, MY, MX, '
                                     'MA, PH, RU, ZA, TW, TH, TR, IS, CL, VE)',
                              'Z59': 'Euro area-16 countries vis-a-vis the EER-21 group of '
                                     'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                     'CH, GB, US, BG, CZ, EE, LV, LT, HU, PL, RO and CN)',
                              'Z60': 'Euro area-16 countries vis-a-vis the EER-41 group of '
                                     'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                     'CH, GB, US, BG, CZ, EE, LV, LT, HU, PL, RO, CN, DZ, '
                                     'AR, BR, CL, HR, IS, IN, ID, IL, MY, MX, MA, NZ, PH, '
                                     'RU, ZA, TW, TH, TR and VE)',
                              'Z61': 'ECB EER-21 group of currencies and Euro area 17 '
                                     'country currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                     'ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, SG, '
                                     'KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, PL, '
                                     'SK, BG, RO, HR)',
                              'Z62': 'Euro and Euro area 15 country currencies (FR, BE, LU, '
                                     'NL, DE, IT, IE, PT, ES, FI, AT, GR, SI, CY, MT)',
                              'Z63': 'Non-euro area 15 currencies combined (all currencies '
                                     'other than those related to FR, BE, LU, NL, DE, IT, '
                                     'IE, PT, ES, FI, AT, GR, SI, CY, MT)',
                              'Z64': 'Euro area-17 countries vis-a-vis the EER-20 group of '
                                     'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                     'CH, GB, US, BG, CZ, LV, LT, HU, PL, RO and CN)',
                              'Z65': 'Euro area-17 countries vis-a-vis the EER-40 group of '
                                     'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                     'CH, GB, US, BG, CZ, LV, LT, HU, PL, RO, CN, DZ, AR, '
                                     'BR, CL, HR, IS, IN, ID, IL, MY, MX, MA, NZ, PH, RU, '
                                     'ZA, TW, TH, TR and VE)',
                              'Z66': 'Euro area-17 countries vis-a-vis the EER-21 group of '
                                     'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                     'CH, GB, US, BG, CZ, LV, LT, HU, PL, RO, HR and CN)',
                              'Z67': 'Euro area-16 countries vis-a-vis the EER-12 group of '
                                     'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                     'CH, GB and US)',
                              'Z68': 'Euro area-17 countries vis-a-vis the EER-12 group of '
                                     'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                     'CH, GB and US)',
                              'Z69': 'Euro area-17 countries vis-a-vis the EER-23 group of '
                                     'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                     'CH, GB, US, BG, CZ, LV, LT, HU, PL, RO, HR, TR, RU '
                                     'and CN)',
                              'Z70': 'ECB EER-23 group of currencies and Euro area 17 '
                                     'country currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                     'ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, SG, '
                                     'KR, SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, PL, '
                                     'SK, BG, RO, HR, TR and RU)',
                              'Z72': 'Euro and Euro area 16 country currencies (FR, BE, LU, '
                                     'NL, DE, IT, IE, PT, ES, FI, AT, GR, SI, CY, MT, SK)',
                              'Z73': 'Non-euro area 16 currencies combined (all currencies '
                                     'other than those related to FR, BE, LU, NL, DE, IT, '
                                     'IE, PT, ES, FI, AT, GR, SI, CY, MT, SK)',
                              'Z82': 'Euro and Euro area 17 country currencies (FR, BE, LU, '
                                     'NL, DE, IT, IE, PT, ES, FI, AT, GR, SI, CY, MT, SK, '
                                     'EE)',
                              'Z83': 'Non-euro area 17 currencies combined (all currencies '
                                     'other than those related to FR, BE, LU, NL, DE, IT, '
                                     'IE, PT, ES, FI, AT, GR, SI, CY, MT, SK, EE)',
                              'ZAR': 'South African Rand',
                              'ZMK': 'Zambian kwacha',
                              'ZMW': 'New zambian kwacha',
                              'ZWD': 'Zimbabwe dollar',
                              'ZWL': 'Fourth Zimbabwe dollar',
                              'ZWN': 'Zimbabwe, Zimbabwe Dollars',
                              'ZWR': 'Third Zimbabwe dollar',
                              '_T': 'All currencies of denomination',
                              '_X': 'Not specified',
                              '_Z': 'Not applicable'},
                 'DECIMALS': {'0': 'Zero',
                              '1': 'One',
                              '10': 'Ten',
                              '11': 'Eleven',
                              '12': 'Twelve',
                              '13': 'Thirteen',
                              '14': 'Fourteen',
                              '15': 'Fifteen',
                              '2': 'Two',
                              '3': 'Three',
                              '4': 'Four',
                              '5': 'Five',
                              '6': 'Six',
                              '7': 'Seven',
                              '8': 'Eight',
                              '9': 'Nine'},
                 'EXR_SUFFIX': {'A': 'Average or standardised measure for given frequency',
                                'E': 'End-of-period',
                                'P': 'Growth rate to previous period',
                                'R': 'Annual rate of change',
                                'S': 'Accumulated perc change compared to 1998 (Dec 1998 '
                                     'for monthly series and 1998Q4 for quart. series)',
                                'T': '3-year percentage change'},
                 'EXR_TYPE': {'BRC0': 'Real bilateral exchange rate, CPI deflated',
                              'CR00': 'Central rate',
                              'DFC0': 'Real effective exch. rate deflator based on CPI',
                              'DFC1': 'Real effective exch. rate deflator based on retail '
                                      'prices',
                              'DFD0': 'Real effective exch. rate deflator based on GDP '
                                      'deflator',
                              'DFM0': 'Real effective exch. rate deflator based on import '
                                      'unit values',
                              'DFP0': 'Real effective exch. rate deflator based on producer '
                                      'prices',
                              'DFU0': 'Real effective exch. rate deflator based on ULC '
                                      'manufacturing',
                              'DFU1': 'Real effective exch. rate deflator based on ULC '
                                      'total economy',
                              'DFW0': 'Real effective exch. rate deflator based on '
                                      'wholesale prices',
                              'DFX0': 'Real effective exch. rate deflator based on export '
                                      'unit values',
                              'EN00': 'Nominal effective exch. rate',
                              'ER00': 'Constant (real) exchange rate',
                              'ERC0': 'Real effective exch. rate CPI deflated',
                              'ERC1': 'Real effective exch. rate retail prices deflated',
                              'ERD0': 'Real effective exch. rate GDP deflators deflated',
                              'ERM0': 'Real effective exch. rate import unit values deflated',
                              'ERP0': 'Real effective exch. rate producer prices deflated',
                              'ERU0': 'Real effective exch. rate ULC manufacturing deflated',
                              'ERU1': 'Real effective exch. rate ULC total economy deflated',
                              'ERW0': 'Real effective exch. rate wholesale prices deflated',
                              'ERX0': 'Real effective exch. rate export unit values deflated',
                              'F01M': '1m-forward',
                              'F03M': '3m-forward',
                              'F06M': '6m-forward',
                              'F12M': '12m-forward',
                              'IR00': 'Indicative rate',
                              'NN00': 'Nominal harmonised competitiveness indicator (ECB '
                                      'terminology), Nominal effective exchange rate (EC '
                                      'terminology)',
                              'NRC0': 'Real harmonised competitiveness indicator CPI '
                                      'deflated (ECB terminology), Real effective exchange '
                                      'rate (EC terminology)',
                              'NRD0': 'Real harmonised competitiveness indicator GDP '
                                      'deflators deflated',
                              'NRP0': 'Real harmonised competitiveness indicator Producer '
                                      'Prices deflated',
                              'NRU0': 'Real harmonised competitiveness indicator ULC '
                                      'manufacturing deflated',
                              'NRU1': 'Real harmonised competitiveness indicator ULC in '
                                      'total economy deflated',
                              'OF00': 'Official fixing',
                              'RR00': 'Reference rate',
                              'SP00': 'Spot'},
                 'FREQ': {'A': 'Annual',
                          'B': 'Business',
                          'D': 'Daily',
                          'E': 'Event (not supported)',
                          'H': 'Half-yearly',
                          'M': 'Monthly',
                          'N': 'Minutely',
                          'Q': 'Quarterly',
                          'S': 'Half Yearly, semester (value H exists but change to S in '
                               '2009, move from H to this new value to be agreed in ESCB '
                               'context)',
                          'W': 'Weekly'},
                 'OBS_CONF': {'C': 'Confidential statistical information',
                              'D': 'Secondary confidentiality set by the sender, not for '
                                   'publication',
                              'F': 'Free',
                              'N': 'Not for publication, restricted for internal use only',
                              'S': 'Secondary confidentiality set and managed by the '
                                   'receiver, not for publication'},
                 'OBS_STATUS': {'A': 'Normal value',
                                'B': 'Time series break',
                                'D': 'Definition differs',
                                'E': 'Estimated value',
                                'F': 'Forecast value',
                                'G': 'Experimental value',
                                'H': 'Missing value; holiday or weekend',
                                'I': 'Imputed value (CCSA definition)',
                                'J': 'Derogation',
                                'L': 'Missing value; data exist but were not collected',
                                'M': 'Missing value; data cannot exist',
                                'N': 'Not significant',
                                'P': 'Provisional value',
                                'Q': 'Missing value; suppressed',
                                'S': 'Strike and any special events',
                                'U': 'Low reliability',
                                'V': 'Unvalidated value'},
                 'ORGANISATION': {'1A0': 'International organisations',
                                  '1B0': 'UN organisations',
                                  '1C0': 'International Monetary Fund (IMF)',
                                  '1D0': 'World Trade Organisation',
                                  '1E0': 'International Bank for Reconstruction and '
                                         'Development',
                                  '1F0': 'International Development Association',
                                  '1G0': 'Other UN Organisations (includes 1H, 1J-1T)',
                                  '1H0': 'UNESCO (United Nations Educational, Scientific '
                                         'and Cultural Organisation)',
                                  '1J0': 'FAO (Food and Agriculture Organisation)',
                                  '1K0': 'WHO (World Health Organisation)',
                                  '1L0': 'IFAD (International Fund for Agricultural '
                                         'Development)',
                                  '1M0': 'IFC (International Finance Corporation)',
                                  '1N0': 'MIGA (Multilateral Investment Guarantee Agency)',
                                  '1O0': 'UNICEF (United Nations Children Fund)',
                                  '1P0': 'UNHCR (United Nations High Commissioner for '
                                         'Refugees)',
                                  '1Q0': 'UNRWA (United Nations Relief and Works Agency for '
                                         'Palestine)',
                                  '1R0': 'IAEA (International Atomic Energy Agency)',
                                  '1S0': 'ILO (International Labour Organisation)',
                                  '1T0': 'ITU (International Telecommunication Union)',
                                  '1U0': 'UNECE (United Nations Economic Commission for '
                                         'Europe)',
                                  '1W0': 'World Bank',
                                  '1Z0': 'Rest of\xa0UN Organisations\xa0n.i.e.',
                                  '4A0': 'European Community Institutions, Organs and '
                                         'Organisms',
                                  '4B0': 'EMS (European Monetary System)',
                                  '4C0': 'European Investment Bank',
                                  '4D0': 'Statistical Office of the European Commission '
                                         '(Eurostat)',
                                  '4D1': 'European Commission (including Eurostat)',
                                  '4E0': 'European Development Fund',
                                  '4F0': 'European Central Bank (ECB)',
                                  '4F1': 'ECB_LM',
                                  '4F2': 'ECB_AC',
                                  '4F3': 'ECB_FO',
                                  '4F4': 'ECB_MB',
                                  '4F5': 'D-Internal Finance',
                                  '4F6': 'ECB, D-BN',
                                  '4F7': 'ECB, DG-P',
                                  '4G0': 'EIF (European Investment Fund)',
                                  '4H0': 'European Community of Steel and Coal',
                                  '4I0': 'Neighbourhood Investment Facility',
                                  '4J0': 'Other EC Institutions, Organs and Organisms '
                                         'covered by General budget',
                                  '4J10': 'European Parliament',
                                  '4J20': 'Council of the European Union',
                                  '4J30': 'Court of Justice',
                                  '4J40': 'Court of Auditors',
                                  '4J50': 'European Council',
                                  '4J60': 'Economic and Social Committee',
                                  '4J70': 'Committee of Regions',
                                  '4J80': 'Other European Community Institutions, Organs '
                                          'and Organisms',
                                  '4K0': 'European Parliament',
                                  '4L0': 'European Council',
                                  '4M0': 'Court of Justice',
                                  '4N0': 'Court of Auditors',
                                  '4P0': 'Economic and Social Committee',
                                  '4Q0': 'Committee of Regions',
                                  '4S0': 'European Stability Mechanism (ESM)',
                                  '4T0': 'Joint Committee of the European Supervisory '
                                         'Authorities (ESAs)',
                                  '4T1': 'European Banking Agency (EBA, European '
                                         'Supervisory Authority)',
                                  '4T10': 'EBA (European Banking Authority)',
                                  '4T2': 'European Insurance and Occupational Pensions '
                                         'Authority (EIOPA, European Supervisory Authority)',
                                  '4T20': 'ESMA (European Securities and Markets Authority)',
                                  '4T3': 'European Securities and Markets Agency (ESMA, '
                                         'European Supervisory Authority)',
                                  '4T30': 'EIOPA (European Insurance and Occupational '
                                          'Pensions Authority)',
                                  '4V0': 'FEMIP (Facility for Euro-Mediterranean Investment '
                                         'and Partnership)',
                                  '4Y0': 'All the European Union Institutions including the '
                                         'ECB and ESM',
                                  '4Z0': 'Other European Community Institutions, Organs and '
                                         'Organisms',
                                  '5A0': 'Organisation for Economic Cooperation and '
                                         'Development (OECD)',
                                  '5B0': 'Bank for International Settlements (BIS)',
                                  '5C0': 'Inter-American Development Bank',
                                  '5D0': 'African Development Bank',
                                  '5E0': 'Asian Development Bank',
                                  '5F0': 'European Bank for Reconstruction and Development',
                                  '5G0': 'IIC (Inter-American Investment Corporation)',
                                  '5H0': 'NIB (Nordic Investment Bank)',
                                  '5I0': 'Eastern Caribbean Central Bank (ECCB)',
                                  '5J0': 'IBEC (International Bank for Economic '
                                         'Co-operation)',
                                  '5K0': 'IIB (International Investment Bank)',
                                  '5L0': 'CDB (Caribbean Development Bank)',
                                  '5M0': 'AMF (Arab Monetary Fund)',
                                  '5N0': 'BADEA (Banque arabe pour le developpement '
                                         'economique en Afrique)',
                                  '5O0': 'Banque Centrale des Etats de l`Afrique de l`Ouest '
                                         '(BCEAO)',
                                  '5P0': 'CASDB (Central African States Development Bank)',
                                  '5Q0': 'African Development Fund',
                                  '5R0': 'Asian Development Fund',
                                  '5S0': 'Fonds special unifie de developpement',
                                  '5T0': 'CABEI (Central American Bank for Economic '
                                         'Integration)',
                                  '5U0': 'ADC (Andean Development Corporation)',
                                  '5V0': 'Other International Organisations (financial '
                                         'institutions)',
                                  '5W0': 'Banque des Etats de l`Afrique Centrale (BEAC)',
                                  '5X0': 'Communaute economique et Monetaire de l`Afrique '
                                         'Centrale (CEMAC)',
                                  '5Y0': 'Eastern Caribbean Currency Union (ECCU)',
                                  '5Z0': 'Other International Financial Organisations n.i.e.',
                                  '6A0': 'Other International Organisations (non-financial '
                                         'institutions)',
                                  '6B0': 'NATO (North Atlantic Treaty Organisation)',
                                  '6C0': 'Council of Europe',
                                  '6D0': 'ICRC (International Committee of the Red Cross)',
                                  '6E0': 'ESA (European Space Agency)',
                                  '6F0': 'EPO (European Patent Office)',
                                  '6G0': 'EUROCONTROL (European Organisation for the Safety '
                                         'of Air Navigation)',
                                  '6H0': 'EUTELSAT (European Telecommunications Satellite '
                                         'Organisation)',
                                  '6I0': 'West African Economic and Monetary Union (WAEMU)',
                                  '6J0': 'INTELSAT (International Telecommunications '
                                         'Satellite Organisation)',
                                  '6K0': 'EBU/UER (European Broadcasting Union/Union '
                                         'europeenne de radio-television)',
                                  '6L0': 'EUMETSAT (European Organisation for the '
                                         'Exploitation of Meteorological Satellites)',
                                  '6M0': 'ESO (European Southern Observatory)',
                                  '6N0': 'ECMWF (European Centre for Medium-Range Weather '
                                         'Forecasts)',
                                  '6O0': 'EMBL (European Molecular Biology Laboratory)',
                                  '6P0': 'CERN (European Organisation for Nuclear Research)',
                                  '6Q0': 'IOM (International Organisation for Migration)',
                                  '6R0': 'Islamic Development Bank (IDB)',
                                  '6S0': 'Eurasian Development Bank (EDB)',
                                  '6T0': 'Paris Club Creditor Institutions',
                                  '6Z0': 'Other International Non-Financial Organisations '
                                         'n.i.e.',
                                  '7A0': 'WAEMU (West African Economic and Monetary Union)',
                                  '7B0': 'IDB (Islamic Development Bank)',
                                  '7C0': 'EDB (Eurasian Development Bank )',
                                  '7D0': 'Paris Club Creditor Institutions',
                                  '7E0': 'CEB (Council of Europe Development Bank)',
                                  '7F0': 'International Union of Credit and Investment '
                                         'Insurers',
                                  '7G0': 'Black Sea Trade and Development Banks',
                                  '7H0': 'AFREXIMBANK (African Export-Import Bank)',
                                  '7I0': 'BLADEX (Banco Latino Americano De Comercio '
                                         'Exterior)',
                                  '7J0': 'FLAR (Fondo Latino Americano de Reservas)',
                                  '7K0': 'Fonds Belgo-Congolais d Amortissement et de '
                                         'Gestion',
                                  '7L0': 'IFFIm (International finance Facility for '
                                         'Immunisation)',
                                  '7M0': 'EUROFIMA (European Company for the Financing of '
                                         'Railroad Rolling Stock)',
                                  '7Z0': 'International Organisations excl. European '
                                         'Community Institutions (4A)',
                                  '8A0': 'International Union of Credit and Investment '
                                         'Insurers',
                                  '9A0': 'International Organisations excl. European '
                                         'Community Institutions (4Y)',
                                  'AE1': 'Central Statistical Organization, part of the '
                                         'Ministry of Economy and Planning (United Arab '
                                         'Emirates)',
                                  'AE2': 'Central Bank of the United Arab Emirates',
                                  'AE4': 'Ministry of Finance and Industry (United Arab '
                                         'Emirates)',
                                  'AF2': 'Da Afghanistan Bank',
                                  'AF4': 'Ministry of Finance (Afghanistan, Islamic State '
                                         'of)',
                                  'AG2': 'Eastern Caribbean Central Bank (ECCB) (Antigua '
                                         'and Barbuda)',
                                  'AG4': 'Ministry of Finance (Antigua and Barbuda)',
                                  'AI1': 'Central Statistical Office (Anguilla)',
                                  'AI4': 'Ministry of Finance (Anguilla)',
                                  'AI99': 'Other competent National Authority (Anguilla)',
                                  'AL1': 'Institution of Statistics (Albania)',
                                  'AL2': 'Bank of Albania',
                                  'AL4': 'Ministere des Finances (Albania)',
                                  'AM1': 'State National Statistics Service (Armenia)',
                                  'AM2': 'Central Bank of Armenia',
                                  'AM4': 'Ministry of Finance and Economy (Armenia)',
                                  'AM99': 'Other competent National Authority (Armenia, '
                                          'Republic of)',
                                  'AN1': 'Central Bureau of Statistics (Netherlands '
                                         'Antilles)',
                                  'AN2': 'Bank of the Netherlands Antilles',
                                  'AN99': 'Other competent National Authority (Netherlands '
                                          'Antilles)',
                                  'AO1': 'National Institute of Statistics (Angola)',
                                  'AO2': 'Banco Nacional de Angola',
                                  'AO4': 'Ministerio das Financas (Angola)',
                                  'AR1': 'Instituto Nacional de Estadistica y Censos '
                                         '(Argentina)',
                                  'AR2': 'Banco Central de la Republica Argentina',
                                  'AR4': 'Ministerio de Economia (Argentina)',
                                  'AR99': 'Other competent National Authority (Argentina)',
                                  'AT1': 'Statistik Osterreich (Austria)',
                                  'AT2': 'Oesterreichische Nationalbank (Austria)',
                                  'AT99': 'Other competent National Authority (Austria)',
                                  'AU1': 'Australian Bureau of Statistics',
                                  'AU2': 'Reserve Bank of Australia',
                                  'AU3': 'Australian Prudential Regulation Authority',
                                  'AU5': 'Department of the Treasury (Australia)',
                                  'AU99': 'Other competent National Authority (Australia)',
                                  'AW1': 'Central Bureau of Statistics (Aruba)',
                                  'AW2': 'Centrale Bank van Aruba',
                                  'AW99': 'Other competent National Authority (Aruba)',
                                  'AZ1': 'State Statistics Committee of the Azerbaijan '
                                         'Republic',
                                  'AZ2': 'National Bank of Azerbaijan',
                                  'AZ4': 'Ministry of Finance (Azerbaijan)',
                                  'AZ99': 'Other competent National Authority (Azerbaijan, '
                                          'Republic of)',
                                  'B22': 'EU 15 central banks',
                                  'B32': 'EU 25 central banks',
                                  'B42': 'EU 27 central banks',
                                  'B52': 'EU 28 central banks',
                                  'BA1': 'Institute of Statistics (Bosnia and Herzegovina)',
                                  'BA2': 'Central Bank of Bosnia and Herzegovina',
                                  'BA4': 'Ministry of Finance for the Federation of Bosnia '
                                         'and Herzegovina',
                                  'BA99': 'Other competent National Authority (Bosnia and '
                                          'Herzegovina)',
                                  'BB1': 'Barbados Statistical Service',
                                  'BB2': 'Central Bank of Barbados',
                                  'BB4': 'Ministry of Finance and Economic Affairs '
                                         '(Barbados)',
                                  'BB99': 'Other competent National Authority (Barbados)',
                                  'BD1': 'Bangladesh Bureau of Statistics',
                                  'BD2': 'Bangladesh Bank',
                                  'BD4': 'Ministry of Finance (Bangladesh)',
                                  'BE1': 'Institut National de Statistiques de Belgique '
                                         '(Belgium)',
                                  'BE2': 'Banque Nationale de Belgique (Belgium)',
                                  'BE3': 'Federal Public Service Budget (Belgium)',
                                  'BE9': 'Bureau van Dijk',
                                  'BE99': 'Other competent National Authority (Belgium)',
                                  'BF2': 'Banque Centrale des Etats de l`Afrique de l`Ouest '
                                         '(BCEAO) (Burkina Faso)',
                                  'BF4': 'Ministere de l`Economie et des Finances (Burkina '
                                         'Faso)',
                                  'BG1': 'National Statistical Institute of Bulgaria',
                                  'BG2': 'Bulgarian National Bank',
                                  'BG3': 'Prime Ministers Office (Bulgaria)',
                                  'BG4': 'Ministry of Finance (Bulgaria)',
                                  'BG99': 'Other competent National Authority (Bulgaria)',
                                  'BH1': 'Directorate of Statistics (Bahrain)',
                                  'BH2': 'Bahrain Monetary Authority',
                                  'BH4': 'Ministry of Finance and National Economy (Bahrain)',
                                  'BH99': 'Other competent National Authority (Bahrain, '
                                          'Kingdom of)',
                                  'BI2': 'Banque de la Republique du Burundi',
                                  'BI3': 'Ministere du Plan (Burundi)',
                                  'BI4': 'Ministere des finances (Burundi)',
                                  'BJ1': 'Institut National de la Statistique et de '
                                         'l`Analyse Economique (Benin)',
                                  'BJ2': 'Banque Centrale des Etats de l`Afrique de l`Ouest '
                                         '(BCEAO) (Benin)',
                                  'BJ4': 'Ministere des Finances (Benin)',
                                  'BJ99': 'Other competent National Authority (Benin)',
                                  'BM1': 'Bermuda Government - Department of Statistics',
                                  'BM2': 'Bermuda Monetary Authority',
                                  'BM99': 'Other competent National Authority (Bermuda)',
                                  'BN1': 'Department of Statistics (Brunei Darussalam)',
                                  'BN2': 'Brunei Currency and Monetary Board (BCMB)',
                                  'BN3': 'Department of Economic Planning and Development '
                                         '(DEPD) (Brunei Darussalam)',
                                  'BN4': 'Ministry of Finance (Brunei Darussalam)',
                                  'BN99': 'Other competent National Authority (Brunei '
                                          'Darussalam)',
                                  'BO1': 'Instituto Nacional de Estadistica (Bolivia)',
                                  'BO2': 'Banco Central de Bolivia',
                                  'BO3': 'Secretaria Nacional de Hacienda (Bolivia)',
                                  'BO4': 'Ministerio de Hacienda (Bolivia)',
                                  'BO99': 'Other competent National Authority (Bolivia)',
                                  'BR1': 'Brazilian Institute of Statistics and Geography '
                                         '(IBGE) (Brazil)',
                                  'BR2': 'Banco Central do Brasil',
                                  'BR3': 'Ministry of Industry, Commerce and Tourism, '
                                         'Secretariat of Foreign Commerce (SECEX) (Brazil)',
                                  'BR4': 'Ministerio da Fazenda (Brazil)',
                                  'BS1': 'Department of Statistics (Bahamas)',
                                  'BS2': 'The Central Bank of the Bahamas',
                                  'BS4': 'Ministry of Finance (Bahamas)',
                                  'BS99': 'Other competent National Authority (Bahamas, The)',
                                  'BT1': 'Central Statistical Office (Bhutan)',
                                  'BT2': 'Royal Monetary Authority of Bhutan',
                                  'BT4': 'Ministry of Finance (Bhutan)',
                                  'BW1': 'Central Statistics Office (Botswana)',
                                  'BW2': 'Bank of Botswana',
                                  'BW3': 'Department of Customs and Excise (Botswana)',
                                  'BW4': 'Ministry of Finance and Development Planning '
                                         '(Botswana)',
                                  'BY1': 'Ministry of Statistics and Analysis of the '
                                         'Republic of Belarus',
                                  'BY2': 'National Bank of Belarus',
                                  'BY4': 'Ministry of Finance of the Republic of Belarus',
                                  'BY99': 'Other competent National Authority (Belarus)',
                                  'BZ1': 'Central Statistical Office (Belize)',
                                  'BZ2': 'Central Bank of Belize',
                                  'BZ3': 'Ministry of Foreign Affairs (Belize)',
                                  'BZ4': 'Ministry of Finance (Belize)',
                                  'BZ99': 'Other competent National Authority (Belize)',
                                  'C992': 'Central banks of the new EU Member States 2004 '
                                          '(CY,CZ,EE,HU,LV,LT,MT,PL,SK,SI)',
                                  'CA1': 'Statistics Canada',
                                  'CA2': 'Bank of Canada',
                                  'CA99': 'Other competent National Authority (Canada)',
                                  'CD1': 'Institute National de la Statistique (Congo, Dem. '
                                         'Rep. of)',
                                  'CD2': 'Banque Centrale du Congo (Congo, Dem. Rep. of)',
                                  'CD4': 'Ministry of Finance and Budget (Congo, Dem. Rep. '
                                         'of)',
                                  'CD5': 'National Office of Research and Development '
                                         '(Congo, Dem. Rep. of)',
                                  'CD99': 'Other competent National Authority (Congo, '
                                          'Democratic Republic of)',
                                  'CF2': 'Banque des Etats de l`Afrique Centrale (BEAC) '
                                         '(Central African Republic)',
                                  'CF3': 'Presidence de la Republique (Central African '
                                         'Republic)',
                                  'CF4': 'Ministere des Finances, du Plan et de la '
                                         'Cooperation International (Central African '
                                         'Republic)',
                                  'CG1': 'Centre National de la Statistique et des Etudes '
                                         'Economiques (CNSEE) (Congo, Rep of)',
                                  'CG2': 'Banque des Etats de l`Afrique Centrale (BEAC) '
                                         '(Congo, Rep. of)',
                                  'CG4': 'Ministere de l`economie, des finances et du '
                                         'budget (Congo, Rep of)',
                                  'CG99': 'Other competent National Authority (Congo, '
                                          'Republic of)',
                                  'CH1': 'Swiss Federal Statistical Office',
                                  'CH2': 'Schweizerische Nationalbank (Switzerland)',
                                  'CH3': 'Direction generale des douanes (Switzerland)',
                                  'CH4': 'Swiss Federal Finance Administration (Switzerland)',
                                  'CH99': 'Other competent National Authority (Switzerland)',
                                  'CI2': 'Banque Centrale des Etats de l`Afrique de l`Ouest '
                                         '(BCEAO) (Cote d`Ivoire)',
                                  'CI4': 'Ministere de l`Economie et des Finances (Cote '
                                         'd`Ivoire)',
                                  'CK1': 'Cook Islands Statistics Office',
                                  'CK4': 'Cook Islands Ministry of Finance',
                                  'CL2': 'Banco Central de Chile',
                                  'CL4': 'Ministerio de Hacienda (Chile)',
                                  'CM2': 'Banque des Etats de l`Afrique Centrale (BEAC) '
                                         '(Cameroon)',
                                  'CM3': 'Ministere du Plan et de l`Amenagement du '
                                         'Territoire (Cameroon)',
                                  'CM4': 'Ministere de l`economie et des finances (Cameroon)',
                                  'CN1': 'State National Bureau of Statistics (China, P.R. '
                                         'Mainland)',
                                  'CN2': 'The Peoples Bank of China',
                                  'CN3': 'State Administration of Foreign Exchange (China, '
                                         'P.R. Mainland)',
                                  'CN4': 'Ministry of Finance (China, P.R. Mainland)',
                                  'CN5': 'General Administration of Customs (China, P.R. '
                                         'Mainland)',
                                  'CN99': 'Other competent National Authority (China, P.R., '
                                          'Mainland)',
                                  'CO1': 'Centro Administrativo Nacional (Colombia)',
                                  'CO2': 'Banco de la Republica (Colombia)',
                                  'CO4': 'Ministerio de Hacienda y Credito Publico '
                                         '(Colombia)',
                                  'CO99': 'Other competent National Authority (Colombia)',
                                  'CR2': 'Banco Central de Costa Rica',
                                  'CR4': 'Ministerio de Hacienda (Costa Rica)',
                                  'CS1': 'Federal Statistical Office (Serbia and Montenegro)',
                                  'CS2': 'National Bank of Serbia',
                                  'CS4': 'Federal Ministry of Finance (Serbia and '
                                         'Montenegro)',
                                  'CS99': 'Other competent National Authority (Serbia and '
                                          'Montenegro)',
                                  'CU1': 'Oficina National de Estadisticas (Cuba)',
                                  'CU2': 'Banco Central de Cuba',
                                  'CU99': 'Other competent National Authority (Cuba)',
                                  'CV1': 'Instituto Nacional de Estatistica (Cape Verde)',
                                  'CV2': 'Banco de Cabo Verde (Cape Verde)',
                                  'CV3': 'Ministere de la coordination economique (Cape '
                                         'Verde)',
                                  'CV4': 'Ministerio das Financas (Cape Verde)',
                                  'CV99': 'Other competent National Authority (Cape Verde)',
                                  'CW1': 'Central Bureau of Statistics (Curacao)',
                                  'CW2': 'Central Bank of Curacao and Sint Maarten',
                                  'CW99': 'Other competent National Authority (Curacao)',
                                  'CY1': 'Cyprus, Department of Statistics and Research '
                                         '(Ministry of Finance)',
                                  'CY2': 'Central Bank of Cyprus',
                                  'CY4': 'Ministry of Finance (Cyprus)',
                                  'CY99': 'Other competent National Authority (Cyprus)',
                                  'CZ1': 'Czech Statistical Office',
                                  'CZ2': 'Czech National Bank',
                                  'CZ3': 'Ministry of Transport and '
                                         'Communications/Transport Policy (Czech Republic)',
                                  'CZ4': 'Ministry of Finance of the Czech Republic',
                                  'CZ99': 'Other competent National Authority (Czech '
                                          'Republic)',
                                  'D22': 'EU 15 central banks',
                                  'D32': 'EU 25 central banks',
                                  'D82': 'Central banks of the new EU Member States 2004 '
                                         '(CY,CZ,EE,HU,LV,LT,MT,PL,SK,SI)',
                                  'DE1': 'Statistisches Bundesamt (Germany)',
                                  'DE2': 'Deutsche Bundesbank (Germany)',
                                  'DE3': 'Kraftfahrt-Bundesamt (Germany)',
                                  'DE4': 'Bundesministerium der Finanzen (Germany)',
                                  'DE8': 'IFO Institut fur Wirtschaftsforschung (Germany)',
                                  'DE9': 'Zentrum fur Europaische Wirtschaftsforschnung '
                                         '(ZEW, Germany)',
                                  'DE99': 'Other competent National Authority (Germany)',
                                  'DJ1': 'Direction Nationale de la Statistique (National '
                                         'Department of Statistics) (Djibouti)',
                                  'DJ2': 'Banque Nationale de Djibouti',
                                  'DJ3': 'Tresor National (Djibouti)',
                                  'DJ4': 'Ministere de l`Economie et des Finances (Djibouti)',
                                  'DK1': 'Danmarks Statistik (Denmark)',
                                  'DK2': 'Danmarks Nationalbank (Denmark)',
                                  'DK98': 'Danish Civil Aviation Administration',
                                  'DK99': 'Other competent National Authority (Denmark)',
                                  'DM1': 'Central Statistical Office (Dominica)',
                                  'DM2': 'Eastern Caribbean Central Bank (ECCB) (Dominica)',
                                  'DM4': 'Ministry of Finance (Dominica)',
                                  'DM99': 'Other competent National Authority (Dominica)',
                                  'DO2': 'Banco Central de la Republica Dominicana',
                                  'DZ1': 'Office National des Statistiques (Algeria)',
                                  'DZ2': 'Banque d`Algerie',
                                  'DZ4': 'Ministere des Finances (Algeria)',
                                  'DZ99': 'Other competent National Authority (Algeria)',
                                  'EC1': 'Instituto Nacional de Estadistica y Censos '
                                         '(Ecuador)',
                                  'EC2': 'Banco Central del Ecuador',
                                  'EC4': 'Ministerio de Finanzas y Credito Publico (Ecuador)',
                                  'EC99': 'Other competent National Authority (Ecuador)',
                                  'EE1': 'Estonia, State Statistical Office',
                                  'EE2': 'Bank of Estonia',
                                  'EE4': 'Ministry of Finance (Estonia)',
                                  'EE99': 'Other competent National Authority (Estonia)',
                                  'EG1': 'Central Agency for Public Mobilization and Stats. '
                                         '(Egypt)',
                                  'EG2': 'Central Bank of Egypt',
                                  'EG4': 'Ministry of Finance (Egypt)',
                                  'EG99': 'Other competent National Authority (Egypt)',
                                  'ER2': 'Bank of Eritrea',
                                  'ER4': 'Ministry of Finance (Eritrea)',
                                  'ES1': 'Instituto Nacional de Statistica (Spain)',
                                  'ES2': 'Banco de Espana (Spain)',
                                  'ES3': 'Departamento de Aduanas (Spain)',
                                  'ES4': 'Ministerio de Economia y Hacienda (Spain)',
                                  'ES5': 'Ministerio de Industria, Tourismo y Comerco '
                                         '(Spain)',
                                  'ES97': 'Puertos del Estado/Portel Spain',
                                  'ES98': 'Ministerio de Fomento - AENA',
                                  'ES99': 'Other competent National Authority (Spain)',
                                  'ET2': 'National Bank of Ethiopia',
                                  'ET3': 'Customs and Excise Administration (Ethiopia)',
                                  'ET4': 'Ministry of Finance (Ethiopia)',
                                  'FI1': 'Statistics Finland (Finland)',
                                  'FI2': 'Bank of Finland (Finland)',
                                  'FI3': 'National Board of Customs (Finland)',
                                  'FI4': 'Ministry of Finance ((Finland)',
                                  'FI97': 'Finnish Maritime Administration',
                                  'FI98': 'Finavia(Civil Aviation Administration)',
                                  'FI99': 'Other competent National Authority (Finland)',
                                  'FJ1': 'Bureau of Statistics (Fiji)',
                                  'FJ2': 'Reserve Bank of Fiji',
                                  'FJ4': 'Ministry of Finance and National Planning (Fiji)',
                                  'FJ99': 'Other competent National Authority (Fiji)',
                                  'FM1': 'Office of Planning and Statistics (Micronesia, '
                                         'Federated States of)',
                                  'FM2': 'Federal States of Micronesia Banking Board '
                                         '(Micronesia, Federated States of)',
                                  'FM99': 'Other competent National Authority (Micronesia, '
                                          'Federated States of)',
                                  'FR1': 'Institut National de la Statistique et des Etudes '
                                         'Economiques - INSEE (France)',
                                  'FR2': 'Banque de France (France)',
                                  'FR3': 'Ministere de l Equipement, des Transports et du '
                                         'Logement (France)',
                                  'FR4': 'Ministere de l`Economie et des Finances (France)',
                                  'FR5': 'Direction generale des douanes (France)',
                                  'FR6': 'National Council of Credit (France)',
                                  'FR97': 'DTMPL France',
                                  'FR98': 'DGAC(Direction General de l`Aviation Civil)',
                                  'FR99': 'Other competent National Authority (France)',
                                  'GA2': 'Banque des Etats de l`Afrique Centrale (BEAC) '
                                         '(Gabon)',
                                  'GA3': 'Ministere du Plan (Gabon)',
                                  'GA4': 'Ministry of Economy, Finance and Privatization '
                                         '(Gabon)',
                                  'GA5': 'Tresorier-Payeur General du Gabon',
                                  'GB1': 'Office for National Statistics (United Kingdom)',
                                  'GB2': 'Bank of England (United Kingdom)',
                                  'GB3': 'Department of Environment, Transport and the '
                                         'Regions (United Kingdom)',
                                  'GB4': 'Department of Trade and Industry (United Kingdom)',
                                  'GB9': 'Markit (United Kingdom)',
                                  'GB98': 'CAA (Civil Aviation Authority)',
                                  'GB99': 'Other competent National Authority (United '
                                          'Kingdom)',
                                  'GD2': 'Eastern Caribbean Central Bank (ECCB) (Grenada)',
                                  'GD4': 'Ministry of Finance (Grenada)',
                                  'GE1': 'State Department for Statistics of Georgia',
                                  'GE2': 'National Bank of Georgia',
                                  'GE4': 'Ministry of Finance (Georgia)',
                                  'GE99': 'Other competent National Authority (Georgia)',
                                  'GF1': 'Institut National de la Statistique et des Etudes '
                                         'Economiques - INSEE - Service regional (Guiana, '
                                         'French)',
                                  'GF99': 'Other competent National Authority (Guiana, '
                                          'French)',
                                  'GG6': 'Financial Services Commission, Guernsey (GG)',
                                  'GH1': 'Ghana Statistical Service',
                                  'GH2': 'Bank of Ghana',
                                  'GH4': 'Ministry of Finance (Ghana)',
                                  'GH99': 'Other competent National Authority (Ghana)',
                                  'GM1': 'Central Statistics Division (Gambia)',
                                  'GM2': 'Central Bank of The Gambia',
                                  'GM4': 'Ministry of Finance and Economic Affairs (Gambia)',
                                  'GN1': 'Service de la Statistique generale et de la '
                                         'Mecanographie (Guinea)',
                                  'GN2': 'Banque Centrale de la Republique de Guinee',
                                  'GN4': 'Ministere de l`Economie et des Finances (Guinea)',
                                  'GN99': 'Other competent National Authority (Guinea)',
                                  'GP1': 'Institut National de la Statistique et des Etudes '
                                         'Economiques - INSEE -Service regional (Guadeloupe)',
                                  'GP99': 'Other competent National Authority (Guadeloupe)',
                                  'GQ2': 'Banque des Etats de l`Afrique Centrale (BEAC) '
                                         '(Equatorial Guinea)',
                                  'GQ4': 'Ministerio de Economia y Hacienda (Equatorial '
                                         'Guinea)',
                                  'GR1': 'National Statistical Service of Greece (Greece)',
                                  'GR2': 'Bank of Greece (Greece)',
                                  'GR4': 'Ministry of Economy and Finance (Greece)',
                                  'GR98': 'Civil Aviation Authority',
                                  'GR99': 'Other competent National Authority (Greece)',
                                  'GT1': 'Instituto Nacional de Estadistica (Guatemala)',
                                  'GT2': 'Banco de Guatemala',
                                  'GT4': 'Ministerio de Finanzas Publicas (Guatemala)',
                                  'GT99': 'Other competent National Authority (Guatemala)',
                                  'GU1': 'Guam Bureau of Statistics',
                                  'GW2': 'Banque Centrale des Etats de l`Afrique de l`Ouest '
                                         '(BCEAO) (Guinea-Bissau)',
                                  'GW4': 'Ministere de l`Economie et des Finances '
                                         '(Guinea-Bissau)',
                                  'GY1': 'Statistical Bureau / Ministry of Planning (Guyana)',
                                  'GY2': 'Bank of Guyana',
                                  'GY4': 'Ministry of Finance (Guyana)',
                                  'GY99': 'Other competent National Authority (Guyana)',
                                  'HK1': 'Census and Statistics Department (China, P.R. '
                                         'Hong Kong)',
                                  'HK2': 'Hong Kong Monetary Authority',
                                  'HK4': 'Financial Services and the Treasury Bureau '
                                         '(Treasury) (China, P.R. Hong Kong)',
                                  'HK99': 'Other competent National Authority (Hong Kong)',
                                  'HN1': 'Direccion General de Censos y Estadisticas '
                                         '(Honduras)',
                                  'HN2': 'Banco Central de Honduras',
                                  'HN4': 'Ministerio de Hacienda y Credito Publico '
                                         '(Honduras)',
                                  'HN99': 'Other competent National Authority (Honduras)',
                                  'HR1': 'Central Bureau of Statistics (Croatia)',
                                  'HR2': 'Croatian National Bank',
                                  'HR4': 'Ministry of Finance (Croatia)',
                                  'HR99': 'Other competent National Authority (Croatia)',
                                  'HT1': 'Institut Haitien de Statistique et d`Informatique '
                                         '(Haiti)',
                                  'HT2': 'Banque de la Republique dHaiti',
                                  'HT4': 'Ministere de l`Economie et des Finances (Haiti)',
                                  'HT99': 'Other competent National Authority (Haiti)',
                                  'HU1': 'Hungarian Central Statistical Office',
                                  'HU2': 'National Bank of Hungary',
                                  'HU4': 'Ministry of Finance (Hungary)',
                                  'HU99': 'Other competent National Authority (Hungary)',
                                  'I22': 'Euro area 12 central banks',
                                  'I32': 'Euro area 13 central banks',
                                  'I42': 'Euro area 15 central banks',
                                  'I52': 'Euro area 16 central banks',
                                  'I62': 'Euro area 17 central banks',
                                  'I72': 'Euro area 18 central banks',
                                  'I82': 'Euro area 19 central banks',
                                  'ID1': 'BPS-Statistics Indonesia',
                                  'ID2': 'Bank Indonesia',
                                  'ID4': 'Ministry of Finance (Indonesia)',
                                  'ID99': 'Other competent National Authority (Indonesia)',
                                  'IE1': 'Central Statistical Office (Ireland)',
                                  'IE2': 'Central Bank of Ireland (Ireland)',
                                  'IE3': 'The Office of the Revenue Commissioners (Ireland)',
                                  'IE4': 'Department of Finance (Ireland)',
                                  'IE99': 'Other competent National Authority (Ireland)',
                                  'IL1': 'Central Bureau of Statistics (Israel)',
                                  'IL2': 'Bank of Israel',
                                  'IL99': 'Other competent National Authority (Israel)',
                                  'IM6': 'Financial Supervision Commission, Isle of Man (IM)',
                                  'IN2': 'Reserve Bank of India',
                                  'IN4': 'Ministry of Finance (India)',
                                  'IQ2': 'Central Bank of Iraq',
                                  'IQ4': 'Ministry of Finance (Iraq)',
                                  'IR2': 'The Central Bank of the Islamic Republic of Iran',
                                  'IS1': 'Statistics Iceland',
                                  'IS2': 'Central Bank of Iceland',
                                  'IS98': 'Civil Aviation Administration',
                                  'IS99': 'Other competent National Authority (Iceland)',
                                  'IT1': 'Instituto Nazionale di Statistica - ISTAT (Italy)',
                                  'IT2': 'Banca d` Italia (Italy)',
                                  'IT3': 'Ufficio Italiano dei Cambi (Italy)',
                                  'IT4': 'Ministerio de Tesore (Italy)',
                                  'IT9': 'Instituto di Studi e Analisi Economica (Italy)',
                                  'IT99': 'Other competent National Authority (Italy)',
                                  'JE6': 'Financial Services Commission, Jersey (JE)',
                                  'JM1': 'Statistical Institute of Jamaica',
                                  'JM2': 'Bank of Jamaica',
                                  'JM4': 'Ministry of Finance and Planning (Jamaica)',
                                  'JM99': 'Other competent National Authority (Jamaica)',
                                  'JO1': 'Department of Statistics (Jordon)',
                                  'JO2': 'Central Bank of Jordan',
                                  'JO4': 'Ministry of Finance (Jordon)',
                                  'JO99': 'Other competent National Authority (Jordan)',
                                  'JP1': 'Bureau of Statistics (Japan)',
                                  'JP2': 'Bank of Japan',
                                  'JP4': 'Ministry of Finance (Japan)',
                                  'JP6': 'Financial Services Agency (Japan)',
                                  'KE1': 'Central Bureau of Statistics (Kenya)',
                                  'KE2': 'Central Bank of Kenya',
                                  'KE3': 'Ministry of Planning and National Development '
                                         '(Kenya)',
                                  'KE4': 'Office of the Vice President and Ministry of '
                                         'Finance (Kenya)',
                                  'KE99': 'Other competent National Authority (Kenya)',
                                  'KG1': 'National Statistical Committee of Kyrgyz Republic',
                                  'KG2': 'National Bank of the Kyrgyz Republic',
                                  'KG4': 'Ministry of Finance (Kyrgyz Republic)',
                                  'KG99': 'Other competent National Authority (Kyrgyz '
                                          'Republic)',
                                  'KH1': 'National Institute of Statistics (Cambodia)',
                                  'KH2': 'National Bank of Cambodia',
                                  'KH4': 'Ministere de l`economie et des finances (Cambodia)',
                                  'KI2': 'Bank of Kiribati, Ltd',
                                  'KI4': 'Ministry of Finance and Economic Planning '
                                         '(Kiribati)',
                                  'KM2': 'Banque Centrale des Comoros',
                                  'KM4': 'Ministere des Finances, du budget et du plan '
                                         '(Comoros)',
                                  'KN1': 'Statistical Office (St. Kitts and Nevis)',
                                  'KN2': 'Eastern Caribbean Central Bank (ECCB) (St. Kitts '
                                         'and Nevis)',
                                  'KN4': 'Ministry of Finance (St. Kitts and Nevis)',
                                  'KR1': 'Korea National Statistical Office (KNSO)',
                                  'KR2': 'The Bank of Korea',
                                  'KR3': 'Economic Planning Board (Korea, Republic of)',
                                  'KR4': 'Ministry of Finance and Economy (Korea, Republic '
                                         'of)',
                                  'KW1': 'Statistics and Information Technology Sector '
                                         '(Kuwait)',
                                  'KW2': 'Central Bank of Kuwait',
                                  'KW4': 'Ministry of Finance (Kuwait)',
                                  'KW99': 'Other competent National Authority (Kuwait)',
                                  'KY1': 'Department of Finance and Development / '
                                         'Statistical Office (Cayman Islands)',
                                  'KY2': 'Cayman Islands Monetary Authority',
                                  'KY99': 'Other competent National Authority (Cayman '
                                          'Islands)',
                                  'KZ1': 'National Statistical Agency / Ministry of Economy '
                                         'and Trade of the Republic of Kazakhstan',
                                  'KZ2': 'National Bank of the Republic of Kazakhstan',
                                  'KZ4': 'Ministry of Finance (Kazakhstan)',
                                  'KZ99': 'Other competent National Authority (Kazakhstan)',
                                  'LA2': 'Bank of the Lao P.D.R.',
                                  'LA4': 'Ministry of Finance (Lao Peoples Democratic '
                                         'Republic)',
                                  'LB1': 'Central Administration of Statistics (Lebanon)',
                                  'LB2': 'Banque du Liban (Lebanon)',
                                  'LB4': 'Ministere des finances (Lebanon)',
                                  'LB99': 'Other competent National Authority (Lebanon)',
                                  'LC1': 'Statistical Office (St. Lucia)',
                                  'LC2': 'Eastern Caribbean Central Bank (ECCB) (St. Lucia)',
                                  'LC4': 'Ministry of Finance, International Financial '
                                         'Services and Economic Affairs (St. Lucia)',
                                  'LI1': 'Amt fur Volkswirtschaft',
                                  'LI99': 'Other competent National Authority '
                                          '(Liechtenstein)',
                                  'LK2': 'Central Bank of Sri Lanka',
                                  'LR1': 'Ministry of Planning and Economic Affairs '
                                         '(Liberia)',
                                  'LR2': 'Central Bank of Liberia',
                                  'LR4': 'Ministry of Finance (Liberia)',
                                  'LR99': 'Other competent National Authority (Liberia)',
                                  'LS1': 'Bureau of Statistics (Lesotho)',
                                  'LS2': 'Central Bank of Lesotho',
                                  'LS4': 'Ministry of Finance (Lesotho)',
                                  'LT1': 'Lithuania, Department of Statistics',
                                  'LT2': 'Bank of Lithuania',
                                  'LT4': 'Ministry of Finance (Lithuania)',
                                  'LT99': 'Other competent National Authority (Lithuania)',
                                  'LU1': 'STATEC - Service central de la statistique et des '
                                         'etudes economiques du Luxembourg',
                                  'LU2': 'Banque centrale du Luxembourg',
                                  'LU99': 'Other competent National Authority (Luxembourg)',
                                  'LV1': 'Central Statistical Bureau of Latvia',
                                  'LV2': 'Bank of Latvia',
                                  'LV3': 'The Treasury of the Republic of Latvia',
                                  'LV99': 'Other competent National Authority (Latvia)',
                                  'LY1': 'The National Corporation for Information and '
                                         'Documentation (Libya)',
                                  'LY2': 'Central Bank of Libya',
                                  'LY3': 'General Peoples Secretariat of the Treasury '
                                         '(Libya)',
                                  'LY4': 'General Directorate for Economic and Social '
                                         'Planning (Libya)',
                                  'LY5': 'The National Corporation for Information and '
                                         'Documentation (Libya)',
                                  'LY99': 'Other competent National Authority (Libya)',
                                  'MA1': 'Ministere de la Prevision Economique et du Plan '
                                         '(Morocco)',
                                  'MA2': 'Bank Al-Maghrib (Morocco)',
                                  'MA4': 'Ministere de l`Economie, des Finances, de la '
                                         'Privatisation et du Tourisme (Morocco)',
                                  'MA5': 'Office des Changes (Morocco)',
                                  'MA99': 'Other competent National Authority (Morocco)',
                                  'MC1': 'Statistical Office (Monaco)',
                                  'MC99': 'Other competent National Authority (Monaco)',
                                  'MD1': 'State Depart. of Statist. of the Rep. of Moldova',
                                  'MD2': 'National Bank of Moldova',
                                  'MD4': 'Ministry of Finance (Moldova)',
                                  'MD99': 'Other competent National Authority (Moldova)',
                                  'ME1': 'Statistical Office (Montenegro)',
                                  'ME2': 'Central Bank of Montenegro',
                                  'MG1': 'INSTAT/Exchanges Commerciaux et des Services '
                                         '(Madagascar)',
                                  'MG2': 'Banque Centrale de Madagascar',
                                  'MG4': 'Ministere des finances de l`Economie (Madagascar)',
                                  'MG99': 'Other competent National Authority (Madagascar)',
                                  'MH4': 'Ministry of Finance (Marshall Islands, Rep)',
                                  'MK1': 'State Statistical Office (Macedonia)',
                                  'MK2': 'National Bank of the Republic of Macedonia',
                                  'MK4': 'Ministry of Finance (Macedonia)',
                                  'MK99': 'Other competent National Authority (Macedonia, '
                                          'FYR)',
                                  'ML1': 'Direction Nationale de la Statistique et de '
                                         'l`Informatique (DNSI) (Mali)',
                                  'ML2': 'Banque Centrale des Etats de l`Afrique de l`Ouest '
                                         '(BCEAO) (Mali)',
                                  'ML4': 'Ministere des Finances et du Commerce (Mali)',
                                  'ML99': 'Other competent National Authority (Mali)',
                                  'MM1': 'Central Statistical Organization (Myanmar)',
                                  'MM2': 'Central Bank of Myanmar',
                                  'MM4': 'Ministry of Finance and Revenue (Myanmar)',
                                  'MM99': 'Other competent National Authority (Myanmar)',
                                  'MN1': 'National Statistical Office (Mongolia)',
                                  'MN2': 'Bank of Mongolia',
                                  'MN4': 'Ministry of Finance and Economy (Mongolia)',
                                  'MN99': 'Other competent National Authority (Mongolia)',
                                  'MO1': 'Statistics and Census Department (China, P.R. '
                                         'Macao)',
                                  'MO2': 'Monetary Authority of Macau (China, P.R. Macao)',
                                  'MO3': 'Revenue Bureau of Macao',
                                  'MO4': 'Departamento de Estudos e Planeamento Financeiro '
                                         '(China, P.R. Macao)',
                                  'MO99': 'Other competent National Authority (China,P.R., '
                                          'Macao)',
                                  'MQ1': 'Department of Statistics (Martinique)',
                                  'MQ99': 'Other competent National Authority (Martinique)',
                                  'MR1': 'Department of Statistics and Economic Studies '
                                         '(Mauritania)',
                                  'MR2': 'Banque Centrale de Mauritanie',
                                  'MR3': 'Ministere du Plan (Mauritania)',
                                  'MR4': 'Ministere des Finances (Mauritania)',
                                  'MT1': 'Malta - Central Office of Statistics',
                                  'MT2': 'Central Bank of Malta',
                                  'MT4': 'Ministry of Finance (Malta)',
                                  'MT97': 'Malta Maritime Authority',
                                  'MT98': 'Malta International Airport',
                                  'MT99': 'Other competent National Authority (Malta)',
                                  'MU1': 'Central Statistical Office (Mauritius)',
                                  'MU2': 'Bank of Mauritius',
                                  'MU99': 'Other competent National Authority (Mauritius)',
                                  'MV2': 'Maldives Monetary Authority (Maldives)',
                                  'MV3': 'Ministry of Planning and Development (Maldives)',
                                  'MV4': 'Ministry of Finance and Treasury (Maldives)',
                                  'MW1': 'National Statistical Office (Malawi)',
                                  'MW2': 'Reserve Bank of Malawi',
                                  'MW4': 'Ministry of Finance (Malawi)',
                                  'MW99': 'Other competent National Authority (Malawi)',
                                  'MX1': 'Instituto Nacional de Estadisticas (INEGI) '
                                         '(Mexico)',
                                  'MX2': 'Banco de Mexico',
                                  'MX4': 'Secretaria de Hacienda y Credito Publico (Mexico)',
                                  'MX99': 'Other competent National Authority (Mexico)',
                                  'MY1': 'Department of Statistics Malaysia',
                                  'MY2': 'Bank Negara Malaysia',
                                  'MY99': 'Other competent National Authority (Malaysia)',
                                  'MZ1': 'Direccao Nacional de Estatistica (Mozambique)',
                                  'MZ2': 'Banco de Mocambique',
                                  'MZ4': 'Ministry of Planning and Finance (Mozambique)',
                                  'MZ99': 'Other competent National Authority (Mozambique)',
                                  'NA1': 'Central Bureau of Statistics (Namibia)',
                                  'NA2': 'Bank of Namibia',
                                  'NA4': 'Ministry of Finance (Namibia)',
                                  'NC1': 'Institut Territorial de la Statistique et des '
                                         'Etudes Economiques (New Caledonia)',
                                  'NC99': 'Other competent National Authority (French '
                                          'Territories, New Caledonia)',
                                  'NE2': 'Banque Centrale des Etats de l`Afrique de l`Ouest '
                                         '(BCEAO) (Niger)',
                                  'NE3': 'Ministere du Plan (Niger)',
                                  'NE4': 'Ministere des Finances (Niger)',
                                  'NG1': 'Federal Office of Statistics (Nigeria)',
                                  'NG2': 'Central Bank of Nigeria',
                                  'NG4': 'Federal Ministry of Finance (Nigeria)',
                                  'NG99': 'Other competent National Authority (Nigeria)',
                                  'NI2': 'Banco Central de Nicaragua',
                                  'NI4': 'Ministerio de Hacienda y Credito Publico '
                                         '(Nicaragua)',
                                  'NL1': 'Central Bureau voor de Statistiek (Netherlands)',
                                  'NL2': 'Nederlandse Bank (Netherlands)',
                                  'NL4': 'Ministry of Finance (Netherlands)',
                                  'NL99': 'Other competent National Authority (Netherlands)',
                                  'NO1': 'Statistics Norway',
                                  'NO2': 'Norges Bank (Norway)',
                                  'NO98': 'Avinor (Civil Aviation Administration)',
                                  'NO99': 'Other competent National Authority (Norway)',
                                  'NP1': 'Central Bureau of Statistics (Nepal)',
                                  'NP2': 'Nepal Rastra Bank',
                                  'NP4': 'Ministry of Finance (Nepal)',
                                  'NR1': 'Nauru Bureau of Statistics (Nauru)',
                                  'NR4': 'Ministry of Finance (Nauru)',
                                  'NR99': 'Other competent National Authority (Nauru)',
                                  'NU1': 'Statistics Offie Niue',
                                  'NZ1': 'Statistics New Zealand',
                                  'NZ2': 'Reserve Bank of New Zealand',
                                  'NZ99': 'Other competent National Authority (New Zealand)',
                                  'OM2': 'Central Bank of Oman',
                                  'OM4': 'Ministry of Finance (Oman)',
                                  'PA1': 'Directorate of Statistics and Census (Panama)',
                                  'PA2': 'Banco Nacional de Panama',
                                  'PA3': 'Office of the Controller General (Panama)',
                                  'PA6': 'Superintendencia de Bancos (Panama)',
                                  'PE2': 'Banco Central de Reserva del Peru',
                                  'PE4': 'Ministerio de Economia y Finanzas (Peru)',
                                  'PG1': 'National Statistical Office (Papua New Guinea)',
                                  'PG2': 'Bank of Papua New Guinea',
                                  'PG99': 'Other competent National Authority (Papua New '
                                          'Guinea)',
                                  'PH2': 'Central Bank of the Philippines',
                                  'PH3': 'Bureau of the Treasury (Philippines)',
                                  'PK1': 'Federal Bureau of Statistics (Pakistan)',
                                  'PK2': 'State Bank of Pakistan',
                                  'PK4': 'Ministry of Finance and Revenue (Pakistan)',
                                  'PK99': 'Other competent National Authority (Pakistan)',
                                  'PL1': 'Central Statistical Office of Poland',
                                  'PL2': 'Bank of Poland',
                                  'PL4': 'Ministry of Finance (Poland)',
                                  'PL99': 'Other competent National Authority (Poland)',
                                  'PS1': 'Palestinian Central Bureau of Statistics',
                                  'PS2': 'Palestine Monetary Authority',
                                  'PS99': 'Other competent National Authority (West Bank '
                                          'and Gaza)',
                                  'PT1': 'Instituto Nacional de Estatistica (Portugal)',
                                  'PT2': 'Banco de Portugal (Portugal)',
                                  'PT3': 'Direccao Geral do Orcamento (DGO) (Portugal)',
                                  'PT4': 'Ministerio Das Financas (Portugal)',
                                  'PT99': 'Other competent National Authority (Portugal)',
                                  'PW1': 'Statistical office (Palau)',
                                  'PW99': 'Other competent National Authority (Palau)',
                                  'PY2': 'Banco Central del Paraguay',
                                  'PY4': 'Ministerio de Hacienda (Paraguay)',
                                  'QA2': 'Qatar Central Bank',
                                  'QA3': 'Customs Department (Qatar)',
                                  'QA4': 'Ministry of Finance, Economy and Commerce (Qatar)',
                                  'RO1': 'Romania, National Commission for Statistics',
                                  'RO2': 'National Bank of Romania',
                                  'RO4': 'Ministere des Finances Public (Romania)',
                                  'RO99': 'Other competent National Authority (Romania)',
                                  'RS1': 'Statistical Office of the Republic of Serbia',
                                  'RS2': 'National Bank of Serbia (NBS) (Serbia, Rep. of)',
                                  'RU1': 'State Committee of the Russian Federation on '
                                         'Statistics',
                                  'RU2': 'Central Bank of Russian Federation',
                                  'RU3': 'State Customs Committee of the Russian Federation',
                                  'RU4': 'Ministry of Finance (Russian Federation)',
                                  'RU99': 'Other competent National Authority (Russian '
                                          'Federation)',
                                  'RW1': 'General Office of Statistics (Rwanda)',
                                  'RW2': 'Banque Nationale Du Rwanda',
                                  'RW4': 'Ministere des Finances et Planification Economie '
                                         '(Rwanda)',
                                  'SA1': 'Central Department of Statistics (Saudi Arabia)',
                                  'SA2': 'Saudi Arabian Monetary Agency',
                                  'SA4': 'Ministry of Finance (Saudi Arabia)',
                                  'SA99': 'Other competent National Authority (Saudi Arabia)',
                                  'SB1': 'Statistical Office (Solomon Islands)',
                                  'SB2': 'Central Bank of Solomon Islands',
                                  'SB4': 'Ministry of Finance and Treasury (Solomon Islands)',
                                  'SC2': 'Central Bank of Seychelles',
                                  'SC4': 'Ministry of Finance (Seychelles)',
                                  'SC6': 'Ministry of Administration and Manpower, '
                                         'Management and Information Systems Division '
                                         '(Seychelles)',
                                  'SD1': 'Central Bureau of Statistics (Sudan)',
                                  'SD2': 'Bank of Sudan',
                                  'SD4': 'Ministry of Finance and National Economy (Sudan)',
                                  'SD99': 'Other competent National Authority (Sudan)',
                                  'SE1': 'Statistics Sweden (Sweden)',
                                  'SE2': 'Sveriges Riksbank (Sweden)',
                                  'SE3': 'Sika Swedish Institute for Transport and '
                                         'Communications Analysis',
                                  'SE4': 'Banverket (National Rail Administration) Sweden',
                                  'SE5': 'National Institute of Economic Research (Sweden)',
                                  'SE99': 'Other competent National Authority (Sweden)',
                                  'SG1': 'Ministry of Trade and Industry / Department of '
                                         'Statistics (Singapore)',
                                  'SG2': 'Monetary Authority of Singapore',
                                  'SG3': 'International Enterprise Singapore',
                                  'SG4': 'Ministry of Finance (Singapore)',
                                  'SG99': 'Other competent National Authority (Singapore)',
                                  'SH1': 'Saint Helena Statistical Office',
                                  'SI1': 'Statistical Office of the Republic of Slovenia',
                                  'SI2': 'Bank of Slovenia',
                                  'SI4': 'Ministry of Finance (Slovenia)',
                                  'SI99': 'Other competent National Authority (Slovenia)',
                                  'SK1': 'Statistical Office of the Slovak Republic',
                                  'SK2': 'National Bank of Slovakia',
                                  'SK4': 'Ministry of Finance of the Slovak Republic',
                                  'SK99': 'Other competent National Authority (Slovak '
                                          'Republic)',
                                  'SL2': 'Bank of Sierra Leone',
                                  'SM1': 'Office of Economic Planning and Data Processing '
                                         'Center and Statistics (San Marino)',
                                  'SM2': 'Instituto di Credito Sammarinese / Central Bank '
                                         '(San Marino)',
                                  'SM4': 'Ministry of Finance and Budget (San Marino)',
                                  'SN1': 'Direction de la Prevision et de la Statistique '
                                         '(Senegal)',
                                  'SN2': 'Banque Centrale des Etats de l`Afrique de l`Ouest '
                                         '(BCEAO) (Senegal)',
                                  'SN4': 'Ministere de l`Economie et des Finances (Senegal)',
                                  'SN99': 'Other competent National Authority (Senegal)',
                                  'SO2': 'Central Bank of Somalia',
                                  'SR1': 'General Bureau of Statistics (Suriname)',
                                  'SR2': 'Centrale Bank van Suriname',
                                  'SR4': 'Ministry of Finance (Suriname)',
                                  'SR99': 'Other competent National Authority (Suriname)',
                                  'SS1': 'National Bureau of Statistics (South Sudan)',
                                  'SS2': 'Central bank of South Sudan',
                                  'SS99': 'Other competent National Authority (South Sudan)',
                                  'ST2': 'Banco Central de Sao Tome e Principe',
                                  'ST4': 'Ministry of Planning and Financing (Sao Tome and '
                                         'Principe)',
                                  'SV2': 'Banco Central de Reserva de El Salvador',
                                  'SV4': 'Ministerio de Hacienda (El Salvador)',
                                  'SX1': 'Bureau for Statistics Sint Maarten',
                                  'SX99': 'Other competent National Authority (Sint Maarten)',
                                  'SY1': 'Central Bureau of Statistics (Syria Arab Rep.)',
                                  'SY2': 'Central Bank of Syria',
                                  'SY4': 'Ministry of Finance (Syrian Arab Rep.)',
                                  'SY99': 'Other competent National Authority (Syrian Arab '
                                          'Republic)',
                                  'SZ1': 'Central Statistical Office (Swaziland)',
                                  'SZ2': 'Central Bank of Swaziland',
                                  'SZ4': 'Ministry of Finance (Swaziland)',
                                  'TC4': 'Ministry of Finance (Turks and Caicos)',
                                  'TC99': 'Other competent National Authority (Turks and '
                                          'Caicos)',
                                  'TD1': 'Institut de la Statistique (INSDEE) (Chad)',
                                  'TD2': 'Banque des Etats de l`Afrique Centrale (BEAC) '
                                         '(Chad)',
                                  'TD4': 'Ministere des finances (Chad)',
                                  'TD99': 'Other competent National Authority (Chad)',
                                  'TG2': 'Banque Centrale des Etats de l`Afrique de l`Ouest '
                                         '(BCEAO) (Togo)',
                                  'TG3': 'Ministere du Plan (Togo)',
                                  'TG4': 'Ministere de l`Economie des Finances (Togo)',
                                  'TH2': 'Bank of Thailand',
                                  'TH4': 'Ministry of Finance (Thailand)',
                                  'TH5': 'National Economic and Social Development Board '
                                         '(Thailand)',
                                  'TJ1': 'State Statistical Agency of Tajikistan',
                                  'TJ2': 'National Bank of Tajikistan',
                                  'TJ4': 'Ministry of Finance (Tajikistan)',
                                  'TJ99': 'Other competent National Authority (Tajikistan)',
                                  'TL1': 'Statistical Office (Timor Leste)',
                                  'TL2': 'Banco Central de Timor-Leste',
                                  'TL4': 'Ministry of Finance (Timor-Leste)',
                                  'TL99': 'Other competent National Authority (Timor-Leste)',
                                  'TM1': 'National Institute of State Statistics and '
                                         'Information (Turkmenistan)',
                                  'TM2': 'Central Bank of Turkmenistan',
                                  'TM4': 'Ministry of Economy and Finance (Turkmenistan)',
                                  'TM99': 'Other competent National Authority (Turkmenistan)',
                                  'TN1': 'National Institute of Statistics (Tunisia)',
                                  'TN2': 'Banque centrale de Tunisie',
                                  'TN4': 'Ministere des Finances (Tunisia)',
                                  'TO1': 'Statistics Department (Tongo)',
                                  'TO2': 'National Reserve Bank of Tonga',
                                  'TO4': 'Ministry of Finance (Tongo)',
                                  'TO99': 'Other competent National Authority (Tonga)',
                                  'TR1': 'State Institute of Statistics (Turkey)',
                                  'TR2': 'Central Bank of the Republic of Turkey',
                                  'TR3': 'Hazine Mustesarligi (Turkish Treasury)',
                                  'TR98': 'State Airports Authority',
                                  'TR99': 'Other competent National Authority (Turkey)',
                                  'TST': 'Internal ECB recipient for automatic and filtered '
                                         'mapping ECB to BIS series keys of data files sent '
                                         'to ESCB',
                                  'TT1': 'Central Statistical Office (Trinidad and Tobago)',
                                  'TT2': 'Central Bank of Trinidad and Tobago',
                                  'TT4': 'Ministry of Finance (Trinidad and Tobago)',
                                  'TV1': 'Tuvalu Statistics',
                                  'TW2': 'Central Bank of China, Taipei',
                                  'TZ1': 'Central Statistical Bureau (Tanzania)',
                                  'TZ2': 'Bank of Tanzania',
                                  'TZ4': 'Ministry of Finance (Tanzania)',
                                  'TZ99': 'Other competent National Authority (Tanzania)',
                                  'U22': 'Central banks belonging to the Euro area',
                                  'U32': 'EU central banks not belonging to the Euro area',
                                  'UA1': 'State Statistics Committee of Ukraine',
                                  'UA2': 'National Bank of Ukraine',
                                  'UA4': 'Ministry of Finance (Ukraine)',
                                  'UA99': 'Other competent National Authority (Ukraine)',
                                  'UG1': 'Uganda Bureau of Statistics',
                                  'UG2': 'Bank of Uganda',
                                  'UG4': 'Ministry of Finance, Planning and Economic '
                                         'Development (Uganda)',
                                  'UG99': 'Other competent National Authority (Uganda)',
                                  'US2': 'Federal Reserve Bank of New York (USA)',
                                  'US3': 'Board of Governors of the Federal Reserve System '
                                         '(USA)',
                                  'US4': 'U.S. Department of Treasury (USA)',
                                  'US5': 'U.S. Department of Commerce (USA)',
                                  'US6': 'Bureau of Labor Statistics',
                                  'US7': 'Bureau of Census',
                                  'US8': 'Bureau of Economic Analysis',
                                  'UY2': 'Banco Central del Uruguay',
                                  'UY4': 'Ministerio de Economia y Finanzas (Uruguay)',
                                  'UZ1': 'Goskomprognozstat (Uzbekistan)',
                                  'UZ3': 'Ministry of Economy (Uzbekistan)',
                                  'UZ4': 'Ministry of Finance (Uzbekistan)',
                                  'UZ99': 'Other competent National Authority (Uzbekistan)',
                                  'V12': 'EU 27 central banks',
                                  'V32': 'EU 28 central banks',
                                  'VC1': 'Statistical Unit (St. Vincent and Grenadines)',
                                  'VC2': 'Eastern Caribbean Central Bank (ECCB) (St. '
                                         'Vincent and Grenadines)',
                                  'VC4': 'Ministry of Finance and Planning (St. Vincent and '
                                         'the Grenadines)',
                                  'VE2': 'Banco Central de Venezuela',
                                  'VE4': 'Ministerio de Finanzas (Venezuela)',
                                  'VG99': 'Other competent National Authority (Virgin '
                                          'Islands, British)',
                                  'VI99': 'Other competent National Authority (Virgin '
                                          'Islands, US)',
                                  'VN1': 'General Statistics Office (Vietnam)',
                                  'VN2': 'State Bank of Vietnam',
                                  'VN99': 'Other competent National Authority (Vietnam)',
                                  'VU1': 'Statistical Office (Vanuatu)',
                                  'VU2': 'Reserve Bank of Vanuatu',
                                  'VU4': 'Ministry of Finance and Economic Management '
                                         '(Vanuatu)',
                                  'VU99': 'Other competent National Authority (Vanuatu)',
                                  'WS1': 'Department of Statistics (Samoa)',
                                  'WS2': 'Central Bank of Samoa',
                                  'WS4': 'Samoa Treasury Department',
                                  'WS99': 'Other competent National Authority (Samoa)',
                                  'XK1': 'Kosovo National statistical Office',
                                  'XK2': 'Kosovo National Bank',
                                  'XK4': 'Ministry of Finance (Kosovo)',
                                  'XK99': 'Other competent National Authority (Kosovo)',
                                  'YE1': 'Central Statistical Organization (Yemen)',
                                  'YE2': 'Central Bank of Yemen',
                                  'YE4': 'Ministry of Finance (Yemen)',
                                  'YE99': 'Other competent National Authority (Yemen, '
                                          'Republic of)',
                                  'ZA1': 'South African Reserve Service',
                                  'ZA2': 'South African Reserve Bank',
                                  'ZA3': 'Department of Customs and Excise (South Africa)',
                                  'ZA99': 'Other competent National Authority (South Africa)',
                                  'ZM1': 'Central Statistical Office (Zambia)',
                                  'ZM2': 'Bank of Zambia',
                                  'ZM99': 'Other competent National Authority (Zambia)',
                                  'ZW1': 'Central Statistical Office (Zimbabwe)',
                                  'ZW2': 'Reserve Bank of Zimbabwe',
                                  'ZW4': 'Ministry of Finance, Economic Planning and '
                                         'Development (Zimbabwe)',
                                  'ZW99': 'Other competent National Authority (Zimbabwe)',
                                  'ZZZ': 'Unspecified (e.g. any, dissemination, internal '
                                         'exchange etc)'},
                 'UNIT': {'ADF': 'Andorran franc (1-1 peg to the French franc)',
                          'ADP': 'Andorran peseta (1-1 peg to the Spanish peseta)',
                          'AED': 'United Arab Emirates dirham',
                          'AFA': 'Afghanistan afghani (old)',
                          'AFN': 'Afghanistan, Afghanis',
                          'ALL': 'Albanian lek',
                          'AMD': 'Armenian dram',
                          'ANG': 'Netherlands Antillean guilder',
                          'AOA': 'Angolan kwanza',
                          'AON': 'Angolan kwanza (old)',
                          'AOR': 'Angolan kwanza readjustado',
                          'ARS': 'Argentine peso',
                          'ATS': 'Austrian schilling',
                          'AUD': 'Australian dollar',
                          'AWG': 'Aruban florin/guilder',
                          'AZM': 'Azerbaijanian manat (old)',
                          'AZN': 'Azerbaijan, manats',
                          'BAM': 'Bosnia-Hezergovinian convertible mark',
                          'BBD': 'Barbados dollar',
                          'BDT': 'Bangladesh taka',
                          'BEF': 'Belgian franc',
                          'BEL': 'Belgian franc (financial)',
                          'BGL': 'Bulgarian lev (old)',
                          'BGN': 'Bulgarian lev',
                          'BHD': 'Bahraini dinar',
                          'BIF': 'Burundi franc',
                          'BMD': 'Bermudian dollar',
                          'BND': 'Brunei dollar',
                          'BOB': 'Bolivian boliviano',
                          'BRL': 'Brazilian real',
                          'BSD': 'Bahamas dollar',
                          'BTN': 'Bhutan ngultrum',
                          'BWP': 'Botswana pula',
                          'BYB': 'Belarussian rouble (old)',
                          'BYR': 'Belarus, Rubles',
                          'BZD': 'Belize dollar',
                          'CAD': 'Canadian dollar',
                          'CDF': 'Congo franc (ex Zaire)',
                          'CHE': 'WIR Euro',
                          'CHF': 'Swiss franc',
                          'CHW': 'WIR Franc',
                          'CLF': 'Chile Unidades de fomento',
                          'CLP': 'Chilean peso',
                          'CNH': 'Chinese yuan offshore',
                          'CNY': 'Chinese yuan renminbi',
                          'COP': 'Colombian peso',
                          'COU': 'Unidad de Valor Real',
                          'CRC': 'Costa Rican colon',
                          'CSD': 'Serbian dinar',
                          'CUC': 'Cuban convertible peso',
                          'CUP': 'Cuban peso',
                          'CVE': 'Cape Verde escudo',
                          'CYP': 'Cypriot pound',
                          'CZK': 'Czech koruna',
                          'DAYS': 'Days',
                          'DEM': 'German mark',
                          'DJF': 'Djibouti franc',
                          'DKK': 'Danish krone',
                          'DOP': 'Dominican peso',
                          'DZD': 'Algerian dinar',
                          'E0': 'Euro area changing composition vis-a-vis the EER-12 group '
                                'of trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, '
                                'CH, GB and US)',
                          'E1': 'Euro area-18 countries vis-a-vis the EER-20 group of '
                                'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                'GB, US, BG, CZ, LT, HU, PL, RO, HR and CN)',
                          'E2': 'Euro area-18 countries vis-a-vis the EER-19 group of '
                                'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                'GB, US, BG, CZ, LT, HU, PL, RO, and CN)',
                          'E3': 'Euro area-18 countries vis-a-vis the EER-39 group of '
                                'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                'GB, US, BG, CZ, LT, HU, PL, RO, CN, DZ, AR, BR, CL, HR, '
                                'IS, IN, ID, IL, MY, MX, MA, NZ, PH, RU, ZA, TW, TH, TR and '
                                'VE)',
                          'E4': 'Euro area-18 countries vis-a-vis the EER-12 group of '
                                'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                'GB and US)',
                          'E5': 'Euro area-19 countries vis-a-vis the EER-19 group of '
                                'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                'GB, US, BG, CZ, HU, PL, RO, HR and CN)',
                          'E6': 'Euro area-19 countries vis-a-vis the EER-18 group of '
                                'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                'GB, US, BG, CZ, HU, PL, RO, and CN)',
                          'E7': 'Euro area-19 countries vis-a-vis the EER-38 group of '
                                'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                'GB, US, BG, CZ, HU, PL, RO, CN, DZ, AR, BR, CL, HR, IS, '
                                'IN, ID, IL, MY, MX, MA, NZ, PH, RU, ZA, TW, TH, TR and VE)',
                          'E8': 'Euro area-19 countries vis-a-vis the EER-12 group of '
                                'trading partners (AU, CA, DK, HK, JP, NO, SG, KR, SE, CH, '
                                'GB and US)',
                          'ECS': 'Ecuador sucre',
                          'EEK': 'Estonian kroon',
                          'EGP': 'Egyptian pound',
                          'ERN': 'Erytrean nafka',
                          'ESP': 'Spanish peseta',
                          'ETB': 'Ethiopian birr',
                          'EUR': 'Euro',
                          'FIM': 'Finnish markka',
                          'FJD': 'Fiji dollar',
                          'FKP': 'Falkland Islands pound',
                          'FRF': 'French franc',
                          'FT': 'Full time equivalent',
                          'GBP': 'UK pound sterling',
                          'GEL': 'Georgian lari',
                          'GGP': 'Guernsey, Pounds',
                          'GHC': 'Ghana Cedi (old)',
                          'GHS': 'Ghana Cedi',
                          'GIP': 'Gibraltar pound',
                          'GMD': 'Gambian dalasi',
                          'GNF': 'Guinea franc',
                          'GR': 'Grams',
                          'GRD': 'Greek drachma',
                          'GTQ': 'Guatemalan quetzal',
                          'GWP': 'Guinea-Bissau Peso (old)',
                          'GYD': 'Guyanan dollar',
                          'H1': 'Euro area 18 currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                'ES, FI, AT, GR, SI, CY, EE, LV, MT, SK)',
                          'H10': 'ECB EER-38 group of currencies and Euro area (latest '
                                 'composition) currencies '
                                 '(FR,BE,LU,NL,DE,IT,IE,PT,ES,FI,AT,GR,SI,AU,CA,CN,DK,HK,JP,NO,SG,KR,SE,CH,GB,US,CY,CZ,EE,HU,LV,LT,MT,PL,SK,BG,RO,NZ,DZ,AR,BR,HR,IN,ID,IL,MY,MX,MA,PH,RU,ZA,TW,TH,TR,IS,CL,VE)',
                          'H11': 'ECB EER-19 group of currencies and Euro area (latest '
                                 'composition) currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                 'ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, SG, KR, '
                                 'SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, PL, SK, BG, '
                                 'RO, HR)',
                          'H2': 'ECB EER-12 group of currencies and Euro areas (latest '
                                'composition) currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                'ES, FI, AT, GR, SI, CY, EE, LV, MT, SK, AU, CA, CN, DK, '
                                'HK, JP, NO, SG, KR, SE, CH, GB, US)',
                          'H3': 'ECB EER-20 group of currencies and Euro areas (latest '
                                'composition) currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                'ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, SG, KR, '
                                'SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, PL, SK, BG, RO)',
                          'H36': 'European Commission IC-36 group of currencies (European '
                                 'Union 27 Member States, i.e. BE, DE, EE, GR, ES, FR, IE, '
                                 'IT, CY, LU, NL, MT, AT, PT, SI, SK, FI, BG, CZ, DK, LV, '
                                 'LT, HU, PL, RO, SE, GB, and US, AU, CA, JP, MX, NZ, NO, '
                                 'CH, TR)',
                          'H37': 'European Commission IC-37 group of currencies (European '
                                 'Union 28 Member States, i.e. BE, DE, EE, GR, ES, FR, IE, '
                                 'IT, CY, LU, NL, MT, AT, PT, SI, SK, FI, BG, CZ, DK, HR, '
                                 'LV, LT, HU, PL, RO, SE, GB, and US, AU, CA, JP, MX, NZ, '
                                 'NO, CH, TR)',
                          'H4': 'ECB EER-40 group of currencies and Euro areas (latest '
                                'composition) currencies '
                                '(FR,BE,LU,NL,DE,IT,IE,PT,ES,FI,AT,GR,SI,AU,CA,CN,DK,HK,JP,NO,SG,KR,SE,CH,GB,US,CY,CZ,EE,HU,LV,LT,MT,PL,SK,BG,RO,NZ,DZ,AR,BR,HR,IN,ID,IL,MY,MX,MA,PH,RU,ZA,TW,TH,TR,IS,CL,VE)',
                          'H42': 'European Commission IC-42 group of currencies (European '
                                 'Union 28 Member States, i.e. '
                                 'BE,DE,EE,GR,ES,FR,IE,IT,CY,LU,NL,MT,AT,PT,SI,SK,FI,BG,CZ,DK,HR,LV,LT,HU,PL,RO,SE,GB, '
                                 'and US,AU,CA,JP,MX,NZ,NO,CH,TR,KR,CN,HK,RU,BR)',
                          'H5': 'ECB EER-21 group of currencies and Euro areas (latest '
                                'composition) currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                'ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, SG, KR, '
                                'SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, PL, SK, BG, '
                                'RO, HR)',
                          'H6': 'ECB EER-12 group of currencies and Euro areas (latest '
                                'composition) currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                'ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, SG, KR, '
                                'SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, PL, SK, BG, '
                                'RO, HR, TR and RU)',
                          'H7': 'Euro area 19 currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                'ES, FI, AT, GR, SI, CY, EE, LT, LV, MT, SK)',
                          'H8': 'ECB EER-12 group of currencies and Euro area (latest '
                                'composition) currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                'ES, FI, AT, GR, SI, CY, EE, LT, LV, MT, SK, AU, CA, CN, '
                                'DK, HK, JP, NO, SG, KR, SE, CH, GB, US)',
                          'H9': 'ECB EER-18 group of currencies and Euro area (latest '
                                'composition) currencies (FR, BE, LU, NL, DE, IT, IE, PT, '
                                'ES, FI, AT, GR, SI, AU, CA, CN, DK, HK, JP, NO, SG, KR, '
                                'SE, CH, GB, US, CY, CZ, EE, HU, LV, LT, MT, PL, SK, BG, RO)',
                          'HKD': 'Hong Kong dollar',
                          'HKQ': 'Hong Kong dollar (old)',
                          'HNL': 'Honduran lempira',
                          'HOURS': 'Hours',
                          'HR': 'Hours',
                          'HRK': 'Croatian kuna',
                          'HTG': 'Haitian gourde',
                          'HUF': 'Hungarian forint',
                          'HW': 'Hours worked',
                          'IDR': 'Indonesian rupiah',
                          'IEP': 'Irish pound',
                          'ILS': 'Israeli shekel',
                          'IMP': 'Isle of Man, Pounds',
                          'INR': 'Indian rupee',
                          'IQD': 'Iraqi dinar',
                          'IRR': 'Iranian rial',
                          'ISK': 'Iceland krona',
                          'ITL': 'Italian lira',
                          'IX': 'Index',
                          'JB': 'Jobs',
                          'JEP': 'Jersey, Pounds',
                          'JMD': 'Jamaican dollar',
                          'JOD': 'Jordanian dinar',
                          'JPY': 'Japanese yen',
                          'KES': 'Kenyan shilling',
                          'KG': 'Kilograms',
                          'KGS': 'Kyrgyzstan som',
                          'KHR': 'Kampuchean real (Cambodian)',
                          'KILO': 'Kilograms',
                          'KL': 'Kilolitres',
                          'KLITRE': 'Kilolitres',
                          'KMF': 'Comoros franc',
                          'KPW': 'Korean won (North)',
                          'KRW': 'Korean won (Republic)',
                          'KWD': 'Kuwait dinar',
                          'KYD': 'Cayman Islands dollar',
                          'KZT': 'Kazakstan tenge',
                          'LAK': 'Lao kip',
                          'LBP': 'Lebanese pound',
                          'LITRES': 'Litres',
                          'LKR': 'Sri Lanka rupee',
                          'LRD': 'Liberian dollar',
                          'LSL': 'Lesotho loti',
                          'LT': 'Litres',
                          'LTL': 'Lithuanian litas',
                          'LUF': 'Luxembourg franc',
                          'LVL': 'Latvian lats',
                          'LYD': 'Libyan dinar',
                          'MAD': 'Moroccan dirham',
                          'MD': 'Man Days',
                          'MDL': 'Moldovian leu',
                          'MGA': 'Madagascar, Ariary',
                          'MGF': 'Malagasy franc',
                          'MH': 'Months',
                          'MKD': 'Macedonian denar',
                          'MMK': 'Myanmar kyat',
                          'MNT': 'Mongolian tugrik',
                          'MONTHS': 'Months',
                          'MOP': 'Macau pataca',
                          'MQ': 'Square Metres',
                          'MRO': 'Mauritanian ouguiya',
                          'MTL': 'Maltese lira',
                          'MUR': 'Mauritius rupee',
                          'MVR': 'Maldive rufiyaa',
                          'MWK': 'Malawi kwacha',
                          'MXN': 'Mexican peso',
                          'MXP': 'Mexican peso (old)',
                          'MXV': 'Mexican Unidad de Inversion (UDI)',
                          'MY': 'Man Years',
                          'MYR': 'Malaysian ringgit',
                          'MZM': 'Mozambique metical (old)',
                          'MZN': 'Mozambique, Meticais',
                          'NAD': 'Namibian dollar',
                          'NATCUR': 'National currency',
                          'NGN': 'Nigerian naira',
                          'NIO': 'Nicaraguan cordoba',
                          'NLG': 'Netherlands guilder',
                          'NOK': 'Norwegian krone',
                          'NPR': 'Nepaleese rupee',
                          'NZD': 'New Zealand dollar',
                          'OMR': 'Oman Sul rial',
                          'OUNCES': 'Ounces',
                          'OZ': 'Ounces',
                          'PA': 'Percent per annum',
                          'PAB': 'Panama balboa',
                          'PC': 'Percent',
                          'PCCH': 'Percentage change',
                          'PCPA': 'Percent per annum',
                          'PCT': 'Percentage change (code value to be discontinued)',
                          'PE': 'Euro, converted using purchasing power parities',
                          'PEN': 'Peru nuevo sol',
                          'PERS': 'Persons',
                          'PGK': 'Papua New Guinea kina',
                          'PHP': 'Philippine peso',
                          'PKR': 'Pakistan rupee',
                          'PLN': 'Polish zloty',
                          'PLZ': 'Polish zloty (old)',
                          'PM': 'Per thousand',
                          'PN': 'Pure number',
                          'PO': 'Points',
                          'POINTS': 'Points',
                          'PP': 'Purchasing power parities',
                          'PS': 'Persons',
                          'PT': 'Percent',
                          'PTE': 'Portugese escudo',
                          'PU': 'US dollar, converted using purchasing power parities',
                          'PURE_NUMB': 'Pure number',
                          'PYG': 'Paraguay guarani',
                          'QAR': 'Qatari rial',
                          'RO': 'Ratio',
                          'ROL': 'Romanian leu (old)',
                          'RON': 'Romanian leu',
                          'RSD': 'Serbian dinar',
                          'RT': 'Interest rate',
                          'RUB': 'Rouble',
                          'RUR': 'Russian ruble (old)',
                          'RWF': 'Rwanda franc',
                          'SAR': 'Saudi riyal',
                          'SBD': 'Solomon Islands dollar',
                          'SCR': 'Seychelles rupee',
                          'SDD': 'Sudanese dinar',
                          'SDG': 'Sudan, Dinars',
                          'SDP': 'Sudanese pound (old)',
                          'SEK': 'Swedish krona',
                          'SGD': 'Singapore dollar',
                          'SHP': 'St. Helena pound',
                          'SIT': 'Slovenian tolar',
                          'SKK': 'Slovak koruna',
                          'SLL': 'Sierra Leone leone',
                          'SOS': 'Somali shilling',
                          'SPL': 'Seborga, Luigini',
                          'SQ_M': 'Square Metres',
                          'SRD': 'Suriname, Dollars',
                          'SRG': 'Suriname guilder',
                          'SSP': 'South sudanese pound',
                          'STD': 'Sao Tome and Principe dobra',
                          'SVC': 'El Salvador colon',
                          'SYP': 'Syrian pound',
                          'SZL': 'Swaziland lilangeni',
                          'THB': 'Thai bhat',
                          'TJR': 'Tajikistan rouble',
                          'TJS': 'Tajikistan, Somoni',
                          'TMM': 'Turkmenistan manat (old)',
                          'TMT': 'Turkmenistan manat',
                          'TN': 'Tonnes',
                          'TND': 'Tunisian dinar',
                          'TONNES': 'Tonnes',
                          'TOP': 'Tongan paanga',
                          'TPE': 'East Timor escudo',
                          'TRL': 'Turkish lira (old)',
                          'TRY': 'Turkish lira',
                          'TTD': 'Trinidad and Tobago dollar',
                          'TVD': 'Tuvalu, Tuvalu Dollars',
                          'TWD': 'New Taiwan dollar',
                          'TZS': 'Tanzania shilling',
                          'UAH': 'Ukraine hryvnia',
                          'UGX': 'Uganda Shilling',
                          'UNITS': 'Unit described in title',
                          'USD': 'US dollar',
                          'UT': 'Unit described in title',
                          'UYI': 'Uruguay Peso en Unidades Indexadas',
                          'UYU': 'Uruguayan peso',
                          'UZS': 'Uzbekistan sum',
                          'VEB': 'Venezuela bolivar (old)',
                          'VEF': 'Venezuela bolivar',
                          'VND': 'Vietnamese dong',
                          'VUV': 'Vanuatu vatu',
                          'WST': 'Samoan tala',
                          'X1': 'All currencies except national currency',
                          'X2': 'All currencies except USD',
                          'X3': 'All currencies except EUR',
                          'X4': 'All currencies except EUR, USD',
                          'X5': 'All currencies except EUR, JPY, USD',
                          'X6': 'All currencies except EUR, CHF, GBP, JPY, USD',
                          'X7': 'All currencies except EUR, USD, JPY, GBP, CHF, domestic '
                                'currency',
                          'XAF': 'CFA franc / BEAC',
                          'XAG': 'Silver',
                          'XAU': 'Gold in units of grams',
                          'XBA': 'European composite unit',
                          'XBB': 'European Monetary unit EC-6',
                          'XBC': 'European Unit of Account 9 (E.U.A.-9)',
                          'XBD': 'European Unit of Account 17 (E.U.A.-17)',
                          'XCD': 'Eastern Caribbean dollar',
                          'XDB': 'Currencies included in the SDR basket, gold and SDRs',
                          'XDC': 'Domestic currency (incl. conversion to current currency '
                                 'made using a fixed parity)',
                          'XDM': 'Domestic currency (incl. conversion to current currency '
                                 'made using market exchange rate)',
                          'XDO': 'Other currencies not included in the SDR basket, exc. '
                                 'gold and SDRs',
                          'XDR': 'Special Drawing Rights (S.D.R.)',
                          'XEU': 'European Currency Unit (E.C.U.)',
                          'XFO': 'Gold-Franc',
                          'XFU': 'UIC-Franc',
                          'XGO': 'Gold fine troy ounces',
                          'XNC': 'Euro area non-participating foreign currency',
                          'XOF': 'CFA franc / BCEAO',
                          'XPC': 'Euro area participating foreign currency',
                          'XPD': 'Palladium Ounces',
                          'XPF': 'Pacific franc',
                          'XPT': 'Platinum, Ounces',
                          'XRH': 'Rhodium',
                          'XSU': 'Sucre',
                          'XTS': 'Codes specifically reserved for testing purposes',
                          'XUA': 'ADB Unit of Account',
                          'XXX': 'Transactions where no currency is involved',
                          'YEARS': 'Years',
                          'YER': 'Yemeni rial',
                          'YR': 'Years',
                          'YUM': 'Yugoslav dinar',
                          'ZAR': 'South African rand',
                          'ZMK': 'Zambian kwacha',
                          'ZMW': 'New zambian kwacha',
                          'ZWD': 'Zimbabwe dollar',
                          'ZWL': 'Fourth Zimbabwe dollar',
                          'ZWN': 'Zimbabwe, Zimbabwe Dollars',
                          'ZWR': 'Third Zimbabwe dollar',
                          '_T': 'All currencies of denomination',
                          '_X': 'Not specified',
                          '_Z': 'Not applicable'},
                 'UNIT_MULT': {'-2': 'Hundredth',
                               '0': 'Units',
                               '1': 'Tens',
                               '12': 'Trillions',
                               '15': 'Quadrillions',
                               '2': 'Hundreds',
                               '3': 'Thousands',
                               '4': 'Tens of thousands',
                               '5': 'Hundreds of thousands',
                               '6': 'Millions',
                               '9': 'Billions'}}
        self.assertEqual(sdmx.ecb.codes('EXR1') ,model)

if __name__ == '__main__':
    unittest.main()
                
