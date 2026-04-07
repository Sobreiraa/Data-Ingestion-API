# Data-Ingestion-API

# Spotify Data Ingestion API

Projeto de engenharia de dados que realiza a ingestão, transformação e carga (ETL) de dados da API do Spotify para um banco de dados PostgreSQL.

## Visão Geral

Este projeto implementa um pipeline ETL completo:

- **Extract**: Consome dados da API do Spotify
- **Transform**: Processa e estrutura os dados em entidades relacionais
- **Load**: Persiste os dados em um banco PostgreSQL

Os dados coletados incluem:

- Álbuns
- Artistas
- Faixas
- Relação entre faixas e artistas (visto que uma faixa pode ter vários artistas)

---

## Tecnologias Utilizadas

- Python
- SQLAlchemy
- PostgreSQL
- Pandas
- Requests

---

## Pipeline ETL

### 1. Extract

- Geração de token de acesso à API do Spotify
- Coleta de dados via requisições HTTP
- Armazenamento em JSON (`data/raw`)

### 2. Transform

Os dados são processados e separados em:

- `coleta_album`
- `coleta_artista`
- `coleta_faixa`
- `coleta_faixa_artista`

Os resultados são salvos em arquivos CSV na camada `staging`.

### 3. Load

- Inserção dos dados no PostgreSQL
- Uso de `SQLAlchemy`
- Controle de duplicidade com `ON CONFLICT`

---

## Banco de Dados

Antes de executar o projeto, crie o banco utilizando:

data/Create_DB.sql

## Como Executar

### 1. Clone o repositório

```
git clone <repo-url>
cd Data-Ingestion-API
```

### 2. Crie o ambiente virtual

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependencias com:

```
pip install -r requirements.txt
```

### 4. Configure variáveis de ambiente

Crie um arquivo .env com suas credenciais da API do Spotify:

```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

### 5. Execute o pipeline

```
python app/main.py
```
