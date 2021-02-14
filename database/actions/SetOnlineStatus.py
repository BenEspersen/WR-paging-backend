from contextlib import closing


def execute(conn, username, status):
    arr = str(username).split(".")
    with closing(conn.cursor()) as cursor:
        cursor.execute("update techniker set status=%s where Vorname=%s and Name=%s", (status, arr[0], arr[1]))
        conn.commit()
