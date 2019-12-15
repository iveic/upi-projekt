from bottle import Bottle, run, \
     template, debug, get, route, static_file

import os, sys

dirname = os.path.dirname(sys.argv[0])

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



@app.route('/')
def index():
    data = {"developer_name": "PMF student",
            "developer_organization": "PMF"}
    #ID;Ime;Prezime;Grad;Vrsta;Mjesec izrade
    #1;Ante;Antic;Solin;Godisnja;1
    with open("baza.txt", "r") as f:
        for line in f:
            line = line.strip("\n")
            l = line.split(";")
            key = l[0]
            data[key] = l[1:]
    #dodat "w" - upis u baza.txt
    return template('C:\\Users\\Josip\\Desktop\\E\\F\\3. godina\\5. semestar\\UPI\\project\\views\\index.tpl', data = data)

run(app, host='localhost', port = 8085)
