import requests
import xml.etree.ElementTree as ET

# Functie om handelingen te ontsluiten
# Deze functie voert een request uit naar de SRU API van de overheid en geeft de resultaten weer in de notebook
def ontsluit_handelingen(query_part2, startRecord=1, maximumRecords=10):
    
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
    
    # Als er een tweede deel voor de query is, voeg deze toe aan de originele query en vervang de query in de parameters
    if query_part2:
        params["query"] += query_part2
    
    # Voer de request uit
    response = requests.get(url, params=params)

    # Controleer of de request gelukt is
    if response.status_code == 200:
        # Zet de response om naar een XML object (bytes)
        xml_data = response.content

        # Parse de XML vanuit bytes naar een ElementTree object
        root = ET.fromstring(xml_data)
        
        # Return het ElementTree object
        return root
    else:
        print(f"Request failed with status code: {response.status_code}")