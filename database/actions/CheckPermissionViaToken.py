from contextlib import closing


def execute(conn, token, owner):
    with closing(conn.cursor()) as cursor:
        cursor.execute("select * from token where token=%s and owner=%s", (token, owner))
        rows = cursor.fetchall()
    return len(rows) == 1
