import bcrypt
from conexão_banco import conectar_banco
import mysql.connector
import flet as ft
import time


def Consultar_estoque(Marca):gi
    conexao = conectar_banco()
    if not conexao:
        return False, "Sem conexão com o banco de dados"
    cursor = conexao.cursor()
    comando = 'SELECT * FROM Produto INNER JOIN Estoque ON Produto.id = Estoque.id_produto where Produto.marca = %s'
    try:
        cursor.execute(comando,(Marca,))
        estoque = []
        for produto in cursor.fetchall():
            estoque.append(produto)
        return True, estoque
    except mysql.connector.Error as err:
        return False, F"Erro na consulta {err}"
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

print(Consultar_estoque('SAMSUNG'))

def Consultar_marcas_estoque():
    conexao = conectar_banco()
    if not conexao:
        return False, "Sem conexão com o banco de dados"
    cursor = conexao.cursor()
    comando = 'Select DISTINCT Marca from produto'
    try:
        cursor.execute(comando)
        marcas = []
        for marca in cursor.fetchall():
            marcas.append(marca[0])
        return marcas
    except mysql.connector.Error as err:
        return False, F'Erro na consulta {err}'
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        



