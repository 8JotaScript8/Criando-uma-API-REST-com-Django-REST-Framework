import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

headers = {'Authorization': f'Token {TOKEN}'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

#assert resultado.status_code == 200

# Testando se o título do primeiro curso está correto
#assert resultado.json()['results'][0]['titulo'] == 'Criação de APIs REST com Django REST Framework'
