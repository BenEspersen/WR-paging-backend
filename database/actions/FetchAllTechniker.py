from contextlib import closing
from database.models.Techniker import TechnikerModel


def execute(conn):
    with closing(conn.cursor()) as cursor:
        cursor.execute("select * from techniker")
        rows = cursor.fetchall()
    arr = []
    for el in rows:
        arr.append(TechnikerModel(el))
    return arr
