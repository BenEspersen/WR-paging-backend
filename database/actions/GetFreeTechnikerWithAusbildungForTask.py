from contextlib import closing
from database.models.Techniker import TechnikerModel


def execute(conn, ausbildung):
    with closing(conn.cursor(buffered=True)) as cursor:
        query = "select * from techniker where aktuellerAuftrag='' and Ausbildungen LIKE '%" + ausbildung + "%' and status=1"
        cursor.execute(query)
        mdl = cursor.fetchall()
    techniker = []
    for tech in mdl:
        techniker.append(TechnikerModel(tech).ID)
    return techniker