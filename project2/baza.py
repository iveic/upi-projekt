import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from karta import Karta
from putnik import Putnik
from kartaputnik import KartaPutnik

def unesi_demo_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS putnik;

        CREATE TABLE putnik (
        id INTEGER PRIMARY KEY,
        ime_prezime TEXT,
        email TEXT);
        """)

        print("uspjesno kreirana tablica putnik!")

        cur.execute("INSERT INTO putnik (ime_prezime, email) VALUES (?, ?)", ("ime prezime 1", "mail_1@gmail.com"))
        cur.execute("INSERT INTO putnik (ime_prezime, email) VALUES (?, ?)", ("ime prezime 2", "mail_2@gmail.com"))

        print("uspjesno uneseni testni podaci u tablicu putnik!")

        cur.executescript("""

        DROP TABLE IF EXISTS karta;

        CREATE TABLE karta (
        id INTEGER PRIMARY KEY,
        vrsta TEXT);
        """)

        print("uspjesno kreirana tablica karta!")

        cur.execute("INSERT INTO karta (vrsta) VALUES (?)", ("mjesecna",))
        cur.execute("INSERT INTO karta (vrsta) VALUES (?)", ("godisnja",))

        print("uspjesno uneseni testni podaci u tablicu karta!")

        cur.executescript("""

        DROP TABLE IF EXISTS kartaputnik;

        CREATE TABLE kartaputnik (
        id INTEGER PRIMARY KEY,
        id_karta INTEGER,
        id_putnik INTEGER,
        datum DATE,
        FOREIGN KEY (id_karta) REFERENCES karta (id),
        FOREIGN KEY (id_putnik) REFERENCES putnik (id));
        """)

        print("uspjesno kreirana tablica karta!")

        cur.execute("INSERT INTO kartaputnik (id_karta, id_putnik, datum) VALUES (?, ?, ?)", (1, 1, "2020-01-05"))
        cur.execute("INSERT INTO kartaputnik (id_karta, id_putnik, datum) VALUES (?, ?, ?)", (2, 2, "2019-03-12"))

        print("uspjesno uneseni testni podaci u tablicu karta!")

        conn.commit()
        
    except Exception as e: 
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()
        
    conn.close()

def procitaj_sve_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    lista_podataka = []
    try:

        cur = conn.cursor()
        cur.execute("""SELECT * FROM putnik INNER JOIN kartaputnik
                    ON kartaputnik.id_putnik = putnik.id INNER JOIN karta
                    ON kartaputnik.id_karta = karta.id""")

        podaci = cur.fetchall()
        print(podaci)

        for e in podaci:
            lista = []
            lista.append(Putnik(e[0], e[1], e[2]))
            lista.append(KartaPutnik(e[3], e[4], e[5], e[6]))
            lista.append(Karta(e[7], e[8]))
            lista_podataka.append(lista)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice karte: ", e)
        conn.rollback()

    conn.close()
    return lista_podataka


def sacuvaj_novu_kartu(imeprezime, email, vrsta, datum):
    conn = sqlite3.connect("upi_projekt.db")
    putnik_test = False
    karta_test = False
    try:
        
        cur = conn.cursor()

        cur.execute("SELECT email FROM putnik")
        putnici = cur.fetchall()
        for putnik in putnici:
            if putnik == email: putnik_test = True

        cur.execute("SELECT vrsta FROM karta")
        karte = cur.fetchall()
        for karta in karte:
            if karta == vrsta: karta_test = True
        
        if putnik_test == False:
            cur.execute("INSERT INTO putnik (ime_prezime, email) VALUES (?, ?)", (imeprezime, email))
        if karta_test == False:
            cur.execute("INSERT INTO karta (vrsta) VALUES (?)", (vrsta,))

        cur.execute("SELECT id FROM putnik WHERE email = ?", (email,))
        id_putnik = cur.fetchone()
        id_putnik = id_putnik[0]
        cur.execute("SELECT id FROM karta WHERE vrsta = ?", (vrsta,))
        id_karta = cur.fetchone()
        id_karta = id_karta[0]
        cur.execute("INSERT INTO kartaputnik (id_karta, id_putnik, datum) VALUES (?, ?, ?)", (id_karta, id_putnik, datum))
        conn.commit()

        print("uspjesno dodana nova karta u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju nove karte u bazu podataka: ", e)
        conn.rollback()
    
    conn.close()

def izbrisi_kartu(karta_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:
        print(karta_id)
        cur = conn.cursor()
        cur.execute("DELETE FROM kartaputnik WHERE id=?;", (karta_id))
        conn.commit()

        print("uspjesno izbrisana karta iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri brisanju karte iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dohvati_kartu_po_id(karta_id):
    conn = sqlite3.connect("upi_projekt.db")
    karta = []
    try:

        cur = conn.cursor()
        cur.execute("""SELECT * FROM putnik INNER JOIN kartaputnik
                    ON kartaputnik.id_putnik = putnik.id INNER JOIN karta
                    ON kartaputnik.id_karta = karta.id
                    WHERE kartaputnik.id=?""", karta_id)
        podaci = cur.fetchone()

        karta.append(Putnik(podaci[0], podaci[1], podaci[2]))
        karta.append(KartaPutnik(podaci[3], podaci[4], podaci[5], podaci[6]))
        karta.append(Karta(podaci[7], podaci[8]))

        print("uspjesno dohvacena karta iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju karte iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return karta

def azuriraj_kartu(karta_id, ime_prezime, email, vrsta, datum):
    conn = sqlite3.connect("upi_projekt.db")
    karta_test = False
    try:

        cur = conn.cursor()
        cur.execute("SELECT id_putnik FROM kartaputnik WHERE id=?", karta_id)
        id_putnik = cur.fetchone()
        id_putnik = id_putnik[0]
        cur.execute("UPDATE putnik SET ime_prezime=?, email=? WHERE id=?", (ime_prezime, email, id_putnik))
        
        cur.execute("SELECT vrsta FROM karta")
        lista_vrsta = cur.fetchall()
        print("lista")
        print(lista_vrsta)
        for v in lista_vrsta:
            if v[0] == vrsta:
                karta_test = True
        
        if karta_test == False:
            cur.execute("INSERT INTO karta (vrsta) VALUES (?)", (vrsta,))
        
        cur.execute("SELECT id FROM karta WHERE vrsta=?", (vrsta,))
        id_karta = cur.fetchone()
        id_karta = id_karta[0]
        
        cur.execute("UPDATE kartaputnik SET id_karta=? WHERE id=?", (id_karta, karta_id))

        cur.execute("UPDATE kartaputnik SET datum=? WHERE id=?", (datum, karta_id))
        
        conn.commit()

        print("uspjesno azurirana karta iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri azuriranju karte iz baze podataka: ", e)
        conn.rollback()

    conn.close()

