from contextlib import closing


def execute(conn, taskID):
    with closing(conn.cursor()) as cursor:
        cursor.execute("update aufgaben set status='2' where id=" + str(taskID))
        conn.commit()
