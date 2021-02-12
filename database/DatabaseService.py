import mysql.connector
from database.actions import FetchAllTechniker


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
