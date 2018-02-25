#!/usr/bin/python

import mysql.connector
from mysql.connector import Error
import os

try:
    conn = mysql.connector.connect(host=os.environ['RDS_HOSTNAME'],
    database=os.environ['RDS_DB_NAME'],
    user=os.environ['RDS_USERNAME'],
    password=os.environ['RDS_PASSWORD'])

    if conn.is_connected():
        print("Suceess!!!")

except Error as e:
    print(e)
    print('Failure')


finally:
    print('lets get rolling')

