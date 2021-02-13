from contextlib import closing
from database.models.Techniker import TechnikerModel


def execute(conn, name):
    arr = str(name).split(".")
    with closing(conn.cursor()) as cursor:
        cursor.execute("select * from techniker where Vorname=%s and Name=%s", (arr[0], arr[1]))
        mdl = cursor.fetchone()
    return TechnikerModel(mdl)