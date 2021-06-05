import sqlite3


def delete_from_izdanie(kod):
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    kor1 = (int(kod),)
    cur.execute("DELETE FROM Izdanie WHERE (KodIzdania=(?))", kor1)
    cur.execute("DELETE FROM Podpiski WHERE (KodIzdania=(?))", kor1)
    con.commit()
    cur.close()

def delete_from_podpischik(kod):
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    kor1 = (int(kod),)
    cur.execute("DELETE FROM Podpischiki WHERE (KodPodpischika=(?))", kor1)
    cur.execute("DELETE FROM Podpiski WHERE (KodPodpischika=(?))", kor1)
    con.commit()
    cur.close()

def delete_from_podpiski(kod):
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    kor1 = (int(kod),)
    cur.execute("DELETE FROM Podpiski WHERE (KodPodpiski=(?))",kor1)
    con.commit()
    cur.close()