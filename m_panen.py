import mysql.connector
from mysql.connector import Error
import connection

def inputPanen(tanggal,blok,varietas,tipe_proses):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO panen (tanggal,blok,varietas,tipe_proses) VALUES (%s,%s,%s,%s)"
    val = (tanggal,blok,varietas,tipe_proses)
    mycursor.execute(query,val)
    conn.commit()
    if mycursor.rowcount == 1:
        print("Data Added")
    
def getPanen(tanggal,blok,varietas,tipe_proses):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "SELECT * FROM panen WHERE tanggal='{}' AND blok = '{}' AND varietas='{}' AND tipe_proses='{}'".format(tanggal,blok,varietas,tipe_proses)
    #query = "SELECT DATE_FORMAT(waktu,'%d/%m/%Y') as 'tanggal' FROM biji_kopi HAVING tanggal BETWEEN '25/04/2020' AND '30/04/2020' "
    mycursor.execute(query)
    result = mycursor.fetchall()
    for x in result:
        print(x)
    return result

def deletePanen(id):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "DELETE FROM biji_kopi WHERE id_panen = %i" %(id)
    print(query)
    mycursor.execute(query)
    conn.commit()
    print("Data Deleted")
