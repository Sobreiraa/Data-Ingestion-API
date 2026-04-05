import requests
import os
import json
import pandas as pd
from dotenv import load_dotenv


def extract_access_token():
        # Localizando o .env
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        env_path = os.path.join(base_dir, ".env")

        # Carregando o .env
        load_dotenv(env_path)  

        # Pegando as credenciais e definindo nas variaveis definidas
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")

        # Definindo a URL para coleta do token de acesso (Endpoint de autenticação do Spotify)
        url = "https://accounts.spotify.com/api/token"

        # Corpo da requisição
        data = {
            "grant_type": "client_credentials", # Tipo da requisição
            "client_id": CLIENT_ID, # Meu ID no SPOTIFY APP
            "client_secret": CLIENT_SECRET # Minha senha no SPOTIFY APP
        }

        # Metadados 
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Requisição HTPP (POST pois estou enviando minhas CREDENCIAIS para pegar o TOKEN de acesso)
        response = requests.post(url, data=data, headers=headers) # Variável para guardar o token de acesso

        if response.status_code != 200:
            raise Exception(f"Erro ao obter token: {response.text}") 

        return response.json()["access_token"]


def extract_dados_API(access_token):
    # URL de onde vamos pegar os dados
    url = "https://api.spotify.com/v1/albums"

    # Parâmetros, IDs dos Albuns que vamos coletar
    params = {
    "ids": "43k99CXeU2JUO21G1F4WCP,1aqg30bNvLSWgShZgX4oop,0KJc9ksnoJJsdpQxV3z5i1,2Y9IRtehByVkegoD7TcLfi,3kjHLu1pL7tdY88GFwEkl6,31hcgCSu4mlA82syOFItur,2DQ6hHlAGj6DiT0Y068bnK,5DV2liMHX5AqtiLqy3Qu1b,0whPMf7IlDh0fRufgqQ37h,65ddZj6nMC8ypPvzoTxVli,7dLOvaC7Qr3cJUt0vo88Os,5yNfC7mKzPRlvSqR3J2Jfq,3ZJMXbIYhx5CG7DsrRVxwP,6RsZXnolUCMjZAcdVlaD0l,6QWmIGUIKxpMphCOQb5s6b,4IL9DJvDvCJUQJwwOdZfYD,3SpBlxme9WbeQdI9kx7KAV,5lxavLVQXbp52tsabsKxhd,7GoZNNb7Yl74fpk8Z6I2cv,2EDW8OhiHdB2UtE6PCAxZD"
    }

    # Token de Acesso
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Realizando a requisição na API, passando a url, o token de acesso e os parâmetros (IDs)
    response = requests.get(url, headers=headers, params=params)
    data = response.json() # Variável para salvar o retorno da response.json
    
    if response.status_code == 200:
        # Salvando o arquivo 
        with open("data/raw/spotify-API.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return 'JSON coletado e salvo com sucesso!'
    else:
        print(data)
        return 'Erro ao coletar dados'


access_token = extract_access_token()
print(extract_dados_API(access_token))




