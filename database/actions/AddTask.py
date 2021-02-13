from contextlib import closing


def execute(conn, name, aufgabe, owner, date=None, treffpunkt=None):
    with closing(conn.cursor()) as cursor:
        if date is not None:
            if treffpunkt is not None:
                stmt = "insert into aufgaben(id, name, aufgabe, status, technikerID, date, treffpunkt, timestamp) values (null, %s, %s, 0, %s, %s, %s, current_timestamp())"
                cursor.execute(stmt, (name, aufgabe, owner, date, treffpunkt))
            else:
                stmt = "insert into aufgaben(id, name, aufgabe, status, technikerID, date, treffpunkt, timestamp) values (null, %s, %s, 0, %s, %s, 'Technikraum', current_timestamp())"
                cursor.execute(stmt, (name, aufgabe, owner, date))
        else:
            if treffpunkt is not None:
                stmt = "insert into aufgaben(id, name, aufgabe, status, technikerID, date, treffpunkt, timestamp) values (null, %s, %s, 0, %s, current_timestamp(), %s, current_timestamp())"
                cursor.execute(stmt, (name, aufgabe, owner, treffpunkt))
            else:
                stmt = "insert into aufgaben(id, name, aufgabe, status, technikerID, date, treffpunkt, timestamp) values (null, %s, %s, 0, %s, current_timestamp(), 'Technikraum', current_timestamp())"
                cursor.execute(stmt, (name, aufgabe, owner))
        conn.commit()
