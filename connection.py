import mysql.connector
from mysql.connector import Error
def koneksi():
    conn = None
    try:
        conn = mysql.connector.connect(host='52.149.60.155',
                                       database='kopi',
                                       user='kopi2',
                                       password='kopi2')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            
def inputPanen(jenis,berat,tanggal,waktu):
    conn = mysql.connector.connect(host='52.149.60.155',
                                       database='kopi',
                                       user='blog',
                                       password='3a95b6d39a6863dc0f53577aac11de16')
    mycursor = conn.cursor()
    query = "INSERT INTO biji_kopi (jenis_kopi,berat,tanggal,waktu) VALUES (%s,%s,%s,%s)"
    val = (jenis,berat)
    mycursor.execute(query,val)
    conn.commit()
    if mycursor.rowcount == 1:
        print("Data Added")
    
koneksi()