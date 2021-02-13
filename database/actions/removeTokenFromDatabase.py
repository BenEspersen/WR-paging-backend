from contextlib import closing


def execute(conn, token, owner):
    with closing(conn.cursor()) as cursor:
        cursor.execute("delete from token where token=%s and owner=%s", (token, owner))
        conn.commit()