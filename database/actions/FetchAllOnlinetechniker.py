from contextlib import closing
from database.models.Techniker import TechnikerModel
from utils.JSON import Encoder


def execute(conn):
    with closing(conn.cursor()) as cursor:
        cursor.execute("select * from techniker where status=1")
        rows = cursor.fetchall()
    techniker = []
    for el in rows:
        techniker.append(Encoder().encode(TechnikerModel(el)))
    return techniker
