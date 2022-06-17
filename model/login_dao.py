import psycopg2
from model.connection import getConnection
import time
import random
import hashlib


# Login Functions -----------------------
def authenticate(username, password):
    connection = getConnection()
    cursor = connection.cursor()
    output = None

    hashedPW = md5hash(password)
    qry = f"SELECT * FROM user_table WHERE username='{username}' AND password='{hashedPW}';"
    print(hashedPW, flush=True)

    try:
        cursor.execute(qry)
        results = list(cursor.fetchall())

        hashstring = str(hash(float(time.time())+random.random()))
        if len(results) == 1:
            output = hashstring
            qry2 = f"UPDATE user_table SET authtoken='{hashstring}' WHERE username='{username}';"
            cursor.execute(qry2)
            connection.commit()

    except psycopg2.DatabaseError:
        print("db error", flush=True)

    connection.close()
    return output


def md5hash(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
