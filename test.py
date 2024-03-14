import PyPublicaties as pp

pubs=pp.retreive_publications(query_dict={'w.subrubriek': 'Stemmingen'}, max_records=1)

print(pubs[0].itemUrl[4])