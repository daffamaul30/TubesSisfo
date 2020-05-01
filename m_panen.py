import mysql.connector
from mysql.connector import Error
import connection

def inputPanen(tanggal,blok,varietas,tipe_proses,berat,biaya):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO panen (tanggal,blok,varietas,tipe_proses) VALUES (%s,%s,%s,%s)"
    val = (tanggal,blok,varietas,tipe_proses)
    mycursor.execute(query,val)
    
    conn.commit()
    if mycursor.rowcount == 1:
        query = "INSERT INTO cherry (id_panen,jumlah_kg,harga_kg) VALUES (%s,%s,%s)"
        val = (mycursor.lastrowid,berat,biaya)
        mycursor.execute(query,val)
        conn.commit()
        if mycursor.rowcount == 1:
            print("Data Added")
        else:
            print("FAILED")
    else:
        print("FAILED")
    
def getPanen(tanggal,blok,varietas,tipe_proses):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    
    query = "SELECT id_cherry,panen.id_panen FROM panen,cherry WHERE tanggal='{}' AND blok = '{}' AND varietas='{}' AND tipe_proses='{}'".format(tanggal,blok,varietas,tipe_proses)
    #query  = "SELECT * from cherry WHERE id_panen =({})".format(sub_query)
    #query = "SELECT DATE_FORMAT(waktu,'%d/%m/%Y') as 'tanggal' FROM biji_kopi HAVING tanggal BETWEEN '25/04/2020' AND '30/04/2020' "
    print(query)
    mycursor.execute(query)
    try :
        result = mycursor.fetchone()
        return result
    except:
        return 0

def deletePanen(id):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "DELETE FROM biji_kopi WHERE id_panen = %i" %(id)
    print(query)
    mycursor.execute(query)
    conn.commit()
    print("Data Deleted")
