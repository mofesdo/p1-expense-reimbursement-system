import psycopg2
from controller.logger import *

from model.connection import getConnection


def create_reimbursements(username: str, description: str, price: float, status: int, urgent: int, date: str):
    connection = getConnection()
    cursor = connection.cursor()
    flag = False

    qry = "INSERT INTO reimbursements VALUES (default, %s, %s, %s, %s, %s, %s) RETURNING request_id ;"

    try:
        cursor.execute(qry, (username, description, price, status, urgent, date))
        inserted_record_id = cursor.fetchone()[0]
        flag = True
        connection.commit()
        log_regular(f"Created a new reimbursement request with id: {inserted_record_id}")
    except psycopg2.DatabaseError as error:
        log_error(str(error))
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()
        log_regular("Database connection closed")

    return flag


def getReimbursementRequests(username, orderStyle):
    connection = getConnection()
    cursor = connection.cursor()

    results = []

    qry = f"SELECT * FROM reimbursements WHERE username='{username}' ORDER BY date_initiated ASC;"
    qry2 = f"SELECT * FROM reimbursements WHERE username='{username}' ORDER BY date_initiated DESC;"

    if orderStyle == "asc":
        finalQry = qry
    else:
        finalQry = qry2

    try:
        cursor.execute(finalQry)
        results = list(cursor.fetchall())
        log_regular(f"all records for {username} retrieved")
    except psycopg2.DatabaseError as e:
        log_error(str(e))

    return results
