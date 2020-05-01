import mysql.connector
from mysql.connector import Error
import connection

def getCherry(id):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    
    query = "SELECT * FROM cherry WHERE id_panen="+str(id)
    mycursor.execute(query)
    
    if mycursor.rowcount == 1:
        print("DATA FOUND")
        return True
    else:
        print("NOT FOUND")
        return False
