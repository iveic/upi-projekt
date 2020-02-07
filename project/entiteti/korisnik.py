class Korisnik():

    def __init__(self, id, username, password, admin):
        self._id = id
        self._username = username
        self._password = password
        self._admin = admin

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def admin(self):
        return self._admin

    def __str__(self):
        return"""
        id: {0}
        username: {1}
        password: {2}
        admin: {3}
        ------------------------
        """.format(self._id, self._username, self._password, self._admin)
