import requests

#GET avaliações

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

#GET avaliacão

avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/4/')

#print(avaliacao.json())

#GET Cursos

headers = {'Authorization': 'Token 947e6f764ea6f84003dbd42c3ea721a03cb187d0'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())