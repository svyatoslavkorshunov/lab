import sqlite3
import datetime
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def insert_to_contract(id,supplier,title,note):
    con = create_connection("localhost", "root", "", "delivery")
    with con.cursor() as cursor:
        kor1 = (int(id), datetime.datetime.now(), int(supplier), title, note)
        cursor.execute("INSERT INTO contract VALUES (?,?,?,?,?)", kor1)
        con.commit()


def insert_to_podpischik(kod,fio,gorod,uliza,dom,kvartira):
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    kor1 = (int(kod), fio, gorod, uliza, dom, kvartira)
    cur.execute("INSERT INTO Podpischiki VALUES (?,?,?,?,?,?)", kor1)
    con.commit()
    cur.close()

def insert_to_podpiski(kod,srok,kodi,kodp):
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    kor1 = (int(kod), datetime.datetime.now(),int(srok),int(kodi),int(kodp))
    cur.execute("INSERT INTO Podpiski VALUES (?,?,?,?,?)", kor1)
    con.commit()
    cur.close()

