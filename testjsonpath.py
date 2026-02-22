import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

results = jsonpath.jsonpath(avaliacoes.json(), 'results')

#nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')

#print(nome)

nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')

print(nomes)