class Karta():

    def __init__(self, id, datum_izrade, vrsta):
        self._id = id
        self._datum_izrade = datum_izrade
        self._vrsta = vrsta

    @property
    def id(self):
        return self._id

    @property
    def datum_izrade(self):
        return self._datum_izrade

    @property
    def vrsta(self):
        return self._vrsta

    def __str__(self):
        return"""
        id: {0}
        datum_izrade: {1}
        vrsta: {2}
        ------------------------
        """.format(self._id, self._datum_izrade, self._vrsta)
