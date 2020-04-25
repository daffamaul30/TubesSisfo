import mysql.connector
from mysql.connector import Error

def inputPanen(jenis,berat,tanggal,waktu):
    conn = mysql.connector.connect(host='localhost',
                                       database='kopi',
                                       user='kopi',
                                       password='kopi')
    mycursor = conn.cursor()
    query = "INSERT INTO biji_kopi (jenis_kopi,berat,tanggal,waktu) VALUES (%s,%s,%s,%s)"
    val = (jenis,berat,waktu,tanggal)
    mycursor.execute(query,val)
    conn.commit()
    if mycursor.rowcount == 1:
        print("Data Added")
    
