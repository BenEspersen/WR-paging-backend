from contextlib import closing
from utils.Hashing import Hash


def execute(conn, vorname, name, pwd):
    with closing(conn.cursor()) as cursor:
        cursor.execute("select * from techniker where Name=%s and Vorname=%s and passwort=%s",
                       (name, vorname, Hash(pwd)))
        row = cursor.fetchall()
    return len(row) == 1
