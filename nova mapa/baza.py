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
    
    try:

        #karta
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

        #putnik
        cur.executescript("""

        DROP TABLE IF EXISTS putnik;

        CREATE TABLE putnik (
        id INTEGER PRIMARY KEY,
        ime_prezime TEXT NOT NULL,
        godiste INTEGER NOT NULL,
        mjesto_stanovanja TEXT,
        karta_id INTEGER NOT NULL,
        FOREIGN KEY (karta_id) REFERENCES karta (id));
        """)

        print("uspijesno kreirana tablica putnik!")

        cur.execute("INSERT INTO putnik (ime_prezime, godiste, mjesto_stanovanja, karta_id) VALUES (?, ?, ?, ?)", ("Ime Prezime 1", 1988, "Split", 1))
        cur.execute("INSERT INTO putnik (ime_prezime, godiste, mjesto_stanovanja, karta_id) VALUES (?, ?, ?, ?)", ("Ime Prezime 2", 1999, "Omis", 2))
        conn.commit()

        print("uspjesno uneseni testni podaci u tablicu putnik!")
    
        #zona
        cur.executescript("""

        DROP TABLE IF EXISTS zona;

        CREATE TABLE zona (
        id INTEGER PRIMARY KEY,
        broj_zone INTEGER NOT NULL);
        """)

        print("uspjesno kreirana tablica zona!")

        cur.execute("INSERT INTO zona (broj_zone) VALUES (?)", (1,))
        cur.execute("INSERT INTO zona (broj_zone) VALUES (?)", (2,))

        print("uspjesno uneseni testni podaci u tablicu zona!")

        #podrucje
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

        ###
        cur.executescript("""DROP TABLE IF EXISTS test;""")
        
    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()
        
    conn.close()

def procitaj_sve_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    lista_podataka = []

    try:

        cur = conn.cursor()
        cur.execute("""SELECT * FROM putnik INNER JOIN karta
                    ON putnik.karta_id = karta.id INNER JOIN podrucje
                    ON podrucje.karta_id = karta.id INNER JOIN zona
                    ON podrucje.zona_id = zona.id""")

        podaci = cur.fetchall()
        for podatak in podaci:
            print(podatak)
            lista = []
            lista.append(Putnik(podatak[0], podatak[1], podatak[2], podatak[3])) #zanemaren 1 strani kljuc, 4
            lista.append(Karta(podatak[5], podatak[6], podatak[7]))
            lista.append(Podrucje(podatak[8], podatak[9])) #zanemarena 2 strana kljuca, 10 11
            lista.append(Broj_zone(podatak[12], podatak[13]))
            lista_podataka.append(lista)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice karte: ", e)
        conn.rollback()

    conn.close()
    return lista_podataka

def sacuvaj_novu_kartu(datumizrade, vrstakarta, imeprezime, godiste, mjestostanovanja, brojzone, vrstapodrucje):

    lista = procitaj_sve_podatke()
    print("Lista")
    print(lista)
    l = len(lista)
    kartaidputnik = l + 1
    kartaidpodrucje = l + 1
    
    conn = sqlite3.connect("upi_projekt.db")
    try:
        cur = conn.cursor()
        
        #karta
        cur.execute("INSERT INTO karta (datum_izrade, vrsta) VALUES (?, ?)", (datumizrade, vrstakarta))
        conn.commit()

        print("uspjesno dodana nova karta")
        
        #putnik
        cur.execute("INSERT INTO putnik (ime_prezime, godiste, mjesto_stanovanja, karta_id) VALUES (?, ?, ?, ?)", (imeprezime, godiste, mjestostanovanja, kartaidputnik))
        conn.commit()

        print("uspjesno dodan novi putnik")
        
        #zona
        cur.execute("INSERT INTO zona (broj_zone) VALUES (?)", (brojzone,))
        conn.commit()

        print("uspjesno dodana nova zona")
        
        #podrucje
        lista = procitaj_sve_podatke()
        zonaid = -1
        x = -1
        for i in range(l):
            if lista[i][3].broj_zone == brojzone:
                x = i
        if x >= 0:
            zonaid = lista[x][3].id
        else:
            zonaid = l + 1
        
        cur.execute("INSERT INTO podrucje (vrsta, karta_id, zona_id) VALUES (?, ?, ?)", (vrstapodrucje, kartaidpodrucje, zonaid))
        conn.commit()

        print("uspjesno dodano novo podrucje")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju nove karte u bazu podataka: ", e)
        conn.rollback()

    conn.close()

