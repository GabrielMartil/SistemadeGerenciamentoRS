import mysql.connector

def conecxao_banco():

  mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="registro"
  )
  
