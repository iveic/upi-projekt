class Podrucje():

    #grad/urbano/prigradsko
    def __init__(self, id, vrsta):
        self._id = id
        self._vrsta = vrsta

    @property
    def id(self):
        return self._id

    @property
    def vrsta(self):
        return self._vrsta

    def __str__(self):
        return"""
        id: {0}
        vrsta: {1}
        ------------------------
        """.format(self._id, self._vrsta)
