from contextlib import closing


def execute(conn, auftragsID):
    with closing(conn.cursor()) as cursor:
        print(type(auftragsID))
        cursor.execute("update aufgaben set status='1' where id=" + str(auftragsID))
        conn.commit()