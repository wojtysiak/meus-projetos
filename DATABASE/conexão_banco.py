import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()


def conectar_banco():
  try:
      conexao = mysql.connector.connect(
          user=os.getenv("DB_user"), 
          password=os.getenv("DB_password"),
          host=os.getenv("DB_Host"),
          database=os.getenv('DB')
      )
      return conexao
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
      return False
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
      return False
    else:
      return False, err









