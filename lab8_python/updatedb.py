import sqlite3
import datetime

def update_the_izdanie(kod,nazvanie,vid,cena):
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    kor1 = (nazvanie, vid, float(cena),int(kod))
    cur.execute("UPDATE Izdanie SET NazvanieIzdania = (?),VidIzdania = (?),CenaPodpiski =(?) WHERE KodIzdania = (?)", kor1)
    con.commit()
    cur.close()

def update_the_podpischik(kod,fio,gorod,uliza,dom,kvartira):
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    kor1 = (fio, gorod, uliza, dom, kvartira,int(kod))
    cur.execute("UPDATE Podpischiki SET FioPodpischika = (?),GorodPodpischika = (?),UlizaPodpischika =(?),DomPodpischika = (?), KvartiraPodpischika = (?) WHERE KodPodpischika = ?", kor1)
    con.commit()
    cur.close()

def update_the_podpiski(kod,srok):
    con = sqlite3.connect('labtest.db')
    cur = con.cursor()
    kor1 = (datetime.datetime.now(),int(srok),int(kod))
    cur.execute("UPDATE Podpiski SET DataPodpiski = (?), SrokPodpiski = (?) WHERE KodPodpiski = (?)", kor1)
    con.commit()
    cur.close()
