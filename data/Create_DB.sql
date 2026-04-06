CREATE TABLE albuns (
    sk_id SERIAL PRIMARY KEY,
    id_album VARCHAR(50) UNIQUE NOT NULL,
    tipo_album VARCHAR(30),
    total_faixas INT,
    nome VARCHAR(255),
    data_lancamento DATE,
    popularidade INT
);

CREATE TABLE artistas (
    sk_id SERIAL PRIMARY KEY,
    id_artista VARCHAR(50) UNIQUE NOT NULL,
    nome VARCHAR(255),
    tipo VARCHAR(30)
);

CREATE TABLE faixas (
    sk_id SERIAL PRIMARY KEY,
    id_faixa VARCHAR(50) UNIQUE NOT NULL,
    id_album VARCHAR(50) NOT NULL,
    numero_faixa INT,
    nome VARCHAR(255),
    duracao_ms INT,
    tipo VARCHAR(30),

    CONSTRAINT fk_album
        FOREIGN KEY (id_album)
        REFERENCES albuns(id_album)
);

CREATE TABLE faixa_artista (
    sk_id SERIAL PRIMARY KEY,
    id_faixa VARCHAR(50) NOT NULL,
    id_artista VARCHAR(50) NOT NULL,

    CONSTRAINT fk_faixa
        FOREIGN KEY (id_faixa)
        REFERENCES faixas(id_faixa),

    CONSTRAINT fk_artista
        FOREIGN KEY (id_artista)
        REFERENCES artistas(id_artista),

    CONSTRAINT unique_faixa_artista
        UNIQUE (id_faixa, id_artista)
);