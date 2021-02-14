from contextlib import closing


def execute(conn, username):
    with closing(conn.cursor()) as cursor:
        stmt = "select * from token where owner='" + username + "';"
        cursor.execute(stmt)
        rows = cursor.fetchall()
    return len(rows)
