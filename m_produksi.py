import mysql.connector
from mysql.connector import Error
import connection

def inputWetMill(id_cherry,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    try:
        mycursor.execute(query,val)
        if mycursor.rowcount == 1:
            query = "INSERT INTO wetmill (id_cherry,id_biaya) VALUES (%s,%s)"
            val = (str(id_cherry),str(mycursor.lastrowid))
            mycursor.execute(query,val)
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
            query = "INSERT INTO gabah_basah (id_cherry) VALUES ({})".format(id_cherry)
            mycursor.execute(query)
            if mycursor.rowcount == 1:
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
            query = "INSERT INTO bongkar (id_gabahB,id_biaya) VALUES (%s,%s)"
            val = (id_gabahB,id_biaya)
            mycursor.execute(query,val)
            if mycursor.rowcount == 1:
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
            query = "INSERT INTO jemurB (id_gabahB,id_biaya) VALUES (%s,%s)"
            val = (id_gabahB,id_biaya)
            mycursor.execute(query,val)
            if mycursor.rowcount == 1:
                query = "UPDATE panen SET status='gb_jemur' WHERE id_panen = "+str(id_panen)          
                mycursor.execute(query)
                conn.commit()
                print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)

def inputGabahKeringHull(id_gabahB,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    try:
        mycursor.execute(query,val)
        if mycursor.rowcount == 1:
            id_biaya = mycursor.lastrowid    
            query = "INSERT INTO gabah_kering (id_gabahB) VALUES ({})".format(id_gabahB)
            mycursor.execute(query)
            if mycursor.rowcount == 1:
                query = "INSERT INTO hull (id_gabahK,id_biaya) VALUES (%s,%s)"
                val = (mycursor.lastrowid,id_biaya)
                mycursor.execute(query,val)
                if mycursor.rowcount == 1:
                    query = "UPDATE panen SET status='gk_hull' WHERE id_panen = "+str(id_panen)          
                    mycursor.execute(query)
                    conn.commit()
                    print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)

def inputGabahKeringJemur(id_gabahK,berat,harga,tanggal,id_panen):        
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    try:
        mycursor.execute(query,val)
        if mycursor.rowcount == 1:
            id_biaya = mycursor.lastrowid    
            query = "INSERT INTO jemurK (id_gabahK,id_biaya) VALUES (%s,%s)"
            val = (id_gabahK,id_biaya)
            mycursor.execute(query,val)
            if mycursor.rowcount == 1:
                query = "UPDATE panen SET status='gk_jemur' WHERE id_panen = "+str(id_panen)          
                mycursor.execute(query)
                conn.commit()
                print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)
        
def getGabahKering(id_cherry):
    conn = connection.koneksi()
    mycursor  = conn.cursor()
    query = "SELECT * FROM gabah_kering JOIN gabah_basah ON gabah_basah.id_gabahB = gabah_kering.id_gabahB WHERE id_cherry = "+str(id_cherry)
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
    
def inputSuton(id_gabahK,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    try:
        mycursor.execute(query,val)
        if mycursor.rowcount == 1:
            id_biaya = mycursor.lastrowid   
            query = "INSERT INTO green_bean (id_gabahK) VALUES ({})".format(id_gabahK)
            mycursor.execute(query)
            if mycursor.rowcount == 1:
                query = "INSERT INTO suton (id_bean,id_biaya) VALUES (%s,%s)"
                val = (mycursor.lastrowid,id_biaya)
                mycursor.execute(query,val)
                if mycursor.rowcount == 1:
                    query = "UPDATE panen SET status='green_suton' WHERE id_panen = "+str(id_panen)          
                    mycursor.execute(query)
                    conn.commit()
                    print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)

def getGreenBean(id_cherry):
    conn = connection.koneksi()
    mycursor  = conn.cursor()
    query = "SELECT * FROM green_bean JOIN gabah_kering ON green_bean.id_gabahK = gabah_kering.id_gabahK JOIN gabah_basah ON gabah_basah.id_gabahB = gabah_kering.id_gabahB WHERE id_cherry = "+str(id_cherry)
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
    
def inputGrading(id_bean,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    try:
        mycursor.execute(query,val)
        if mycursor.rowcount == 1:
            id_biaya = mycursor.lastrowid    
            query = "INSERT INTO grading (id_bean,id_biaya) VALUES (%s,%s)"
            val = (id_bean,id_biaya)
            mycursor.execute(query,val)
            if mycursor.rowcount == 1:
                query = "UPDATE panen SET status='green_grading' WHERE id_panen = "+str(id_panen)          
                mycursor.execute(query)
                conn.commit()
                print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)

