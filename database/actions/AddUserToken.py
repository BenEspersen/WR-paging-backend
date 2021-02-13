from contextlib import closing


def execute(conn, owner, token):
    with closing(conn.cursor()) as cursor:
        cursor.execute("insert into token (ID, token, owner, timestamp) values (null, %s, %s, current_timestamp()) ",
                       (token, owner))
        conn.commit()
