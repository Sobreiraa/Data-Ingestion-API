import requests
import os
import pprint
import pandas as pd
import json
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




