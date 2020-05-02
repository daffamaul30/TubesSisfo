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
def inputWetMill(id_cherry,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    print(query,val)
    mycursor.execute(query,val)
    mycursor.commit()
    if mycursor.rowcount == 1:
        query = "INSERT INTO wetmill (id_cherry,id_biaya) VALUES(%s,%s)"
        val = (id_cherry,mycursor.lastrowid)
        if mycursor.rowcount == 1:
            query = "UPDATE panen SET status='wetmill' WHERE id_panen = "+str(id_panen)          
            mycursor.execute(query)
            mycursor.commit()
            print("Data Added")
        else:
            print("FAILED")   
    else:
        print("FAILED")
def getWetMill(id_cherry):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "SELECT * FROM wetmill WHERE id_cherry ="+str(id_cherry)
    mycursor.execute(query)
    try :
        result = mycursor.fetchone()
        return result
    except:
        return 0
    
