import json
import pandas as pd

# 
with open("data/raw/api_return.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def coleta_album(data_json): # Coleta dados do album
    data_album = {
        "id_album": data_json["id"],
        "tipo_album": data_json["album_type"],
        "total_faixas": data_json["total_tracks"],
        "nome_album": data_json["name"],
        "data_lancamento": data_json["release_date"],
        "popularidade": data_json["popularity"],
    }

    df = pd.DataFrame([data_album]) # Transformando o 'dict único' em DF
    df.to_csv(f"data/staging/albums/album-{data_json['id']}.csv", index=False) # Pegando o DF e gerando um arquivo CSV

    return 'Dados coletados com sucesso!'


def coleta_artista(data_json):  # Coleta dados dos Artistas do Album
    lista_artistas = []
    artistas_vistos = set()  # Controle de duplicados

    # Artistas do álbum
    for artista_album in data_json["artists"]:
        if artista_album["id"] not in artistas_vistos:
            data_artista = {
                "id_artista": artista_album["id"],
                "nome": artista_album["name"],
                "type": artista_album["type"]
            }
            lista_artistas.append(data_artista)
            artistas_vistos.add(artista_album["id"])

    # Artistas das faixas
    for faixa in data_json["tracks"]["items"]:
        for artista_faixa in faixa["artists"]:
            if artista_faixa["id"] not in artistas_vistos:
                data_artista = {
                    "id_artista": artista_faixa["id"],
                    "nome": artista_faixa["name"],
                    "type": artista_faixa["type"]
                }
                lista_artistas.append(data_artista)
                artistas_vistos.add(artista_faixa["id"])

    df = pd.DataFrame(lista_artistas)
    df.to_csv(f"data/staging/artists/artistas_album-{data_json['id']}.csv", index=False)

    return 'Dados coletados com sucesso!'


def coleta_faixa(data_json): # Coleta dados das Músicas do Album
    faixas = []

    for faixa in data_json["tracks"]["items"]: # Iterando pelas faixas do album
        faixas.append({
            "id_faixa": faixa["id"], 
            "id_album": data_json["id"], # Coletando o ID do Album
            "numero_faixa": faixa["track_number"],
            "nome": faixa["name"],
            "duracao_ms": faixa["duration_ms"],
            "tipo": faixa["type"]
        })
    
    df = pd.DataFrame(faixas) # Transformando a 'lista de dict' em DF
    df.to_csv(f"data/staging/tracks/faixas_album-{data_json['id']}.csv", index=False) # Pegando o DF e transformando em arquivo CSV

    return 'Dados coletados com sucesso!'


def coleta_faixa_artista(data_json):
    # Relação de id_faixa e id_artista, para as faixas com mais de um artista
    lista_faixa_artista = []

    for faixa in data_json["tracks"]["items"]: # Iteando pelas faixas
        id_faixa = faixa["id"]

        for artista in faixa["artists"]: # Iterando pelos artistas das faixas
            lista_faixa_artista.append({
                "id_faixa": id_faixa,
                "id_artista": artista["id"]
            })
    
    df = pd.DataFrame(lista_faixa_artista)
    df.to_csv(f"data/staging/tracks/faixa_artistas_album-{data_json['id']}.csv", index=False)

    return 'Dados coletados com sucesso!'


for album in data["albums"]:
    print(coleta_album(album))
    print(coleta_artista(album))
    print(coleta_faixa(album))
    print(coleta_faixa_artista(album)) 





