import PyPublicaties as pp

query_list = [
    'w.subrubriek=Stemmingen',
    'dt.identifier=h-tk-20192020-46-12'
]

pubs=pp.retreive_publications(query_list=query_list,max_records=1)

print(pubs[0].title[0])