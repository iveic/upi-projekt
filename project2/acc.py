import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from korisnik import Korisnik

def unesi_demo_korisnika():

    conn = sqlite3.connect("upi_korisnici.db")

    try:

        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS korisnik;

        CREATE TABLE korisnik (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL);
        """)

        print("uspjesno kreirana tablica korisnika!")

        cur.execute("INSERT INTO korisnik (username, password) VALUES (?, ?)", ("admin1", "admin1"))

        print("uspjesno uneseni testni podaci u tablicu korisnika!")

        conn.commit()

    except Exception as e: 
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()
        
    conn.close()

def provjera(username, password):

    conn = sqlite3.connect("upi_korisnici.db")
    provjera = False
    try:

        cur = conn.cursor()
        cur.executescript("SELECT password FROM korisnik WHERE username=?", (username))
        pass_table = cur.fetchone()

        if pass_table == password:
            provjera = True

    except Exception as e: 
        print("Dogodila se greska pri provjeri podataka: ", e)
        conn.rollback()
        
    conn.close()
    return provjera

def stvaranje_novog_korisnika(username, password):

    conn = sqlite3.connect("upi_korisnici.db")
    postoji = False
    try:

        cur = conn.cursor()
        cur.executescript("SELECT username FROM korisnik")

        korisnici = cur.fetchall()

        for k in korisnici:
            if k == username:
                postoji = True

        if postoji == False:
            cur.executescript("INSERT INTO korisnik (username, password) VALUES (?, ?)", (username, password))

    except Exception as e: 
        print("Dogodila se greska pri provjeri podataka: ", e)
        conn.rollback()
        
    conn.close()
