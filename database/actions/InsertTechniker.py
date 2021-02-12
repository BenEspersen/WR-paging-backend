from contextlib import closing
from utils.Hashing import Hash


def execute(conn, user_info):
    with closing(conn.cursor()) as cursor:
        stmt = "insert into techniker(id, Name, Vorname, Klasse, Schlüssel, Ausbildungen, Aufgaben, aktuellerAuftrag, " \
               "passwort, status, timestamp) values (null, %s, %s, %s, %s, %s, %s, '', %s, 0, current_timestamp())"
        cursor.execute(stmt, (
            user_info.get("name"),
            user_info.get("vorname"),
            user_info.get("klasse"),
            user_info.get("schluessel"),
            user_info.get("ausbildungen"),
            user_info.get("aufgaben"),
            Hash(user_info.get("password"))
        ))
        conn.commit()
