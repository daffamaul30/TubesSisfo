import mysql.connector
from mysql.connector import Error
import connection

def getCherry(id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    
    query = "SELECT * FROM cherry WHERE id_panen="+str(id_panen)
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        if result[0] >= 1:
            print("DATA FOUND")
            return result
    except:
        print("NOT FOUND")
        return 0

def getGabahBasah(id_cherry):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    
    query = "SELECT * FROM gabah_basah WHERE id_cherry="+str(id_cherry)
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        if result[0] >= 1:
            print("DATA FOUND")
            return result
    except:
        print("NOT FOUND")
        return 0
