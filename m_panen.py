import mysql.connector
from mysql.connector import Error
import connection

def inputPanen(jenis,berat,waktu,tanggal):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biji_kopi (jenis_kopi,berat,waktu,tanggal) VALUES (%s,%s,%s,%s)"
    val = (jenis,berat,waktu,tanggal)
    mycursor.execute(query,val)
    conn.commit()
    if mycursor.rowcount == 1:
        print("Data Added")
    
def getPanen():
    conn = connection.koneksi()
    mycursor = conn.cursor()
    #query = "SELECT * FROM biji_kopi"
    query = "SELECT DATE_FORMAT(waktu,'%d/%m/%Y') as 'tanggal' FROM biji_kopi HAVING tanggal BETWEEN '25/04/2020' AND '30/04/2020' "
    mycursor.execute(query)
    result = mycursor.fetchall()
    for x in result:
        print(x)
