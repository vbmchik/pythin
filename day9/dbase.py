import mysql.connector
from mysql.connector import errorcode


mydb = mysql.connector.connect(
host='localhost',
user='dbmanager',
password='!QA2ws3ed'
) 
cursor = mydb.cursor()
query = "select * from "
cursor.execute(query)
result = cursor.fetchall()



print(result)