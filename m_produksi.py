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


def inputWetMill(id_cherry,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    print(query,val)
    try:
        mycursor.execute(query,val)
        #conn.commit()
        if mycursor.rowcount == 1:
            
            query = "INSERT INTO wetmill (id_cherry,id_biaya) VALUES (%s,%s)"
            val = (str(id_cherry),str(mycursor.lastrowid))
            mycursor.execute(query,val)
            #conn.commit()
            if mycursor.rowcount == 1:
                print("WETMILL SUKSES")
                query = "UPDATE panen SET status='wetmill' WHERE id_panen = "+str(id_panen)          
                mycursor.execute(query)
                conn.commit()
                print("Data Added")
            
    except mysql.connector.Error as err:
            print(err)
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
def inputTransport(id_cherry,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    
    try:
        mycursor.execute(query,val)
        
        if mycursor.rowcount == 1:
            id_biaya = mycursor.lastrowid
            #print("IDBIAYA",id_biaya)    
            query = "INSERT INTO gabah_basah (id_cherry) VALUES ({})".format(id_cherry)
            mycursor.execute(query)
            if mycursor.rowcount == 1:
                #print("GABAH BASAH")
                query = "INSERT INTO transport (id_gabahB,id_biaya) VALUES (%s,%s)"
                val = (mycursor.lastrowid,id_biaya)
                mycursor.execute(query,val)
                if mycursor.rowcount == 1:
                    query = "UPDATE panen SET status='transport' WHERE id_panen = "+str(id_panen)          
                    mycursor.execute(query)
                    conn.commit()
                    print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)

def inputBongkar(id_gabahB,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    
    try:
        mycursor.execute(query,val)
        
        if mycursor.rowcount == 1:
            id_biaya = mycursor.lastrowid
            #print("IDBIAYA",id_biaya)    
            query = "INSERT INTO bongkar (id_gabahB,id_biaya) VALUES (%s,%s)"
            val = (id_gabahB,id_biaya)
            mycursor.execute(query,val)
            if mycursor.rowcount == 1:
                #print("BONGKAR")
                query = "UPDATE panen SET status='bongkar' WHERE id_panen = "+str(id_panen)          
                mycursor.execute(query)
                conn.commit()
                print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)
        
def getGabahBasah(id_cherry):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "SELECT * FROM gabah_basah WHERE id_cherry="+str(id_cherry)
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0

def inputGabahBasahJemur(id_gabahB,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    
    try:
        mycursor.execute(query,val)
        
        if mycursor.rowcount == 1:
            id_biaya = mycursor.lastrowid
            #print("IDBIAYA",id_biaya)    
            query = "INSERT INTO jemurB (id_gabahB,id_biaya) VALUES (%s,%s)"
            val = (id_gabahB,id_biaya)
            mycursor.execute(query,val)
            if mycursor.rowcount == 1:
                #print("GB JEMUR")
                query = "UPDATE panen SET status='gb_jemur' WHERE id_panen = "+str(id_panen)          
                mycursor.execute(query)
                conn.commit()
                print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)