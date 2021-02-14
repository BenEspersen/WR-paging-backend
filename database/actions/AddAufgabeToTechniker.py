from contextlib import closing

from database.models.Techniker import TechnikerModel


def execute(conn, username, aufgabe):
    arr = str(username).split(".")
    with closing(conn.cursor()) as cursor:
        cursor.execute("select * from techniker where Vorname=%s and Name=%s", (arr[0], arr[1]))
        value = TechnikerModel(cursor.fetchone()).Aufgaben
        value += ';' + aufgabe
        cursor.execute("update techniker set Aufgaben=%s where Vorname=%s and Name=%s", (value, arr[0], arr[1]))
        conn.commit()