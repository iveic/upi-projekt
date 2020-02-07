class Podrucje():

    def __init__(self, id, vrsta, id_zona):
        self._id = id
        self._vrsta = vrsta
        self._id_zona = id_zona

    @property
    def id(self):
        return self._id
    
    @property
    def vrsta(self):
        return self._vrsta

    @property
    def id_zona(self):
        return self._id_zona

    def __str__(self):
        return"""
        id: {0}
        vrsta: {1}
        id_zona: {2}
        ------------------------
        """.format(self._id, self._vrsta, self._id_zona)
