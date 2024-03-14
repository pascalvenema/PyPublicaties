from sru import retrieve_ops_sru
from sftp import retrieve_ops_sftp

# STEP 1: Get ElementTrees
# For SRU 2.0: one big XML with all records.
# For SFTP: each record is a folder, with 'identifier' as folder name. Each folder contains: {identifier}.html.zip, {identifier}.odt, {identifier}.pdf, {identifier}.xml, metadata_owms.xml, metadata.xml

# STEP 2:

def retrieve_obs(method = 'sru', queryList = [], limit = 10, startRecord = 1):
    # Query is a list in a list
    # For example:
    # [
    #     ['title', '=', 'Wet op de Ruimtelijke Ordening'],
    #     ['date', '>', '2020-01-01']
    # ]
    
    ops = []


    if method=="sru":        
        ops = retrieve_ops_sru(queryList=queryList, maximumRecords=limit, startRecord=startRecord)
        number_of_results = retrieve_number_of_results_sru(queryList=queryList)
    
    elif method=="sftp":
        ops = retrieve_ops_sftp(queryList=queryList)
    
    
    return ops


queryList = [
    ['dcterms:identifier', '=', 'h-tk-20142015-13-14'],
    ['overheidwetgeving:subrubriek', '=', 'Stemmingen']
]

ops = retrieve_obs(queryList=queryList)

print(ops)