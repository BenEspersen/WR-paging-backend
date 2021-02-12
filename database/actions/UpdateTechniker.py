from contextlib import closing


def execute(conn, category, value, token_owner):
    arr = str(token_owner).split(".")
    with closing(conn.cursor()) as cursor:
        cursor.execute("update techniker set " + category + "=%s where Name=%s and Vorname=%s",
                       (value, arr[1], arr[0]))
        conn.commit()
