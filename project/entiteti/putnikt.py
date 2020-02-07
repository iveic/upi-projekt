class Putnik():

    def __init__(idd, ime_prezime, email):
        if "@" not in email:
            raise ValueError("Mail mora sadržavati @")
        
        Putnik._id = idd
        Putnik._ime_prezime = ime_prezime
        Putnik._email = email

    @property
    def id(self):
        return Putnik._id

    @property
    def ime_prezime(self):
        return Putnik._ime_prezime

    @property
    def email(self):
        return Putnik._email

    def __str__(self):
        return"""
        id: {0}
        ime_prezime: {1}
        email: {2}
        ------------------------
        """.format(Putnik._id, Putnik._ime_prezime, Putnik._email)
