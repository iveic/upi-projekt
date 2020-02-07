class Veza():

    def __init__(self, id, id_karta, id_putnik, id_podrucje, datum):
        self._id = id
        self._id_karta = id_karta
        self._id_putnik = id_putnik
        self._id_podrucje = id_podrucje
        self._datum = datum

    @property
    def id(self):
        return self._id
    
    @property
    def id_karta(self):
        return self._id_karta

    @property
    def id_putnik(self):
        return self._id_putnik

    @property
    def id_podrucje(self):
        return self._id_podrucje

    @property
    def datum(self):
        return self._datum

    def __str__(self):
        return"""
        id: {0}
        id_karta: {1}
        id_putnik: {2}
        id_podrucje: {3}
        datum: {4}
        ------------------------
        """.format(self._id, self._id_karta, self._id_putnik, id_podrucje, self._datum)
