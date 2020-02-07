import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from karta import Karta
from putnik import Putnik
from podrucje import Podrucje
from zona import Zona
from veza import Veza
from korisnik import Korisnik

def unesi_demo_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()

        #putnik
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

        #karta
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

        #zona
        cur.executescript("""

        DROP TABLE IF EXISTS zona;

        CREATE TABLE zona (
        id INTEGER PRIMARY KEY,
        broj_zone INTEGER);
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
        vrsta TEXT,
        id_zona INTEGER,
        FOREIGN KEY (id_zona) REFERENCES zona (id));
        """)

        print("uspjesno kreirana tablica podrucje!")

        cur.execute("INSERT INTO podrucje (vrsta, id_zona) VALUES (?, ?)", ("grad", 1))
        cur.execute("INSERT INTO podrucje (vrsta, id_zona) VALUES (?, ?)", ("prigradsko", 2))

        print("uspjesno uneseni tesni podaci u tablicu podrucje!")

        #veza
        cur.executescript("""

        DROP TABLE IF EXISTS veza;

        CREATE TABLE veza (
        id INTEGER PRIMARY KEY,
        id_karta INTEGER,
        id_putnik INTEGER,
        id_podrucje INTEGER,
        datum DATE,
        FOREIGN KEY (id_karta) REFERENCES karta (id),
        FOREIGN KEY (id_putnik) REFERENCES putnik (id),
        FOREIGN KEY (id_podrucje) REFERENCES podrucje (id));
        """)

        print("uspjesno kreirana tablica karta!")

        cur.execute("INSERT INTO veza (id_karta, id_putnik, id_podrucje, datum) VALUES (?, ?, ?, ?)", (1, 1, 1, "2020-01-05"))
        cur.execute("INSERT INTO veza (id_karta, id_putnik, id_podrucje, datum) VALUES (?, ?, ?, ?)", (2, 2, 2, "2019-03-12"))

        print("uspjesno uneseni testni podaci u tablicu karta!")

        #korisnik
        cur.executescript("""

        DROP TABLE IF EXISTS korisnik;

        CREATE TABLE korisnik (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        admin BOOL NOT NULL);
        """)

        print("uspjesno kreirana tablica korisnika!")

        cur.execute("INSERT INTO korisnik (username, password, admin) VALUES (?, ?, ?)", ("admin1", "admin1", True))

        print("uspjesno uneseni testni podaci u tablicu korisnika!")
                
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
        cur.execute("""SELECT * FROM putnik INNER JOIN veza
                    ON veza.id_putnik = putnik.id INNER JOIN karta
                    ON veza.id_karta = karta.id INNER JOIN podrucje
                    ON veza.id_podrucje = podrucje.id INNER JOIN zona
                    ON podrucje.id_zona = zona.id""")

        podaci = cur.fetchall()
        print(podaci)
        
        for e in podaci:
            lista = []
            lista.append(Putnik(e[0], e[1], e[2]))
            lista.append(Veza(e[3], e[4], e[5], e[6], e[7]))
            lista.append(Karta(e[8], e[9]))
            lista.append(Podrucje(e[10], e[11], e[12]))
            lista.append(Zona(e[13], e[14]))
            lista_podataka.append(lista)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice karte: ", e)
        conn.rollback()

    conn.close()
    return lista_podataka

def procitaj_sve_podatke_korisnik(korisnik):
    conn = sqlite3.connect("upi_projekt.db")
    lista_podataka = []
    try:

        cur = conn.cursor()
        cur.execute("""SELECT * FROM putnik INNER JOIN veza
                    ON veza.id_putnik = putnik.id INNER JOIN karta
                    ON veza.id_karta = karta.id INNER JOIN podrucje
                    ON veza.id_podrucje = podrucje.id INNER JOIN zona
                    ON podrucje.id_zona = zona.id WHERE putnik.ime_prezime=?""", (korisnik,))

        podaci = cur.fetchall()
        print(podaci)
        
        for e in podaci:
            lista = []
            lista.append(Putnik(e[0], e[1], e[2]))
            lista.append(Veza(e[3], e[4], e[5], e[6], e[7]))
            lista.append(Karta(e[8], e[9]))
            lista.append(Podrucje(e[10], e[11], e[12]))
            lista.append(Zona(e[13], e[14]))
            lista_podataka.append(lista)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice karte: ", e)
        conn.rollback()

    conn.close()
    return lista_podataka