def inputColor(id_bean,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    try:
        mycursor.execute(query,val)
        if mycursor.rowcount == 1:
            id_biaya = mycursor.lastrowid   
            query = "INSERT INTO sorter (id_bean,id_biaya) VALUES (%s,%s)"
            val = (id_bean,id_biaya)
            mycursor.execute(query,val)
            if mycursor.rowcount == 1:
                query = "UPDATE panen SET status='green_color' WHERE id_panen = "+str(id_panen)          
                mycursor.execute(query)
                conn.commit()
                print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)

def inputHandPick(id_bean,berat,harga,tanggal,id_panen):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "INSERT INTO biaya (berat_kg,biaya,tanggal) VALUES (%s,%s,%s)"
    val = (berat,harga,tanggal)
    try:
        mycursor.execute(query,val)  
        if mycursor.rowcount == 1:
            id_biaya = mycursor.lastrowid    
            query = "INSERT INTO hand_pick (id_bean,id_biaya) VALUES (%s,%s)"
            val = (id_bean,id_biaya)
            mycursor.execute(query,val)
            if mycursor.rowcount == 1:
                query = "UPDATE panen SET status='green_hand_pick' WHERE id_panen = "+str(id_panen)          
                mycursor.execute(query)
                conn.commit()
                print("DATA ADDED")
    except mysql.connector.Error as err:
        print(err)
def getDataWetMill(id_cherry):
    conn = connection.koneksi()
    mycursor = conn.cursor()
    query = "SELECT berat_kg,biaya FROM biaya JOIN wetmill ON biaya.id_biaya = wetmill.id_biaya JOIN cherry ON wetmill.id_cherry = cherry.id_cherry WHERE cherry.id_cherry = "+str(id_cherry)
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
def getDataTransport(id_cherry):
    
    query = "SELECT berat_kg,biaya FROM biaya JOIN transport ON biaya.id_biaya = transport.id_biaya JOIN gabah_basah ON gabah_basah.id_gabahB = transport.id_gabahB WHERE id_cherry = "+str(id_cherry)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0

def getDataBongkar(id_cherry):
    query = "SELECT berat_kg,biaya FROM biaya JOIN bongkar ON biaya.id_biaya = bongkar.id_biaya JOIN gabah_basah ON gabah_basah.id_gabahB = bongkar.id_gabahB WHERE id_cherry = "+str(id_cherry)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
    
def getDataGabahBasahJemur(id_cherry):
    query = "SELECT berat_kg,biaya FROM biaya JOIN jemurB ON biaya.id_biaya = jemurB.id_biaya JOIN gabah_basah ON gabah_basah.id_gabahB = jemurB.id_gabahB WHERE id_cherry = "+str(id_cherry)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0

def getDataGabahKeringHull(id_gabahB):
    query = "SELECT berat_kg,biaya FROM biaya JOIN hull ON biaya.id_biaya = hull.id_biaya JOIN gabah_kering ON gabah_kering.id_gabahK = hull.id_gabahK WHERE id_gabahB = "+str(id_gabahB)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
def getDataGabahKeringJemur(id_gabahB):
    query = "SELECT berat_kg,biaya FROM biaya JOIN jemurK ON biaya.id_biaya = jemurK.id_biaya JOIN gabah_kering ON gabah_kering.id_gabahK = jemurK.id_gabahK WHERE id_gabahB = "+str(id_gabahB)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0

def getDataGreenBeanSuton(id_gabahK):
    query = "SELECT berat_kg,biaya FROM biaya JOIN suton ON biaya.id_biaya = suton.id_biaya JOIN green_bean ON green_bean.id_bean = suton.id_bean WHERE id_gabahK = "+str(id_gabahK)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0

def getDataGreenBeanGrading(id_gabahK):
    query = "SELECT berat_kg,biaya FROM biaya JOIN grading ON biaya.id_biaya = grading.id_biaya JOIN green_bean ON green_bean.id_bean = grading.id_bean WHERE id_gabahK = "+str(id_gabahK)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
def getDataGreenBeanSorter(id_gabahK):
    query = "SELECT berat_kg,biaya FROM biaya JOIN sorter ON biaya.id_biaya = sorter.id_biaya JOIN green_bean ON green_bean.id_bean = sorter.id_bean WHERE id_gabahK = "+str(id_gabahK)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
def getDataGreenBeanHandPick(id_gabahK):
    query = "SELECT berat_kg,biaya,tanggal FROM biaya JOIN hand_pick ON biaya.id_biaya = hand_pick.id_biaya JOIN green_bean ON green_bean.id_bean = hand_pick.id_bean WHERE id_gabahK = "+str(id_gabahK)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
    
