
import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='challenge',
                                       user='',
                                       password='')
        return conn
    except Error as e:
        print(e)



def fetch_challenge_from_database(conn):
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM challenges ORDER BY RAND() LIMIT 1;")
        # get all records
        records = cursor.fetchall()

        for row in records:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            return row[1]

if __name__ == '__main__':
    connect()

