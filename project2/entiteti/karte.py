class Karte():

    def __init__(self, id, ime_prezime, godiste, datum_izrade, vrsta):
        self._id = id
        self._ime_prezime = ime_prezime
        self._godiste = godiste
        self._datum_izrade = datum_izrade
        self._vrsta = vrsta

    @property
    def id(self):
        return self._id

    @property
    def ime_prezime(self):
        return self._ime_prezime

    @property
    def godiste(self):
        return self._godiste

    @property
    def datum_izrade(self):
        return self._datum_izrade

    @property
    def vrsta(self):
        return self._vrsta

    def __str__(self):
        return"""
        id: {0}
        ime_prezime: {1}
        godiste: {2}
        datum_izrade: {3}
        vrsta: {4}
        ------------------------
        """.format(self._id, self._ime_prezime, self._godiste, self._datum_izrade, self._vrsta)
