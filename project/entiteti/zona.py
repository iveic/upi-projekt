class Zona():

    def __init__(self, id, broj_zone):
        self._id = id
        self._broj_zone = broj_zone

    @property
    def id(self):
        return self._id
    
    @property
    def broj_zone(self):
        return self._broj_zone

    def __str__(self):
        return"""
        id: {0}
        broj_zone: {1}
        ------------------------
        """.format(self._id, self._broj_zone)
