from contextlib import closing


def execute(conn, username):
    with closing(conn.cursor()) as cursor:
        cursor.execute("select * from token where owner=%s", (username))
        rows = cursor.fetchall()
    return len(rows)