def sacuvaj_novu_kartu(imeprezime, email, vrsta, datum, podrucje):
    conn = sqlite3.connect("upi_projekt.db")
    putnik_test = False
    try:
        
        cur = conn.cursor()
        cur.execute("SELECT email FROM putnik")
        putnici = cur.fetchall()
        for putnik in putnici:
            if putnik == email: putnik_test = True
        
        if putnik_test == False:
            cur.execute("INSERT INTO putnik (ime_prezime, email) VALUES (?, ?)", (imeprezime, email))

        cur.execute("SELECT id FROM putnik WHERE email = ?", (email,))
        id_putnik = cur.fetchone()
        id_putnik = id_putnik[0]
        
        cur.execute("SELECT id FROM karta WHERE vrsta = ?", (vrsta,))
        id_karta = cur.fetchone()
        id_karta = id_karta[0]

        cur.execute("SELECT id FROM podrucje WHERE vrsta=?", (podrucje,))
        id_podrucje = cur.fetchone()
        id_podrucje = id_podrucje[0]
        
        cur.execute("INSERT INTO veza (id_karta, id_putnik, id_podrucje, datum) VALUES (?, ?, ?, ?)", (id_karta, id_putnik, id_podrucje, datum))
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
        cur.execute("DELETE FROM veza WHERE id=?;", (karta_id))
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
        cur.execute("""SELECT * FROM putnik INNER JOIN veza
                    ON veza.id_putnik = putnik.id INNER JOIN karta
                    ON veza.id_karta = karta.id INNER JOIN podrucje
                    ON veza.id_podrucje = podrucje.id
                    WHERE veza.id=?""", karta_id)
        podaci = cur.fetchone()

        karta.append(Putnik(podaci[0], podaci[1], podaci[2]))
        karta.append(Veza(podaci[3], podaci[4], podaci[5], podaci[6], podaci[7]))
        karta.append(Karta(podaci[8], podaci[9]))
        karta.append(Podrucje(podaci[10], podaci[11], podaci[12]))

        print("uspjesno dohvacena karta iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju karte iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return karta

def azuriraj_kartu(karta_id, ime_prezime, email, vrsta, datum, podrucje):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("SELECT id_putnik FROM veza WHERE id=?", karta_id)
        id_putnik = cur.fetchone()
        id_putnik = id_putnik[0]
        cur.execute("UPDATE putnik SET ime_prezime=?, email=? WHERE id=?", (ime_prezime, email, id_putnik))
        
        cur.execute("SELECT id FROM karta WHERE vrsta=?", (vrsta,))
        id_karta = cur.fetchone()
        id_karta = id_karta[0]

        cur.execute("SELECT id FROM podrucje WHERE vrsta=?", (podrucje,))
        id_podrucje = cur.fetchone()
        id_podrucje = id_podrucje[0]
        
        cur.execute("UPDATE veza SET id_karta=? WHERE id=?", (id_karta, karta_id))

        cur.execute("UPDATE veza SET datum=? WHERE id=?", (datum, karta_id))

        cur.execute("UPDATE veza SET id_podrucje=? WHERE id=?", (id_podrucje, karta_id))
        
        conn.commit()

        print("uspjesno azurirana karta iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri azuriranju karte iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dodaj_novu_vrstu_karte(nova_vrsta):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO karta (vrsta) VALUES (?)", (nova_vrsta,))
        conn.commit()
        
    except Exception as e: 
        print("Dogodila se greska pri unosu nove vrste karte: ", e)
        conn.rollback()

    conn.close()

def dodaj_novu_vrstu_podrucja(novo_podrucje, zona):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO podrucje (vrsta, id_zona) VALUES (?, ?)", (novo_podrucje, zona))
        print("uspjesno uneseno novo podrucje!")
        conn.commit()

    except Exception as e: 
        print("Dogodila se greska pri unosu nove vrste podrucja: ", e)
        conn.rollback()

    conn.close()

def dodaj_novu_zonu(zona):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO zona (broj_zone) VALUES (?)", (zona,))
        print("uspjesno unesena nova zona!")
        conn.commit()

    except Exception as e: 
        print("Dogodila se greska pri unosu nove zone: ", e)
        conn.rollback()

    conn.close()

def procitaj_podatke_korisnik():
    con=sqlite3.connect("upi_projekt.db")
    lista_korisnika=[]
    try:
        cur=con.cursor()
        cur.execute(""" SELECT id,username,password, admin FROM korisnik """)
        
        podaci=cur.fetchall()

        for kor in podaci:
            # 0 - id
            # 1 - e_mail
            # 2 - lozinka
            # 3 - admin

            k=Korisnik(kor[0],kor[1],kor[2], kor[3])
            lista_korisnika.append(k)

        print ("Uspjesno dohvaceni svi podaci iz tablice korisnika")

        for k in lista_korisnika:
            print(k)
        
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice korisnika: ",e)
        con.rollback()

    con.close()
    return lista_korisnika

def provjera(username, password):

    conn=sqlite3.connect("upi_projekt.db")
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

def stvaranje_novog_korisnika(username, password, admin):

    conn=sqlite3.connect("upi_projekt.db")
    postoji = False
    try:

        cur = conn.cursor()
        cur.executescript("SELECT username FROM korisnik")

        korisnici = cur.fetchall()

        for k in korisnici:
            if k == username:
                postoji = True

        if postoji == False:
            cur.execute("INSERT INTO korisnik (username, password, admin) VALUES (?, ?, ?)", (username, password, admin))
        conn.commit()
    except Exception as e: 
        print("Dogodila se greska pri provjeri podataka: ", e)
        conn.rollback()
        
    conn.close()

def provjera_admin(korisnik):
    conn=sqlite3.connect("upi_projekt.db")
    provjera = False
    try:
        cur = conn.cursor()
        cur.execute("SELECT admin FROM korisnik WHERE username=?", (korisnik,))
        admin = cur.fetchone()
        provjera = admin[0]

    except Exception as e: 
        print("Dogodila se greska pri provjeri podataka: ", e)
        conn.rollback()
        
    conn.close()
    return provjera

def sve_zone():
    conn=sqlite3.connect("upi_projekt.db")
    lista = []
    try:
        cur = conn.cursor()
        cur.execute("SELECT broj_zone FROM zona")
        zone = cur.fetchall()
        for z in zone:
            lista.append(z[0])

    except Exception as e: 
        print("Dogodila se greska pri citanju podataka: ", e)
        conn.rollback()
        
    conn.close()
    return lista

def sva_podrucja():
    conn=sqlite3.connect("upi_projekt.db")
    lista = []
    try:
        cur = conn.cursor()
        cur.execute("SELECT vrsta FROM podrucje")
        podrucje = cur.fetchall()
        for p in podrucje:
            lista.append(p[0])

    except Exception as e: 
        print("Dogodila se greska pri citanju podataka: ", e)
        conn.rollback()
        
    conn.close()
    return lista

def sve_karte():
    conn=sqlite3.connect("upi_projekt.db")
    lista = []
    try:
        cur = conn.cursor()
        cur.execute("SELECT vrsta FROM karte")
        karta = cur.fetchall()
        for k in karta:
            lista.append(k[0])

    except Exception as e: 
        print("Dogodila se greska pri citanju podataka: ", e)
        conn.rollback()
        
    conn.close()
    return lista
