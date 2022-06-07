import psycopg2
from model.connection import get_connection
from model.people import Login


def select_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM user_table WHERE username = '{username}' AND password = '{password}';"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_login = Login(record[0], record[1], record[2])
            return user_login

    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def authenticate(username, password):
    connection = getConnection()
    cursor = connection.cursor()
    output = None

    qry = f"SELECT * FROM users WHERE username='{username}' AND password='{password}';"

    try:
        cursor.execute(qry)

        results = list(cursor.fetchall())

        hashstring = str(hash(float(time.time())+random.random()))
        if len(results) == 1 and results[0][3] == 0:
            output = hashstring
            qry2 = f"UPDATE users SET authtoken='{hashstring}' WHERE username='{username}';"
            cursor.execute(qry2)
            connection.commit()

    except psycopg2.DatabaseError:
        print("db error", flush=True)

    connection.close()
    return output