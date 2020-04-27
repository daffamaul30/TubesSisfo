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
        conn.cursor()
    except Error as e:
        print(e)

    finally:
        return conn
        # if conn is not None and conn.is_connected():
        #     conn.close()
            
def inputPanen(jenis,berat,waktu,tanggal):
    conn = koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biji_kopi (jenis_kopi,berat,waktu,tanggal) VALUES (%s,%s,%s,%s)"
    val = (jenis,berat,waktu,tanggal)
    mycursor.execute(query,val)
    conn.commit()
    if mycursor.rowcount == 1:
        print("Data Added")
    
def getPanen():
    conn = koneksi()
    mycursor = conn.cursor()
    #query = "SELECT * FROM biji_kopi"
    query = "SELECT DATE_FORMAT(waktu,'%d/%m/%Y') as 'tanggal' FROM biji_kopi HAVING tanggal BETWEEN '25/04/2020' AND '30/04/2020' "
    mycursor.execute(query)
    result = mycursor.fetchall()
    for x in result:
        print(x)
