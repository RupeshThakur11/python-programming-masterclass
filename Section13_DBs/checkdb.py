#!/usr/bin/env python3

"""
Query the DB
"""

import sqlite3

name = input("please enter a name: ")
sql = "SELECT * FROM contacts WHERE name = ?"

conn = sqlite3.connect("contacts.sqlite")

for row in conn.execute(sql, (name,)):
    print(row)

conn.close()
