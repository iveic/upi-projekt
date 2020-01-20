import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from karta import Karta
from putnik import Putnik
from podrucje import Podrucje
from zona import Broj_zone

#Karta, Putnik, Podrucje, Broj_zone

def unesi_demo_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    
    try: #karta

        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS karta;

        CREATE TABLE karta (
        id INTEGER PRIMARY KEY,
        datum_izrade DATE NOT NULL,
        vrsta TEXT NOT NULL);
        """)
        
        print("uspjesno kreirana tablica karta!")

        cur.execute("INSERT INTO karta (datum_izrade, vrsta) VALUES (?, ?)", ("2019-12-04", "mjesecna"))
        cur.execute("INSERT INTO karta (datum_izrade, vrsta) VALUES (?, ?)", ("2020-01-08", "godisnja"))
        conn.commit()

        print("uspjesno uneseni testni podaci u tablicu karte!")

    except Exception as e: 
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()

    try: #putnik

        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS putnik;

        CREATE TABLE putnik (
        id INTEGER PRIMARY KEY,
        ime_prezime TEXT NOT NULL,
        godiste INTEGER NOT NULL,
        mjesto_stanovanja TEXT NOT NULL,
        karta_id INTEGER NOT NULL,
        FOREIGN KEY (karta_id) REFERENCES karta (id));
        """)

        print("uspijesno kreirana tablica putnik!")

        cur.execute("INSERT INTO putnik (ime_prezime, godiste, mjesto_stanovanja, karta_id) VALUES (?, ?, ?, ?)", ("Ime Prezime 1", 1988, "Split", 1))
        cur.execute("INSERT INTO putnik (ime_prezime, godiste, mjesto_stanovanja, karta_id) VALUES (?, ?, ?, ?)", ("Ime Prezime 2", 1999, "Omis", 2))
        conn.commit()

        print("uspjesno uneseni testni podaci u tablicu putnik!")
        
    except Exception as e:
        print("dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()

    try: #zona

        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS zona;

        CREATE TABLE zona (
        id INTEGER PRIMARY KEY,
        broj_zone INTEGER NOT NULL);
        """)

        print("uspjesno kreirana tablica zona!")

        cur.execute("INSERT INTO zona (broj_zone) VALUES (?)", (2,))
        cur.execute("INSERT INTO zona (broj_zone) VALUES (?)", (1,))

        print("uspjesno uneseni testni podaci u tablicu zona!")
        
    except Exception as e: 
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()

    try: #podrucje
        
        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS podrucje;

        CREATE TABLE podrucje (
        id INTEGER PRIMARY KEY,
        vrsta TEXT NOT NULL,
        karta_id INTEGER NOT NULL,
        zona_id INTEGER NOT NULL,
        FOREIGN KEY (karta_id) REFERENCES karta (id),
        FOREIGN KEY (zona_id) REFERENCES zona (id));
        """)

        print("uspjesno kreirana tablica podrucje!")

        cur.execute("INSERT INTO podrucje (vrsta, karta_id, zona_id) VALUES (?, ?, ?)", ("grad", 1, 1))
        cur.execute("INSERT INTO podrucje (vrsta, karta_id, zona_id) VALUES (?, ?, ?)", ("prigradsko", 2, 2))

        print("uspjesno uneseni testni podaci u tablicu podrucje!")

    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()
        
    conn.close()

def procitaj_sve_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    lista_podataka = []

    try:

        cur = conn.cursor()
        '''
        cur.execute("""SELECT * FROM putnik INNER JOIN karta
                    ON putnik.karta_id = karta.id JOIN podrucje
                    ON podrucje.karta_id = karta.id JOIN zona
                    ON podrucje.zona_id = zona.id""")''' #problem povezivanja sa podrucjem i zonom
        
        cur.execute("""SELECT * FROM putnik INNER JOIN karta
                    ON putnik.karta_id = karta.id""")

        podaci = cur.fetchall()
        for karta in podaci:
            print(karta)
            p = Putnik(karta[0], karta[1], karta[2], karta[3])
            lista_podataka.append(p)
            k = Karta(karta[5], karta[6], karta[7])
            lista_podataka.append(k)

        print("!")

        for p in lista_podataka:
            print(p)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice karte: ", e)
        conn.rollback()

    conn.close()
    return lista_podataka

def sacuvaj_novu_kartu(datumizrade, vrsta, imeprezime, godiste, mjestostanovanja, kartaid):

    conn = sqlite3.connect("upi_projekt.db")
    try:
        cur = conn.cursor()

        cur.execute("INSERT INTO karta (datum_izrade, vrsta) VALUES (?, ?)", (datumizrade, vrsta))
        conn.commit()

        print("uspjesno dodana nova karta")
        
        cur.execute("INSERT INTO putnik (ime_prezime, godiste, mjesto_stanovanja, karta_id) VALUES (?, ?, ?, ?)", (imeprezime, godiste, mjestostanovanja, kartaid))
        conn.commit()

        print("uspjesno dodan noi putnik")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju nove karte u bazu podataka: ", e)
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
'''
