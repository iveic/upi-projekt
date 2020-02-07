from bottle import Bottle, run, \
     template, debug, get, request, redirect, post, route, static_file

import os, sys

from datetime import date

from baza import *

login = False
trenutni_korisnik = ""
admin = False

#poziv funkcije koja napuni bazu testnim podacima
unesi_demo_podatke()

#citanje svih podataka iz baze
procitaj_sve_podatke()

dirname = os.path.dirname(sys.argv[0])
template_path = dirname + '\\views'
app = Bottle()
debug(True)

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.css.map>')
def send_cssmap(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'/static/assets/js')

@app.route('/static/<filename:re:.*\.js.map>')
def send_jsmap(filename):
    return static_file(filename, root=dirname+'/static/assets/js')

@app.route('/info')
def info():
    #vrati template info
    return template('info', data = None, template_lookup=[template_path])

@app.route('/ispis-karata')
def ispis_karata():
    karte = procitaj_sve_podatke()
    
    file = open("karte_ispis.txt", "w")
    for karta in karte:
        file.write(str(karta[1].id) + "\t")
        file.write(karta[0].ime_prezime + "\t")
        file.write(karta[0].email + "\t\t")
        file.write(karta[2].vrsta + "\t\t")
        file.write(str(karta[1].datum) + "\n")

    file.close()
    redirect('/crud-primjer')

@app.route('/crud-primjer')
def crud_primjer():
    global login, trenutni_korisnik, admin
    if login == True:
        provjera = provjera_admin(trenutni_korisnik)
        if provjera == True:
            admin = True
            podaci = procitaj_sve_podatke()
            return template('crud-primjer', data = podaci, template_lookup=[template_path])
        else:
            admin = False
            podaci = procitaj_sve_podatke_korisnik(trenutni_korisnik)
            return template('crud-primjer-korisnik', data = podaci, template_lookup=[template_path])
    else:
        return template('prijava', data = None, form_akcija="provjera", template_lookup=[template_path])

@app.route('/crud-primjer-nova-karta')
def crud_primjer_nova_karta():
    #vrati template s formom za unos novog profesora
    listaPodrucja = sva_podrucja()
    listaKarata = sve_karte()
    if admin == True:
        return template('forma', data=None, podaciP=listaPodrucja, podaciK=listaKarata, form_akcija="/crud-primjer-nova-karta-save", template_lookup=[template_path])
    else:
        return template('forma-korisnik', data=None, podaciP=listaPodrucja, podaciK=listaKarata, form_akcija="/crud-primjer-nova-karta-save-korisnik", template_lookup=[template_path])

@app.route('/crud-primjer-nova-karta-save', method='POST')
def crud_primjer_nova_karta_save():
    postdata = request.body.read()

    #dohvacamo podatke po atributu "name" definiranog u input elementu forme
    ime_prezime = request.forms.get("imeprezime")
    email = request.forms.get("email")
    vrsta = request.forms.get("vrsta")
    datum = request.forms.get("datum")
    podrucje = request.forms.get("podrucje")
    
    #sacuvaj kartu u bazu
    sacuvaj_novu_kartu(ime_prezime, email, vrsta, datum, podrucje)

    #redirektaj korisnika na pocetnu stranicu
    redirect('/crud-primjer')

@app.route('/crud-primjer-nova-karta-save-korisnik', method='POST')
def crud_primjer_nova_karta_save_korisnik():
    postdata = request.body.read()

    #dohvacamo podatke po atributu "name" definiranog u input elementu forme
    ime_prezime = trenutni_korisnik
    email = request.forms.get("email")
    vrsta = request.forms.get("vrsta")
    datum = date.today()
    podrucje = request.forms.get("podrucje")
    
    #sacuvaj kartu u bazu
    sacuvaj_novu_kartu(ime_prezime, email, vrsta, datum, podrucje)

    #redirektaj korisnika na pocetnu stranicu
    redirect('/crud-primjer')

@app.route('/crud-primjer-azuriraj-kartu')
def crud_primjer_azuriraj_kartu():
    #dohvati id od karte iz query parametara
    karta_id = request.query['kartaid']

    #dohvati sve podatke karte iz baze podataka
    karta = dohvati_kartu_po_id(karta_id)
    print(karta)

    listaPodrucja = sva_podrucja()
    listaKarata = sve_karte()

    #vrati template s formom za unos novog profesora
    if admin == True:
        return template('forma', data=karta, podaciP=listaPodrucja, podaciK=listaKarata, form_akcija="/crud-primjer-azuriraj-kartu-save", template_lookup=[template_path])
    else:
        return template('forma-korisnik', data=karta, podaciP=listaPodrucja, podaciK=listaKarata, form_akcija="/crud-primjer-azuriraj-kartu-save", template_lookup=[template_path])

