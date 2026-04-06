from app.pipelines.extract import extract_access_token, extract_dados_API
from app.pipelines.transform import coleta_album, coleta_artista, coleta_faixa, coleta_faixa_artista
from app.pipelines.load import carrega_album_db, carrega_artistas_db, carrega_faixas_db, carrega_faixas_artistas_db
from sqlalchemy import create_engine
import json

# dialect+driver://username:password@host:port/database
engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/spotify") # Engine do SQLAlchemy pra conectar no db


# -----------------------------------
# ---------EXECUÇÃO DO ETL-----------
# -----------------------------------

# EXTRACT
access_token = extract_access_token()
print(extract_dados_API(access_token))


# TRANSFORM
with open("data/raw/spotify-API.json", "r", encoding="utf-8") as f: # Abrindo o json salvo para usar na transformação e coleta dos dados
    data = json.load(f)

for album in data["albums"]:
    print(coleta_album(album))
    print(coleta_artista(album))
    print(coleta_faixa(album))
    print(coleta_faixa_artista(album)) 


# LOAD
print(carrega_album_db(engine))
print(carrega_artistas_db(engine))
print(carrega_faixas_db(engine))
print(carrega_faixas_artistas_db(engine))

