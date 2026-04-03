import json
import pandas as pd

# 
with open("data/api_return.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def coleta_dados(data_json):
    # Coletando dados do album
    data_album = {
        "id_album": data_json["id"],
        "total_faixas": data_json["total_tracks"],
        "nome_album": data_json["name"],
        "data_lancamento": data_json["release_date"],
        "tipo": data_json["album_type"],
        #"popularidade": data_json["popularity"],
        "genero": data_json["genres"]
    }

    # Coletando dados do Artista do Album
    lista_artistas = []
    for artista in data_json["artists"]:
        data_artista = {
            "id_artista": artista["id"],
            "nome": artista["name"],
            "type": artista["type"]
        }
        
        lista_artistas.append(data_artista)

    # Coletando dados das Músicas do Album
    lista_faixas = []

    for 1 in qtd_faixas+1:
        data_faixas = {
            ""
        }
    return data_album, data_artista



print(coleta_dados(data))
    


