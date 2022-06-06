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

