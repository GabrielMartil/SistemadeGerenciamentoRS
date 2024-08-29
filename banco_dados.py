import sqlite3
from sqlite3 import Error
import os

def ConexaoBanco():
    caminho="registro.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()
def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
    except Error as ex:
        print(ex)
image_data = b''

vcon = ConexaoBanco()

"""vsql=CREATE TABLE base_dados (
        seg INTEGER PRIMARY KEY ASC,
        cpf VARCHAR (14) NOT NULL,
        tipo1 CHAR (10) NOT NULL,
        nome CHAR (40)NOT NULL,
        data INT NOT NULL,
        supervisor CHAR (40),
        parceiro CHAR (40) NOT NULL,
        valor DECIMAL (15, 2) NOT NULL,
        obs CHAR (100),
        data_pg INT
    );
def criartabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("tabela criada")
    except Error as ex:
        print(ex)
criarTabela(vcon,vsql)
vcon.close()"""

def dql(query): #select
    vcon=ConexaoBanco()
    c=vcon.cursor()
    vcon.commit()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res
    
def dml(query): #insert, update, delete
    try:
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close
    except Error as ex:
        print(ex)