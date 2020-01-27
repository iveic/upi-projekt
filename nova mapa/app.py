from bottle import Bottle, run, \
     template, debug, get, request, redirect, post, route, static_file

import os, sys

#from baza import procitaj_sve_podatke, sacuvaj_novu_kartu, dohvati_kartu_po_id, azuriraj_kartu, izbrisi_kartu
from baza import unesi_demo_podatke, procitaj_sve_podatke, sacuvaj_novu_kartu, izbrisi_kartu, azuriraj_kartu, dohvati_kartu_po_id
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


@app.route('/crud-primjer')
def crud_primjer():
    procitaj_sve = procitaj_sve_podatke()
    podaci = []
    #print(procitj_sve)
    for p in procitaj_sve:
        lista = []
        lista.append(p[0].id)
        lista.append(p[0].ime_prezime)
        lista.append(p[0].godiste)
        lista.append(p[0].mjesto_stanovanja)
        lista.append(p[1].datum_izrade)
        lista.append(p[1].vrsta)
        lista.append(p[2].vrsta)
        lista.append(p[3].broj_zone)
        podaci.append(lista)
        #print("!")
    #print(podaci)
    return template('crud-primjer', data = podaci, template_lookup=[template_path])

@app.route('/crud-primjer-nova-karta')
def crud_primjer_nova_karta():
    #vrati template s formom za unos nove karte
    return template('forma', data=None, form_akcija="/crud-primjer-nova-karta-save", template_lookup=[template_path])


@app.route('/crud-primjer-nova-karta-save', method='POST')
def crud_primjer_nova_karta_save():
    postdata = request.body.read()

    #dohvaćamo podatke po atributu "name" definiranog u input elementu forme
    ime_prezime = request.forms.get("imeprezime")
    godiste = int(request.forms.get("godiste"))
    mjesto_stanovanja = request.forms.get("mjestostanovanja")
    datum_izrade = request.forms.get("datumizrade")
    vrsta_karte = request.forms.get("vrsta")
    vrsta_podrucja = request.forms.get("podrucje")
    zona = int(request.forms.get("zona"))

    #sacuvaj kartu u bazu
    sacuvaj_novu_kartu(datum_izrade, vrsta_karte, ime_prezime, godiste, mjesto_stanovanja, zona, vrsta_podrucja)

    #redirektaj korisnika na pocetnu stranicu
    redirect('/crud-primjer')


@app.route('/crud-primjer-azuriraj-kartu')
def crud_primjer_azuriraj_kartu():
    #dohvati id od karte iz query parametara
    karta_id = request.query['kartaid']

    #dohvati sve podatke karte iz baze podataka
    karta = dohvati_kartu_po_id(karta_id)

    #vrati template s formom za unos novog profesora
    return template('forma', data=karta, form_akcija="/crud-primjer-azuriraj-kartu-save", template_lookup=[template_path])


@app.route('/crud-primjer-azuriraj-kartu-save', method='POST')
def crud_primjer_azuriraj_kartu_save():

     #dohvaćamo podatke po atributu "name" definiranog u input elementu forme
    karta_id = request.forms.get("kartaid")
    ime_prezime = request.forms.get("imeprezime")
    godiste = int(request.forms.get("godiste"))
    mjesto_stanovanja = request.forms.get("mjestostanovanja")
    datum_izrade = request.forms.get("datumizrade")
    vrsta_karte = request.forms.get("vrsta")
    vrsta_podrucja = request.forms.get("podrucje")
    zona = int(request.forms.get("zona"))

    #azuriraj kartu u bazi s novim vrijednostima
    azuriraj_kartu(karta_id, ime_prezime, godiste, mjesto_stanovanja, datum_izrade, vrsta_karte, vrsta_podrucja, zona)

    #redirektaj korisnika na pocetnu stranicu
    redirect('/crud-primjer')


@app.route('/crud-primjer-izbrisi-kartu')
def crud_primjer_izbrisi_kartu():

    #dohvati id karte iz query parametara
    karta_id = request.query['kartaid']
    print(karta_id)
    #izbrisi kartu iz baze
    izbrisi_kartu(karta_id)

    #redirektaj korisnika na pocetnu stranicu
    redirect('/crud-primjer')

@app.route('/')
def index():
    data = {"developer_name": "PMF student",
            "developer_organization": "PMF"}
    return template('C:\\Users\\Josip\\Desktop\\E\\F\\3. godina\\5. semestar\\UPI\\project2\\views\\index.tpl', data = data, template_lookup=[template_path])

run(app, host='localhost', port = 8085)
