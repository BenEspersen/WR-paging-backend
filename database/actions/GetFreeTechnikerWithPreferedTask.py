from contextlib import closing
from database.models.Techniker import TechnikerModel


def execute(conn, aufgabe):
    with closing(conn.cursor(buffered=True)) as cursor:
        query = "select * from techniker where aktuellerAuftrag='' and Aufgaben LIKE '%" + aufgabe + "%'"
        cursor.execute(query)
        mdl = cursor.fetchone()
    if mdl is None:
        return None
    else:
        return TechnikerModel(mdl)
