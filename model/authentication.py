from model.connection import getConnection
import psycopg2


def checkToken(token):
    connection = getConnection()
    cursor = connection.cursor()
    flag = False

    qry = f"SELECT * FROM user_table WHERE authtoken='{token}';"

    try:
        cursor.execute(qry)
        if len(list(cursor.fetchall())) == 1:
            flag = True
    except psycopg2.DatabaseError:
        print("db error", flush=True)

    connection.close()

    return flag


def getUsername(token):
    connection = getConnection()
    cursor = connection.cursor()
    output = ""

    qry = f"SELECT username FROM user_table WHERE authtoken='{token}';"

    try:
        cursor.execute(qry)
        results = list(cursor.fetchall())
        if len(results) == 1:
            output = results[0][0]
    except psycopg2.DatabaseError:
        print("db error", flush=True)

    connection.close()

    return output

