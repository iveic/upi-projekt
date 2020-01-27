class Putnik():

    def __init__(self, id, ime_prezime, godiste, mjesto_stanovanja):
        self._id = id
        self._ime_prezime = ime_prezime
        self._godiste = godiste
        self._mjesto_stanovanja = mjesto_stanovanja

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
    def mjesto_stanovanja(self):
        return self._mjesto_stanovanja

    def __str__(self):
        return"""
        id: {0}
        ime_prezime: {1}
        godiste: {2}
        mjesto_stanovanja: {3}
        ------------------------
        """.format(self._id, self._ime_prezime, self._godiste, self._mjesto_stanovanja)
