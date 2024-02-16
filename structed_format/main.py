import csv
import random
import time

import mysql.connector
import psycopg2

import config

# import pandas as pd

def main():
    crime_file = open(config.FILE_NAME, mode='r')
    data = csv.reader(crime_file)

    connection = get_rds_connection()
    create_table(connection)
    cursor = connection.cursor()
    next(data, None)

    for index_row, row in enumerate(data):
        # cursor.execute(config.insert_rows_format, row)
        # connection.commit()
        print(row)
        time.sleep(get_seconds_wait())

    crime_file.close()

    show_table(connection)
    connection.close()


def get_seconds_wait() -> int:
    seconds_wait = random.randint(config.min_seconds, config.max_seconds)
    return seconds_wait


def get_rds_connection():
    return mysql.connector.connect(
        host="crimessql.c3csg4yoy1nr.us-east-1.rds.amazonaws.com",
        user="admin",
        password="J9f5*rEs!",
        database="crimes_mysql")


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(config.CREATE_TABLE_FORMAT)
    connection.commit()
    print(f"Table {config.TABLE_NAME} created")


def show_table(connection):
    cursor = connection.cursor()
    cursor.execute(f"select * from {config.TABLE_NAME}")
    for row in cursor:
        print(row)


def delete_values(connection):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM{config.TABLE_NAME}")
    connection.commit()
    print(f"Table {config.TABLE_NAME} deleted")


if __name__ == '__main__':
    main()
