import requests
import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

class TestCursos:
    headers = {'Authorization': f'Token {TOKEN}'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}8/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação com Ruby 345",
            "url": "http://www.geekuniversity.com.br/cpr234"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby 34",
            "url": "http://www.geekuniversity.com.br/ncr34"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}8/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby 225",
            "url": "http://www.geekuniversity.com.br/ncr225"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}8/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}8/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0


