import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()

try:
    
    conexao = mysql.connector.connect(
         user=os.getenv("DB_user"), 
        password=os.getenv("DB_password"),
        host=os.getenv("DB_Host"),
        database=os.getenv('DB')
    )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print("conectado com sucesso ao banco")



cursor=conexao.cursor()


def fechar_conexões ():
    cursor.close()
    conexao.close()
    return print("conexão encerrada")



# query = f'select * from colaboradores'


# cursor.execute(query)
# resultado = cursor.fetchall()


# print(resultado)
