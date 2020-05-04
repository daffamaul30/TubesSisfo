import mysql.connector
from mysql.connector import Error
def koneksi():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='kopi',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')
        conn.cursor()
    except Error as e:
        print(e)

    finally:
        return conn
        # if conn is not None and conn.is_connected():
        #     conn.close()
            

