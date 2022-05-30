import requests

servers = {
    "triple_host": "http://172.18.0.101:5000/api/v1/",
    "stanford_host": "http://172.18.0.102:9000",
    "neo4j_host": "neo4j://172.18.0.103:7687",
    "neo4j_user": "neo4j",
    "neo4j_pass": "test"
}

services = {
    'plain_all': servers['triple_host'] + 'plain',
    'rdf_dbpedia': servers['triple_host'] + 'rdf/DBPEDIA',
    'csv': servers['triple_host'] + 'save/csv'
    'n-triples': servers['triple_host'] + 'save/ntriples'
    'turttle': servers['triple_host'] + 'save/turttle'
    'json-ld': servers['triple_host'] + 'save/json'
    'neo4j': servers['triple_host'] + 'save/NEO4J'
}

headers = {
    'Content-type':'application/json' 
}


def executeRequest(operation, url, headers, data):
	result = dict()
	try:
		response = ''
		if(operation == 'POST'):
			response = requests.post(url, data=str(data), headers=headers, timeout=1000)
		elif(operation == 'GET'):
			response = requests.get(url, timeout=1000)
		#print(response)
		response.raise_for_status()
		result = response.json()
	# Code here will only run if the request is successful
	except requests.exceptions.HTTPError as errh:
		result = errh
	except requests.exceptions.ConnectionError as errc:
		result = errc
	except requests.exceptions.Timeout as errt:
		result = errt
	except requests.exceptions.RequestException as err:
		result = err
	return result
