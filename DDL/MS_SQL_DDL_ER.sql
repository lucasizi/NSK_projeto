create database PROD_NSK;

use PROD_NSK;


CREATE TABLE PLANTAS (
    id_planta INT PRIMARY KEY,
    nome VARCHAR(100),
    pais VARCHAR(50),
    estado VARCHAR(50),
    cidade VARCHAR(50)
);

CREATE TABLE PRODUTOS (
    id_produto INT PRIMARY KEY,
    nome VARCHAR(100),
    categoria VARCHAR(50),
    preco_unitario DECIMAL(10,2),
    id_planta INT,
    FOREIGN KEY (id_planta) REFERENCES PLANTAS(id_planta)
);

CREATE TABLE CLIENTES (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    segmento VARCHAR(50),
    pais VARCHAR(50),
    estado VARCHAR(50),
    cidade VARCHAR(50)
);

CREATE TABLE VENDAS (
    id_venda INT PRIMARY KEY,
    data_venda DATE,
    id_cliente INT,
    id_produto INT,
    quantidade INT,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente),
    FOREIGN KEY (id_produto) REFERENCES PRODUTOS(id_produto)
);

CREATE TABLE QUALIDADE (
    id_controle INT PRIMARY KEY,
    id_planta INT,
    data DATE,
    unidades_produzidas INT,
    unidades_defeituosas INT,
    indice_qualidade DECIMAL(5,2),
    FOREIGN KEY (id_planta) REFERENCES PLANTAS(id_planta)
);