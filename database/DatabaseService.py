import mysql.connector
from utils.Generation import generateToken
from database.actions import FetchAllTechniker, LoginAction, AddUserToken


class DatabaseService(object):
    conn = None

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="10.11.0.3",
            password="LgdQJUcBKd5AEtaF",
            user="wr-paging",
            database="wr-paging",
            auth_plugin="mysql_native_password"
        )

    def drop(self):
        self.conn.close()

    def FetchAllTechniker(self):
        return FetchAllTechniker.execute(self.conn)

    def Login(self, vorname, nachname, password):
        status = LoginAction.execute(self.conn, vorname=vorname, name=nachname, pwd=password)
        if status:
            token = generateToken()
            owner = vorname + '.' + nachname
            AddUserToken.execute(self.conn, owner=owner, token=token)
            return True, token
        else:
            return False, None

