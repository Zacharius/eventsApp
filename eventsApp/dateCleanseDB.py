#!/usr/bin/python3

import datetime
import sqlite3

today = datetime.datetime.today().strftime('%Y-%m-%d')
today += ' 00:00:00'

try:
    conn = sqlite3.connect('db.sqlite3')

    c = conn.cursor()
    c.execute('''delete from cal_event where date<'2018-06-18 00:00:00' ''')

    conn.commit()
    conn.close()

except Sqlite3.Error as e:
    print("SQLite3 error :: %s", e)
    conn.close()
