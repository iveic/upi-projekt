class Putnik():

    def __init__(self, id, ime_prezime, email):
        if "@" not in email:
            raise ValueError("Mail mora sadržavati @")
        
        self._id = id
        self._ime_prezime = ime_prezime
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def ime_prezime(self):
        return self._ime_prezime

    @property
    def email(self):
        return self._email

    def __str__(self):
        return"""
        id: {0}
        ime_prezime: {1}
        email: {2}
        ------------------------
        """.format(self._id, self._ime_prezime, self._email)
