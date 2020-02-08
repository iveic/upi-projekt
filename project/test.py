import unittest
import os, sys, sqlite3

from baza import *

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from korisnik import Korisnik
from putnik import Putnik

class TestMethods(unittest.TestCase):

    def test_init_username_error(self):
        with self.assertRaises(ValueError):
            Korisnik("", "user x", "", "")

    def test_init_password_error(self):
        with self.assertRaises(ValueError):
            Korisnik("", "", "123", "")

    def test_init_email_error(self):
        with self.assertRaises(ValueError):
            Putnik("", "", "mail")

    def test_init_sacuvaj_novu_kartu(self):
        lista_unos = ["ImePrezime1", "mail_1@gmail.com", "mjesecna", "2020-01-05", "grad"]
        sacuvaj_novu_kartu(lista_unos[0], lista_unos[1], lista_unos[2], lista_unos[3], lista_unos[4])
        
        l = procitaj_sve_podatke()
        i = len(l) - 1
        lista_rezultat = [l[i][0].ime_prezime, l[i][0].email, l[i][2].vrsta, l[i][1].datum, l[i][3].vrsta]

        self.assertEqual(lista_rezultat, (lista_unos))
        print("\nsacuvaj_novu_kartu")
        print("Unešeni podaci")
        print(lista_unos)
        print("Rezultat")
        print(lista_rezultat)

    def test_init_azuriraj_kartu(self):
        lista_unos = ["2", "ImePrezime2", "mail_12@gmail.com", "godisnja", "2019-03-12", "prigradsko"]
        azuriraj_kartu(lista_unos[0], lista_unos[1], lista_unos[2], lista_unos[3], lista_unos[4], lista_unos[5])

        l = dohvati_kartu_po_id("2")
        lista_rezultat = [str(l[2].id), l[0].ime_prezime, l[0].email, l[2].vrsta, l[1].datum, l[3].vrsta]

        self.assertEqual(lista_rezultat, (lista_unos))
        print("\nazuriraj_kartu")
        print("Unešeni podaci")
        print(lista_unos)
        print("Rezultat")
        print(lista_rezultat)

    def test_init_dodaj_novu_vrstu_karte(self):
        unos = "nova vrsta"
        dodaj_novu_vrstu_karte(unos)

        l = sve_karte()
        i = len(l) - 1
        rezultat = l[i]
        
        self.assertEqual(rezultat, (unos))
        print("\ndodaj_novu_vrstu_karte")
        print("Unešeni podaci")
        print(unos)
        print("Rezultat")
        print(rezultat)

    def test_init_dodaj_novu_zonu(self):
        unos = "zona"
        dodaj_novu_zonu(unos)

        l = sve_zone()
        i = len(l) - 1
        rezultat = l[i]

        self.assertEqual(rezultat, (unos))
        print("\ndodaj_novu_zonu")
        print("Unešeni podaci")
        print(unos)
        print("Rezultat")
        print(rezultat)

    def test_init_dodaj_novu_vrstu_podrucja(self):
        unos = "podrucje"
        dodaj_novu_vrstu_podrucja(unos, 1)

        l = sva_podrucja()
        i = len(l) - 1
        rezultat = l[i]

        self.assertEqual(rezultat, (unos))
        print("\ndodaj_novu_vrstu_podrucja")
        print("Unešeni podaci")
        print(unos)
        print("Rezultat")
        print(rezultat)

    def test_init_stvaranje_novog_korisnika(self):
        unos = ["korisnik", "password", 0]
        stvaranje_novog_korisnika(unos[0], unos[1], unos[2])

        l = procitaj_podatke_korisnik()
        i = len(l) - 1
        rezultat = [l[i].username, l[i].password, l[i].admin]

        self.assertEqual(rezultat, (unos))
        print("\nstvaranje_novog_korisnika")
        print("Unešeni podaci")
        print(unos)
        print("Rezultat")
        print(rezultat)

unittest.main()
