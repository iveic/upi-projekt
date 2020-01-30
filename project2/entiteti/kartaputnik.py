class KartaPutnik():

    def __init__(self, id, id_karta, id_putnik, datum):
        self._id = id
        self._id_karta = id_karta
        self._id_putnik = id_putnik
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
    def datum(self):
        return self._datum

    def __str__(self):
        return"""
        id: {0}
        id_karta: {1}
        id_putnik: {2}
        datum: {3}
        ------------------------
        """.format(self._id, self._id_karta, self._id_putnik, self._datum)