def izbrisi_kartu(karta_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        '''
        cur.execute("""DELETE FROM putnik WHERE karta_id in
                    (SELECT karta.id FROM karta INNER JOIN podrucje
                    ON podrucje.karta_id = karta.id INNER JOIN zona
                    ON podrucje.zona_id = zona.id where karta.id = ?)""", [karta_id])'''
        #conn.commit()
        
        #cur.execute("DELETE FROM zona WHERE (SELECT karta_id FROM podrucje WHERE karta_id = ?)", karta_id)
        #conn.commit()
        #cur.execute("DELETE FROM podrucje WHERE karta_id = ?)", karta_id)
        #conn.commit()
        #cur.execute("DELETE FROM putnik WHERE karta_id = ?)", karta_id)
        #conn.commit()
        #cur.execute("DELETE FROM karta WHERE id = ?)", karta_id)
        #conn.commit()
        
        print("Uspjesno izbrisana karta iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri brisanju karte iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def azuriraj_kartu(karta_id, imeprezime, godiste, mjestostanovanja, datumizrade, vrstakarta, vrstapodrucje, brojzone):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = con.cursor()
        cur.execute("UPDATE putnik SET ime_prezime = ?, godiste = ?, mjesto_stanovanja = ? WHERE karta_id = ?", (imeprezime, godiste, mjestostanovanja, karta_id))
        cur.commit()

        cur.execute("UPDATE karta SET datum_izrade = ?, vrsta = ? WHERE id = ?", (datumizrade, vrstakarta, karta_id))
        cur.commit()

        cur.execute("UPDATE podrucje SET vrsta = ? WHERE karta_id = ?", (vrstapodrucje, karta_id))
        cur.commit()

        cur.execute("UPDATE zona SET broj_zone = ? WHERE (SELECT karta_id FROM podrucje) karta_id = ?)", (brojzone, karta_id)) #vrlo vjerovatno krivo
        cur.commit()
        
        print("uspjesno azurirani podatci")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju karte iz baze podataka: ", e)
        conn.rollback()
        
    conn.close()


def dohvati_kartu_po_id(karta_id):
    conn = sqlite3.connect("upi_projekt.db")
    #karta = None
    try:

        cur = conn.cursor()
        cur.execute("""SELECT * FROM putnik INNER JOIN karta
                    ON putnik.karta_id = karta.id INNER JOIN podrucje
                    ON podrucje.karta_id = karta.id INNER JOIN zona
                    ON podrucje.zona_id = zona.id
                    WHERE karta.id = ?""", (karta_id))
        podatak = cur.fetchone()
        print("podatak")
        print(podatak)
        lista_podataka = []
        lista = []
        lista.append(Putnik(podatak[0], podatak[1], podatak[2], podatak[3]))
        lista.append(Karta(podatak[5], podatak[6], podatak[7]))
        lista.append(Podrucje(podatak[8], podatak[9]))
        lista.append(Broj_zone(podatak[12], podatak[13]))
        lista_podataka.append(lista[1].id)
        lista_podataka.append(lista[0].ime_prezime)
        lista_podataka.append(lista[0].godiste)
        lista_podataka.append(lista[0].mjesto_stanovanja)
        lista_podataka.append(lista[1].datum_izrade)
        lista_podataka.append(lista[1].vrsta)
        lista_podataka.append(lista[2].vrsta)
        lista_podataka.append(lista[3].broj_zone)
        print(lista_podataka)

        print("uspjesno dohvacena karta iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju karte iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return lista_podataka #karta
