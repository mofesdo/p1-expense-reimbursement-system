# this file is used to define a function to get the database connection
import psycopg2

def get_connection():
    connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="Blackbeard",
            host="p1-database.cvzbvdn4nh5s.us-west-1.rds.amazonaws.com",
            port="5432"
            )
    return connection


def getConnection():
    return psycopg2.connect(
            database="postgres",
            user="postgres",
            password="revature",
            host="database-project0.c3f2ribjt3t3.us-east-1.rds.amazonaws.com",
            port="5432"
    )