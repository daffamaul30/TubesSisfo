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
def inputCherry(id_panen,jumlah,harga):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO cherry (id_panen,jumalah_kg,harga_kg) VALUES (%s,%s,%s)"
    val = (id_panen,jumlah,harga)
    mycursor.execute(query,val)
    mycursor.commit()
    if mycursor.rowcount == 1:
        print("Data Added")
    else:
        print("FAILED")
