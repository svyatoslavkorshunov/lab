import sqlite3

def vivod():
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    cur.execute("SELECT * From Izdanie")
    a = "IZDANIE:\n" +str(cur.fetchall()) + "\nPODPISCHIKI:\n"
    cur.execute("SELECT * From Podpischiki")
    a += str(cur.fetchall()) + "\nPODPISKI:\n"
    cur.execute("SELECT * From Podpiski")
    a += str(cur.fetchall())
    cur.close()
    return a

def vivod_izdanie():
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    cur.execute("SELECT * From Izdanie")
    a = cur.fetchall()
    return a

def vivod_podpischiki():
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    cur.execute("SELECT * From Podpischiki")
    a = cur.fetchall()
    return a

def vivod_podpiski():
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    cur.execute("SELECT * From Podpiski")
    a = cur.fetchall()
    return a

con = sqlite3.connect('labtest.db')
cur = con.cursor()