@app.route('/crud-primjer-azuriraj-kartu-save', method='POST')
def crud_primjer_azuriraj_kartu_save():

    #dohvacamo podatke po atributu "name" definiranog u input elementu forme
    karta_id = request.forms.get("kartaid")
    ime_prezime = request.forms.get("imeprezime")
    email = request.forms.get("email")
    vrsta = request.forms.get("vrsta")
    datum = request.forms.get("datum")
    podrucje = request.forms.get("podrucje")

    #azuriraj kartu u bazi s novim vrijednostima
    azuriraj_kartu(karta_id, ime_prezime, email, vrsta, datum, podrucje)

    #redirektaj korisnika na pocetnu stranicu
    redirect('/crud-primjer')

@app.route('/crud-primjer-izbrisi-kartu')
def crud_primjer_izbrisi_kartu():

    #dohvati id od profesora iz query parametara
    karta_id = request.query['kartaid']

    #izbrisi profesora iz baze
    izbrisi_kartu(karta_id)

    #redirektaj korisnika na pocetnu stranicu
    redirect('/crud-primjer')

@app.route('/nova-karta')
def nova_karta():
    return template('nova-karta', data=None, form_akcija="/nova-vrsta-karte-save", template_lookup=[template_path])

@app.route('/nova-vrsta-karte-save', method='POST')
def nova_vrsta_karte_save():
    vrsta = request.forms.get("vrstakarte")
    dodaj_novu_vrstu_karte(vrsta)
    redirect('/crud-primjer')

@app.route('/novo-podrucje')
def novo_podrucje():
    zone = sve_zone()
    return template('novo-podrucje', data=zone, form_akcija="/nova-vrsta-podrucja-save", template_lookup=[template_path])

@app.route('/nova-vrsta-podrucja-save', method=['GET', 'POST'])
def nova_vrsta_podrucja():
    vrsta = request.forms.get("vrstapodrucja")
    zona = request.forms.get("zona")
    dodaj_novu_vrstu_podrucja(vrsta, zona)
    redirect('/crud-primjer')

@app.route('/nova-zona')
def nova_zona():
    return template('nova-zona', data=None, form_akcija="/nova-zona-save", template_lookup=[template_path])

@app.route('/nova-zona-save', method=['GET', 'POST'])
def nova_zona_save():
    zona = request.forms.get("zona")
    dodaj_novu_zonu(zona)
    redirect('/crud-primjer')

@app.route('/provjera', method=['GET', 'POST'])
def provjera():
    global login, trenutni_korisnik
    postdata = request.body.read()
    user = request.forms.get("login_username")
    lozinka = str(request.forms.get("login_password"))
    svi_korisnici = procitaj_podatke_korisnik()
    for korisnik in svi_korisnici:
        if (korisnik.username == user):
            if (korisnik.password == lozinka):
                login = True
                trenutni_korisnik = korisnik.username
                print(trenutni_korisnik)
                redirect('crud-primjer')
            else:
                redirect('prijava')
    redirect('info')

@app.route('/prijava')
def prijava():
    return template('prijava', data = None, form_akcija="provjera", template_lookup=[template_path])

@app.route('/provjera-singup', method=['GET', 'POST'])
def provjera_singup():
    postdata = request.body.read()
    user = request.forms.get("singup_username")
    lozinka = str(request.forms.get("singup_password"))
    admin = False

    stvaranje_novog_korisnika(user, lozinka, admin)
    procitaj_podatke_korisnik()
    redirect('prijava')

@app.route('/provjera-singup-admin', method=['GET', 'POST'])
def provjera_singup_admin():
    postdata = request.body.read()
    user = request.forms.get("singup_username")
    lozinka = str(request.forms.get("singup_password"))
    admin = request.forms.get("admin")
    if admin == None:
        admin = False
    else:
        admin = True
    
    stvaranje_novog_korisnika(user, lozinka, admin)
    procitaj_podatke_korisnik()
    redirect('prijava')

@app.route('/novi-korisnik')
def novi_korisnik():
    if login == False or (login == True and admin == False):
        return template('novi-korisnik', data = None, form_akcija="provjera-singup", template_lookup = [template_path])
    elif login == True and admin == True:
        return template('novi-korisnik-admin', data = None, form_akcija="provjera-singup-admin", template_lookup = [template_path])

@app.route('/odjava')
def odjava():
    global login, trenutni_korisnik
    login = False
    trenutni_korisnik = ""
    redirect('info')


@app.route('/')
def index():
    data = {"developer_name": "PMF student",
            "developer_organization": "PMF"}
    return template('C:\\Users\\Josip\\Desktop\\project2\\views\\index.tpl', data = data, template_lookup=[template_path])

run(app, host='localhost', port = 8085)
