class Korisnik():

    def __init__(idd, username, password, admin):
        if " " in username:
            raise ValueError("Username nesmije imati razmak")
        if " " in password:
            raise ValueError("Password nesmije imati razmak")
        if len(password)<4:
            raise ValueError("Password mora biti minimalne dužine 5")
        
        Korisnik._id = idd
        Korisnik._username = username
        Korisnik._password = password
        Korisnik._admin = admin

    @property
    def id(self):
        return Korisnik._id

    @property
    def username(self):
        return Korisnik._username

    @property
    def password(self):
        return Korisnik._password

    @property
    def admin(self):
        return Korisnik._admin

    def __str__(self):
        return"""
        id: {0}
        username: {1}
        password: {2}
        admin: {3}
        ------------------------
        """.format(Korisnik._id, Korisnik._username, Korisnik._password, Korisnik._admin)
