import psycopg2
from controller.logger import *

from model.connection import getConnection


def create_reimbursements(username: str, description: str, price: float, status: int, urgent: int):
    connection = getConnection()
    cursor = connection.cursor()
    flag = False

    qry = "INSERT INTO reimbursements VALUES (default, %s, %s, %s, %s, %s) RETURNING request_id ;"

    try:
        cursor.execute(qry, (username, description, price, status, urgent))
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

