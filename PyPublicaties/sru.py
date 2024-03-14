import requests
import xml.etree.ElementTree as ET
from skeleton import OfficielePublicatie

# Functie om handelingen te ontsluiten
# Deze functie voert een request uit naar de SRU API van de overheid en geeft de resultaten weer in de notebook
def retrieve_ops_sru(queryList, maximumRecords=10, startRecord=1):
    # Connectiestring met basis parameters, waarbij al gefilterd wordt op 'officielepublicaties'
    url = "https://repository.overheid.nl/sru"
    params = {
    "operation": "searchRetrieve",
    "version": "2.0",
    "query": "c.product-area==officielepublicaties",  
    "startRecord": startRecord,
    "maximumRecords": maximumRecords,
    "recordSchema": "gzd"
    }
    
    def transform_query_to_cql_index(queryList):
        # Dict where key are the SRU-ouput values (which is the input), and where the values are the CQL index names
        # Refer to: https://data.overheid.nl/sites/default/files/dataset/d0cca537-44ea-48cf-9880-fa21e1a7058f/resources/Handleiding%2BSRU%2B2.0.pdf 
        # Page 16
        values = {
            'dcterms:identifier':	                        'dt.identifier',
            'dcterms:title':	                            'dt.title',
            'dcterms:type':	                                'dt.type',
            'dcterms:language':	                            'dt.language',
            'overheid:authority':	                        'ot.authority',
            'dcterms:creator':          	                'dt.creator',
            'dcterms:modified':         	                'dt.modified',
            'dcterms:temporal':              	            'dt.temporal',
            'dcterms:spatial':          	                'dt.spatial',
            'dcterms:alternative':          	            'dt.alternative',
            'dcterms:date':	                                'dt.date',
            'dcterms:hasVersion':       	                'dt.hasVersion',
            'dcterms:source':               	            'dt.source',
            'dcterms:requires': 	                        '',
            'dcterms:isPartOf':             	            'dt.isPartOf',
            'dcterms:isrequiredby':     	                'dt.isrequiredby',
            'dcterms:isreplacedby':                         'dt.isreplacedby',
            'dcterms:hasPart':              	            'dt.hasPart',
            'dcterms:subject':              	            'dt.subject',
            'dcterms:available':            	            'dt.available',
            'dcterms:abstract':             	            '',	 
            'dcterms:publisher':            	            '',
            'dcterms:issued':           	                'dt.issued',
            'dcterms:replaces':           	                '',
            'overheidwetgeving:aanhangsel':  	            'w.aanhangsel',
            'overheidwetgeving:aanhangselnummer':           'w.aanhangselnummer',
            'overheidwetgeving:adviesRvs':              	'w.adviesRvs',
            'overheidwetgeving:bedrijfsnaam':           	'w.bedrijfsnaam',
            'overheidwetgeving:behandeldDossier':	        'w.behandeldDossier',
            'overheidwetgeving:betreft':	                'w.betreft',
            'overheidwetgeving:betreftopschrift':       	'w.betreftopschrift',
            'overheidwetgeving:betreftRegeling':        	'w.betreftRegeling',
            'overheidwetgeving:bijlage':                	'w.bijlage',
            'overheidwetgeving:datumBrief':     	        'w.datumBrief',
            'overheidwetgeving:datumIndiening':     	    'w.datumIndiening',
            'overheidwetgeving:datumOndertekening':     	'w.datumOndertekening',
            'overheidwetgeving:datumOntvangst':         	'w.datumOntvangst',
            'overheidwetgeving:datumTotstandkoming':    	'w.datumTotstandkoming',
            'overheidwetgeving:datumVergadering':       	'w.datumVergadering',
            'overheidwetgeving:deurwaardersdossier':    	'w.deurwaardersdossier',
            'overheidwetgeving:documentstatus':     	    'w.documentstatus',
            'overheidwetgeving:documenttitel':	            'w.documenttitel',
            'overheidwetgeving:dossiernummer':      	    'w.dossiernummer',
            'overheidwetgeving:dossiertitel':           	'w.dossiertitel',
            'overheidwetgeving:effectgebied':               'w.effectgebied',
            'overheidwetgeving:einddatum':              	'w.einddatum',
            'overheidwetgeving:datumEindeReactietermijn':	'w.datumEindeReactie',
            'overheidwetgeving:eindpagina':                 'w.eindpagina',
            'overheidwetgeving:externeBijlage':             'w.externeBijlage',
            'overheidwetgeving:gebiedsmarkering':           'w.gebiedsmarkering',
            'overheidwetgeving:gemeentenaam':               'w.gemeentenaam',
            'overheidwetgeving:geometrie':                  'w.locatiegebied',
            'overheidwetgeving:geometrie':                  'w.effectgebied',
            'overheidwetgeving:geometrielabel':             'w.geometrielabel',
            'overheidwetgeving:hectometernummer':           'w.hectometernummer',
            'overheidwetgeving:heeftMededeling':            'w.heeftMededeling',
            'overheidwetgeving:hoofddocument':              'w.hoofddocument',
            'overheidwetgeving:huisnummer':                 'w.huisnummer',
            'overheidwetgeving:huisletter':                 'w.huisletter',
            'overheidwetgeving:huisnummertoevoeging':       'w.huisnummertoevoeging',
            'overheidwetgeving:indiener':                   'w.indiener',
            'overheidwetgeving:handelingenitemnummer':      'w.handelingenitemnummer',
            'overheidwetgeving:jaargang':                   'w.jaargang',
            'overheidwetgeving:kadastraleSectie':           'w.kadastraleSectie',
            'overheidwetgeving:ketenid':                    'w.ketenid',
            'overheidwetgeving:ligtInGemeente':             'w.ligtInGemeente',
            'overheidwetgeving:ligtInProvincie':            'w.ligtInProvincie',
            'overheidwetgeving:materieelUitgewerkt':        'w.materieelUitgewerkt',
            'overheidwetgeving:mededelingOver':             'w.mededelingOver',
            'overheidwetgeving:ondernummer':                'w.ondernummer',
            'overheidwetgeving:ontvanger':                  'w.ontvanger',
            'overheidwetgeving:organisatietype':            'w.organisatietype',
            'overheidwetgeving:perceelnummer':              'w.perceelnummer',
            'overheidwetgeving:persoonsgegevens':           'w.persoonsgegevens',
            'overheidwetgeving:plaatsTotstandkoming':       'w.plaatsTotstandkoming',
            'overheidwetgeving:postcode':                   'w.postcode',
            'overheidwetgeving:postcodeHuisnummer':         'w.postcodeHuisnummer',
            'overheidwetgeving:provincie':                  'w.provincie',
            'overheidwetgeving:provincienaam':              'w.provincienaam',
            'overheidwetgeving:publicatienummer':           'w.publicatienummer',
            'overheidwetgeving:publicatienaam':             'w.publicatienaam',
            'overheidwetgeving:besluitReferendabiliteit':   'w.w.besluitReferendabili',
            'overheidwetgeving:referentienummer':           'w.referentienummer',
            'overheidwetgeving:rijkswetnummer':             'w.rijkswetnummer',
            'overheidwetgeving:bekendmakingBetreffendePlan':'w.bekendmakingBetreffendePlan',
            'overheidwetgeving:startdatum':                 'w.startdatum',
            'overheidwetgeving:startpagina':                'w.startpagina',
            'overheidwetgeving:straatnaam':                 'w.straatnaam',
            'overheidwetgeving:subrubriek':                 'w.subrubriek',
            'overheidwetgeving:sysyear':                    'w.sysyear',
            'overheidwetgeving:sysnumber':                  'w.sysnumber',
            'overheidwetgeving:sysseqnumber':               'w.sysseqnumber',
            'overheidwetgeving:terinzageleggingBG':         'w.terinzageleggingBG',
            'overheidwetgeving:terinzageleggingOP':         'w.terinzageleggingOP',
            'overheidwetgeving:typeVerkeersbesluit':        'w.typeVerkeersbesluit',
            'overheidwetgeving:verdragnummer':              'w.verdragnummer',
            'overheidwetgeving:vereisteVanBesluit':         'w.vereisteVanBesluit',
            'overheidwetgeving:vergaderjaar':               'w.vergaderjaar',
            'overheidwetgeving:verkeersbordcode':           'w.verkeersbordcode',
            'overheidwetgeving:versieinformatie':           'w.versieinformatie',
            'overheidwetgeving:versienummer':               'w.versienummer',
            'overheidwetgeving:vraagnummer':                'w.vraagnummer',
            'overheidwetgeving:waterschapsnaam':            'w.waterschapsnaam',
            'overheidwetgeving:wegcategorie':               'w.wegcategorie',
            'overheidwetgeving:weggebruiker':               'w.weggebruiker',
            'overheidwetgeving:wegnummer':                  'w.wegnummer',
            'overheidwetgeving:woonplaats':                 'w.woonplaats',
            'overheidwetgeving:zittingsdatum':              'w.zittingsdatum',
            'c:product-area':                               'c.product-area',
            'c:content-area':                               'c.content-area',
            'cd:datumTijdstipWijzigingWork':                'cd.datumTijdstipWijzigingWork',
            'cd:datumTijdstipWijzigingExpression':          'cd.datumTijdstipWijzigingExpression',
            'gzd:url':                                      '',
            'gzd:prefferedUrl':                             '',
            'gzd:itemUrl':                                  '',
            'gzd:timestamp':                                '',
            '':                                             'cql.textAndIndexes'
            }
        
        for query in queryList:
            query[0] = values[query[0]]
            
        return queryList
    
    transform_query_to_cql_index(queryList)
    
    # Als er een tweede deel voor de query is, voeg deze toe aan de originele query en vervang de query in de parameters
    queryConcatter = ' AND '
    query = ''
    while len(queryList) > 0:
        query += f"{queryConcatter}{queryList[0][0]}{queryList[0][1]}{queryList[0][2]}"
        queryList.pop(0)
    
    params['query'] += query
    
    # Voer de request uit
    response = requests.get(url, params=params)

    # Controleer of de request gelukt is
    root = None
    if response.status_code == 200:
        # Zet de response om naar een XML object (bytes)
        xml_data = response.content

        # Parse de XML vanuit bytes naar een ElementTree object
        root = ET.fromstring(xml_data)
        
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    def from_xml_element(instance, element: ET.Element, namespaces: dict):
        """
        Adapted to work with an instance of `OfficielePublicatie`.
        
        Parameters:
        - instance: An instance of `OfficielePublicatie`.
        - element: An ET.Element object to parse.
        - namespaces: A dictionary of XML namespaces.
        """
        for child in element.findall('.//*', namespaces):
            tag = parse_namespaced_tag(child.tag)

            if tag not in instance.__dict__:
                continue

            if child.attrib:
                key, value = list(child.attrib.items())[0]
                value_dict = {value: child.text.strip() if child.text else ""}
                instance.__dict__[tag].append(value_dict)
            else:
                instance.__dict__[tag].append(child.text.strip() if child.text else "")
        return instance

    def parse_namespaced_tag(tag: str) -> str:
        """Parse a namespaced tag and return the tag without its namespace."""
        return tag.split('}', 1)[-1] if '}' in tag else tag
        
    namespaces = {
        'sru': "http://docs.oasis-open.org/ns/search-ws/sruResponse",
        'gzd': "http://standaarden.overheid.nl/sru"
        }    
        
    ops = []

    
    # Loop door iedere record in de records container
    for record in root.findall('.//sru:records/sru:record', namespaces):
        # Genest in <sru:recordData>
        record_data = record.find('.//sru:recordData', namespaces)
        if record_data is not None:
            op = from_xml_element(OfficielePublicatie(), record_data, namespaces)
            ops.append(op)
    
    
    return ops
     
def retrieve_number_of_results_sru():
    