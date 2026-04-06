from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Table, MetaData
import pandas as pd
import os


def carrega_album_db(engine): # Função para carregar os CSVs no DB
    try:
        caminho_pasta ="data/staging/albums" # Caminho onde estão os CSV

        dfs = [] # Lista vazia para concatenar os CSVs

        # Percorrendo cada arquivo que existe na pasta 'ALBUMS'
        for arquivo in os.listdir(caminho_pasta):
            if arquivo.endswith(".csv"): # Pegando os arquivos que terminam com '.CSV'
                caminho_completo = os.path.join(caminho_pasta, arquivo) # Juntando o caminho e o arquivo
                df = pd.read_csv(caminho_completo) # Pegando o arquivo e transformando em DF
                dfs.append(df) # Adicionando o DF na lista de DF vazias

        df_album = pd.concat(dfs, ignore_index=True) # DF_ALBUM com os DFs concatenados

        dados = df_album.to_dict(orient="records") # Transformando o DF (cada linha vira um dict)

        metadata = MetaData() # Fazendo o SQLAlchemy copiar uma tabela já criada no DB
        album_table = Table(
            "albuns", # Nome da Tabela
            metadata,
            autoload_with=engine
        )

        stmt = insert(album_table) # Inserindo na tabela 'ALBUNS' o DF 'dados'

        stmt = stmt.on_conflict_do_nothing(
            index_elements=["id_album"] # Ignorando duplicados pelo id_album que é único
        )

        with engine.connect() as conn: # Executando no banco de dados 
            conn.execute(stmt, dados) 
            conn.commit() 

        return 'Dados inseridos com sucesso.'
    
    except Exception as e: # Exceção caso dê algum erro.
        print(f"Erro ao inserir csv no banco: {e}")



def carrega_artistas_db(engine): # Função para carregar os CSVs no DB
    try:
        caminho_pasta ="data/staging/artists" # Caminho onde estão os CSV

        dfs = [] # Lista vazia para concatenar os CSVs

        # Percorrendo cada arquivo que existe na pasta 'ALBUMS'
        for arquivo in os.listdir(caminho_pasta):
            if arquivo.endswith(".csv"): # Pegando os arquivos que terminam com '.CSV'
                caminho_completo = os.path.join(caminho_pasta, arquivo) # Juntando o caminho e o arquivo
                df = pd.read_csv(caminho_completo) # Pegando o arquivo e transformando em DF
                dfs.append(df) # Adicionando o DF na lista de DF vazias

        df_artistas = pd.concat(dfs, ignore_index=True) # DF_ARTISTA com os DFs concatenados

        dados = df_artistas.to_dict(orient="records") # Transformando o DF (cada linha vira um dict)

        metadata = MetaData() # Fazendo o SQLAlchemy copiar uma tabela já criada no DB
        artistas_table = Table(
            "artistas", # Nome da Tabela
            metadata,
            autoload_with=engine
        )

        stmt = insert(artistas_table) # Inserindo na tabela 'ARTISTAS' o DF 'dados'

        stmt = stmt.on_conflict_do_nothing(
            index_elements=["id_artista"] # Ignorando duplicados pelo id_artista que é único
        )

        with engine.connect() as conn: # Executando no banco de dados 
            conn.execute(stmt, dados) 
            conn.commit() 

        return 'Dados inseridos com sucesso.'
    
    except Exception as e: # Exceção caso dê algum erro.
        print(f"Erro ao inserir csv no banco: {e}")


def carrega_faixas_db(engine): # Função para carregar os CSVs no DB
    try:
        caminho_pasta ="data/staging/tracks" # Caminho onde estão os CSV

        dfs = [] # Lista vazia para concatenar os CSVs

        # Percorrendo cada arquivo que existe na pasta 'ALBUMS'
        for arquivo in os.listdir(caminho_pasta):
            if arquivo.endswith(".csv"): # Pegando os arquivos que terminam com '.CSV'
                caminho_completo = os.path.join(caminho_pasta, arquivo) # Juntando o caminho e o arquivo
                df = pd.read_csv(caminho_completo) # Pegando o arquivo e transformando em DF
                dfs.append(df) # Adicionando o DF na lista de DF vazias

        df_faixas = pd.concat(dfs, ignore_index=True) # DF_FAIXAS com os DFs concatenados

        dados = df_faixas.to_dict(orient="records") # Transformando o DF (cada linha vira um dict)

        metadata = MetaData() # Fazendo o SQLAlchemy copiar uma tabela já criada no DB
        faixas_table = Table(
            "faixas", # Nome da Tabela
            metadata,
            autoload_with=engine
        )

        stmt = insert(faixas_table) # Inserindo na tabela 'FAIXAS' o DF 'dados'

        stmt = stmt.on_conflict_do_nothing(
            index_elements=["id_faixa"] # Ignorando duplicados pelo id_faixas que é único
        )

        with engine.connect() as conn: # Executando no banco de dados 
            conn.execute(stmt, dados) 
            conn.commit() 

        return 'Dados inseridos com sucesso.'
    
    except Exception as e: # Exceção caso dê algum erro.
        print(f"Erro ao inserir csv no banco: {e}")


def carrega_faixas_artistas_db(engine): # Função para carregar os CSVs no DB
    try:
        caminho_pasta ="data/staging/tracks-artists" # Caminho onde estão os CSV

        dfs = [] # Lista vazia para concatenar os CSVs

        # Percorrendo cada arquivo que existe na pasta 'ALBUMS'
        for arquivo in os.listdir(caminho_pasta):
            if arquivo.endswith(".csv"): # Pegando os arquivos que terminam com '.CSV'
                caminho_completo = os.path.join(caminho_pasta, arquivo) # Juntando o caminho e o arquivo
                df = pd.read_csv(caminho_completo) # Pegando o arquivo e transformando em DF
                dfs.append(df) # Adicionando o DF na lista de DF vazias

        df_faixas_artists = pd.concat(dfs, ignore_index=True) # DF_faixas_ARTISTAS com os DFs concatenados

        dados = df_faixas_artists.to_dict(orient="records") # Transformando o DF (cada linha vira um dict)

        metadata = MetaData() # Fazendo o SQLAlchemy copiar uma tabela já criada no DB
        faixa_artista_table = Table(
            "faixa_artista", # Nome da Tabela
            metadata,
            autoload_with=engine
        )

        stmt = insert(faixa_artista_table) # Inserindo na tabela 'FAIXA_ARTISTA' o DF 'dados'

        stmt = stmt.on_conflict_do_nothing(
            index_elements=["id_faixa", "id_artista"] # Ignorando duplicados pelos id_faixas e id_artistas que são únicos
        )

        with engine.connect() as conn: # Executando no banco de dados 
            conn.execute(stmt, dados) 
            conn.commit() 

        return 'Dados inseridos com sucesso.'
    
    except Exception as e: # Exceção caso dê algum erro.
        print(f"Erro ao inserir csv no banco: {e}")