def getDataSubProcess(status,tipe_proses,id_panen,focus):
    if focus:
        query = """SELECT `biaya`.`berat_kg`, `biaya`.`biaya`"""
    else :
        query = """SELECT SUM(`biaya`.`berat_kg`) AS 'berat total', SUM(`biaya`.`biaya`) AS 'Total Biaya' """
    if status == "cherry":
        query += """
            FROM `biaya`
            JOIN `panen`
            JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
            WHERE (`panen`.`id_panen` = {})""".format(id_panen)
    elif status == "wetmill":
        query += """
            FROM `biaya`
            JOIN `panen`
            JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
            JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
            WHERE (`panen`.`id_panen` = {}) 
            AND (`biaya`.`id_biaya` = `wetmill`.`id_biaya`)""".format(id_panen)
    elif status == "transport":
        query += """
            FROM `biaya`
            JOIN `panen`
            JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
            JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
            JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
            JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            WHERE (`panen`.`id_panen` = {}) 
            AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `transport`.`id_biaya`))""".format(id_panen)
    elif status == "bongkar":
        query += """
            FROM `biaya`
            JOIN `panen`
            JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
            JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
            JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
            JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            WHERE (`panen`.`id_panen` = {}) 
            AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`))""".format(id_panen)
    elif status == "gb_jemur":
        query += """
            FROM `biaya`
            JOIN `panen`
            JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
            JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
            JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
            JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            WHERE (`panen`.`id_panen` = {}) 
            AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`))""".format(id_panen)
    elif status == "gk_hull":
        query += """
            FROM `biaya`
            JOIN `panen`
            JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
            JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
            JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
            JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
            WHERE (`panen`.`id_panen` = {}) 
            AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `hull`.`id_biaya`))""".format(id_panen)
    elif status == "gk_jemur":
        query += """
            FROM `biaya`
            JOIN `panen`
            JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
            JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
            JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
            JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
            JOIN `jemurK` ON (`jemurK`.`id_gabahK`= `gabah_kering`.`id_gabahK`)
            WHERE (`panen`.`id_panen` = {}) 
            AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `hull`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `jemurK`.`id_biaya`))""".format(id_panen)
    elif status == "green_suton":
        if tipe_proses != "Wet Hull" or tipe_proses != "Natural Wet Hull" or tipe_proses != "Honey Wet Hull":
                query += """
                FROM `biaya`
                JOIN `panen`
                JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
                JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
                JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
                JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `green_bean` ON (`green_bean`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `suton` ON (`suton`.`id_bean` = `green_bean`.`id_bean`)
                WHERE (`panen`.`id_panen` = {}) 
                AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `hull`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `suton`.`id_biaya`))""".format(id_panen)
        else:
            query += """
                FROM `biaya`
                JOIN `panen`
                JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
                JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
                JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
                JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `jemurK` ON (`jemurK`.`id_gabahK`= `gabah_kering`.`id_gabahK`)
                JOIN `green_bean` ON (`green_bean`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `suton` ON (`suton`.`id_bean` = `green_bean`.`id_bean`)
                WHERE (`panen`.`id_panen` = {}) 
                AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `hull`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurK`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `suton`.`id_biaya`))""".format(id_panen)
    elif status == "green_grading":
        if tipe_proses != "Wet Hull" or tipe_proses != "Natural Wet Hull" or tipe_proses != "Honey Wet Hull":
            query += """
                FROM `biaya`
                JOIN `panen`
                JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
                JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
                JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
                JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `green_bean` ON (`green_bean`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `suton` ON (`suton`.`id_bean` = `green_bean`.`id_bean`)
                JOIN `grading` ON (`grading`.`id_bean` = `green_bean`.`id_bean`)
                WHERE (`panen`.`id_panen` = {}) 
                AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `hull`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `suton`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `grading`.`id_biaya`)) """.format(id_panen)
        else:
            query += """
                FROM `biaya`
                JOIN `panen`
                JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
                JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
                JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
                JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `jemurK` ON (`jemurK`.`id_gabahK`= `gabah_kering`.`id_gabahK`)
                JOIN `green_bean` ON (`green_bean`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `suton` ON (`suton`.`id_bean` = `green_bean`.`id_bean`)
                JOIN `grading` ON (`grading`.`id_bean` = `green_bean`.`id_bean`)
                WHERE (`panen`.`id_panen` = {}) 
                AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `hull`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurK`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `suton`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `grading`.`id_biaya`)) """.format(id_panen)
    elif status == "green_color":
        if tipe_proses != "Wet Hull" or tipe_proses != "Natural Wet Hull" or tipe_proses != "Honey Wet Hull":
            query += """
            FROM `biaya`
            JOIN `panen`
            JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
            JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
            JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
            JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
            JOIN `green_bean` ON (`green_bean`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
            JOIN `suton` ON (`suton`.`id_bean` = `green_bean`.`id_bean`)
            JOIN `grading` ON (`grading`.`id_bean` = `green_bean`.`id_bean`)
            JOIN `sorter` ON (`sorter`.`id_bean` = `green_bean`.`id_bean`)
            WHERE (`panen`.`id_panen` = {}) 
            AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `hull`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `suton`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `grading`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `sorter`.`id_biaya`)) """.format(id_panen)
        else:
            query += """
                FROM `biaya`
                JOIN `panen`
                JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
                JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
                JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
                JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `green_bean` ON (`green_bean`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `suton` ON (`suton`.`id_bean` = `green_bean`.`id_bean`)
                JOIN `grading` ON (`grading`.`id_bean` = `green_bean`.`id_bean`)
                JOIN `sorter` ON (`sorter`.`id_bean` = `green_bean`.`id_bean`)
                WHERE (`panen`.`id_panen` = {}) 
                AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `hull`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurK`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `suton`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `grading`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `sorter`.`id_biaya`)) """.format(id_panen)
    elif status == "green_hand_pick":
        if tipe_proses != "Wet Hull" or tipe_proses != "Natural Wet Hull" or tipe_proses != "Honey Wet Hull":
            query += """
            FROM `biaya`
            JOIN `panen`
            JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
            JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
            JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
            JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
            JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
            JOIN `green_bean` ON (`green_bean`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
            JOIN `suton` ON (`suton`.`id_bean` = `green_bean`.`id_bean`)
            JOIN `grading` ON (`grading`.`id_bean` = `green_bean`.`id_bean`)
            JOIN `sorter` ON (`sorter`.`id_bean` = `green_bean`.`id_bean`)
            JOIN `hand_pick` ON (`hand_pick`.`id_bean` = `green_bean`.`id_bean`)
            WHERE (`panen`.`id_panen` = {}) 
            AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `hull`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `suton`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `grading`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `sorter`.`id_biaya`)
            OR (`biaya`.`id_biaya` = `hand_pick`.`id_biaya`)) """.format(id_panen)
        else:
            query += """
                FROM `biaya`
                JOIN `panen`
                JOIN `cherry` ON (`cherry`.`id_panen` = `panen`.`id_panen`)
                JOIN `wetmill` ON (`cherry`.`id_cherry` = `wetmill`.`id_cherry`) 
                JOIN `gabah_basah` ON (`gabah_basah`.`id_cherry` = `cherry`.`id_cherry`)
                JOIN `transport` ON (`transport`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `bongkar` ON (`bongkar`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `jemurB` ON (`jemurB`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `gabah_kering` ON (`gabah_kering`.`id_gabahB` = `gabah_basah`.`id_gabahB`)
                JOIN `hull` ON (`hull`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `jemurK` ON (`jemurK`.`id_gabahK`= `gabah_kering`.`id_gabahK`)
                JOIN `green_bean` ON (`green_bean`.`id_gabahK` = `gabah_kering`.`id_gabahK`)
                JOIN `suton` ON (`suton`.`id_bean` = `green_bean`.`id_bean`)
                JOIN `grading` ON (`grading`.`id_bean` = `green_bean`.`id_bean`)
                JOIN `sorter` ON (`sorter`.`id_bean` = `green_bean`.`id_bean`)
                JOIN `hand_pick` ON (`hand_pick`.`id_bean` = `green_bean`.`id_bean`)
                WHERE (`panen`.`id_panen` = {}) 
                AND ((`biaya`.`id_biaya` = `wetmill`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `transport`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `bongkar`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurB`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `hull`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `jemurK`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `suton`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `grading`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `sorter`.`id_biaya`)
                OR (`biaya`.`id_biaya` = `hand_pick`.`id_biaya`)) """.format(id_panen)
    print(query)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
    
def getTanggalTerakhir(id_panen):
    query = """SELECT DATE_FORMAT(biaya.tanggal,'%d/%m/%Y') FROM biaya
    JOIN hand_pick ON hand_pick.id_biaya = biaya.id_biaya
    JOIN green_bean ON green_bean.id_bean = hand_pick.id_bean
    JOIN gabah_kering ON gabah_kering.id_gabahK = green_bean.id_gabahK
    JOIN gabah_basah ON gabah_basah.id_gabahB = gabah_kering.id_gabahB
    JOIN cherry ON cherry.id_cherry = gabah_basah.id_cherry
    WHERE cherry.id_panen = {} """.format(id_panen)
    conn = connection.koneksi()
    mycursor = conn.cursor()
    mycursor.execute(query)
    try:
        result = mycursor.fetchone()
        return result
    except:
        return 0
    