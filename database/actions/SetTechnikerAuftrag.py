from contextlib import closing


def execute(conn, auftragsID, username):
    arr = str(username).split(".")
    with closing(conn.cursor()) as cursor:
        cursor.execute("update techniker set aktuellerAuftrag=%s where Vorname=%s and Name=%s",
                       (auftragsID, arr[0], arr[1]))
        conn.commit()
