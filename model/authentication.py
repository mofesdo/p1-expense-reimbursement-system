from model.connection import getConnection
import psycopg2
from controller.logger import *


def checkToken(token):
    connection = getConnection()
    cursor = connection.cursor()
    flag = False

    qry = f"SELECT * FROM user_table WHERE authtoken='{token}';"

    try:
        cursor.execute(qry)
        if len(list(cursor.fetchall())) == 1:
            flag = True
    except psycopg2.DatabaseError as e:
        log_error(str(e))

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
    except psycopg2.DatabaseError as e:
        log_error(str(e))

    connection.close()

    return output


def isManager(token):
    connection = getConnection()
    cursor = connection.cursor()
    flag = False

    qry = f"SELECT is_manager FROM user_table WHERE authtoken='{token}';"

    try:
        cursor.execute(qry)
        result = list(cursor.fetchall())

        if result[0][0] == 1:
            flag = True

        log_regular(f"user with token {token} has manager status {flag}")
    except psycopg2.DatabaseError as e:
        log_error(str(e))

    connection.close()

    return flag


