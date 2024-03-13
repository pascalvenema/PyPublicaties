from .structure import OfficielePublicatie
from .webservice import ontsluit_handelingen

def retreive_publications(query_dict = {}, max_records = 10, start_record = 1):
    query_concatter = ' AND '
    query_part2 = ''
    for key, value in query_dict.items():
        query_part2 += f"{query_concatter}{key}={value}"
    
    root = ontsluit_handelingen(query_part2, start_record, max_records)
    
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
            ob = OfficielePublicatie.from_xml_element(record_data, namespaces)
            ops.append(ob)
            
    return ops
    
    
query_dict = {
    'w.subrubriek': 'Stemmingen'
}

publications = retreive_publications(query_dict=query_dict, max_records=100, start_record=1)