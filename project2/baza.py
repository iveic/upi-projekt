import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from karte import Karte
'''
def unesi_demo_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS karte;

        CREATE TABLE karte (
        id INTEGER PRIMARY KEY,
        ime_prezime TEXT NOT NULL,
        godiste INTEGER NOT NULL,
        datum_izrade DATE NOT NULL,
        vrsta TEXT NOT NULL);
        """)
        
        print("uspjesno kreirana tablica karte!")

        cur.execute("INSERT INTO karte (ime_prezime, godiste, datum_izrade, vrsta) VALUES (?, ?, ?, ?)", ("Mate Matic", 1984, "2019-12-04", "mjesecna"))
        cur.execute("INSERT INTO karte (ime_prezime, godiste, datum_izrade, vrsta) VALUES (?, ?, ?, ?)", ("Stipe Stipic", 1980, "2020-01-08", "godisnja"))
        conn.commit()

        print("uspjesno uneseni testni podaci u tablicu karte!")

    except Exception as e: 
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()
        
    conn.close()
'''
def procitaj_sve_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    lista_karata = []
    try:

        cur = conn.cursor()
        cur.execute(""" SELECT id, ime_prezime, godiste, datum_izrade, vrsta FROM karte """)

        podaci = cur.fetchall()
        
        for karta in podaci:
            # 0 - id
            # 1 - ime_prezime
            # 2 - godiste
            # 3 - datum_izrade
            # 4 - vrsta

            k = Karte(karta[0], karta[1], karta[2], karta[3], karta[4])
            lista_karata.append(k)

        print("uspjesno dohvaceni svi podaci iz tablice karte!")

        for k in lista_karata:
            print(k)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice karte: ", e)
        conn.rollback()

    conn.close()
    return lista_karata


def sacuvaj_novu_kartu(imeprezime, godiste, datumizrade, vrsta):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO karte (ime_prezime, godiste, datum_izrade, vrsta) VALUES (?, ?, ?, ?)", (imeprezime, godiste, datumizrade, vrsta))
        conn.commit()

        print("uspjesno dodana nova karta u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju nove karte u bazu podataka: ", e)
        conn.rollback()

    conn.close()

def izbrisi_kartu(karta_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("DELETE FROM karte WHERE id=?;", (karta_id))
        conn.commit()

        print("uspjesno izbrisana karta iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri brisanju karte iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dohvati_kartu_po_id(karta_id):
    conn = sqlite3.connect("upi_projekt.db")
    karta = None
    try:

        cur = conn.cursor()
        cur.execute(" SELECT id, ime_prezime, godiste, datum_izrade, vrsta FROM karte WHERE id = ?", (karta_id))
        podaci = cur.fetchone()

        print("podaci", podaci)
        karta = Karte(podaci[0], podaci[1], podaci[2], podaci[3], podaci[4])

        print("uspjesno dohvacena karta iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju karte iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return karta

def azuriraj_kartu(karta_id, imeprezime, godiste, datumizrade, vrsta):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("UPDATE karte SET ime_prezime = ?, godiste = ?, datum_izrade = ?, vrsta = ? WHERE id = ?", (imeprezime, godiste, datumizrade, vrsta, karta_id))
        conn.commit()

        print("uspjesno ažurirana karta iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju karte iz baze podataka: ", e)
        conn.rollback()

    conn.close()
