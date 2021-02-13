from contextlib import closing
from database.models.Techniker import TechnikerModel


def execute(conn, username):
    with closing(conn.cursor()) as cursor:
        arr = str(username).split(".")
        cursor.execute("select * from techniker where Vorname=%s and Name=%s", (arr[0], arr[1]))
        rows = cursor.fetchone()
    return TechnikerModel(rows).aktuellerAuftrag
