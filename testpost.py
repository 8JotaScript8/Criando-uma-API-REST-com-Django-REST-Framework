import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

headers = {'Authorization': f'Token {TOKEN}'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


novo_curso = {
    "titulo": "Como criar seu dragão 2",
    "url": "http://www.comocriarseudragao.com.br/CD2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

print(resultado.status_code)
print(resultado.text)






