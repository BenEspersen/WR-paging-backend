from contextlib import closing
from database.models.Auftrag import Auftrag


def execute(conn, technikerID):
    with closing(conn.cursor()) as cursor:
        cursor.execute("select * from aufgaben where technikerID like '%" + str(technikerID) + "%'")
        rows = cursor.fetchall()
    aufgaben = []
    for el in rows:
        aufgaben.append(Auftrag(el))
    return aufgaben
