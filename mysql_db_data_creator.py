#!/usr/bin/python
# Simple MySQL db data creator (based on mysql-connector-python library) with error handling
# prerequisites # mysql-connector-python installation: shell> pip install mysql-connector-python
# source code based on Python 3

from __future__ import print_function

import mysql.connector
#from mysql.connector.cursor import MySQLCursorPrepared
import datetime
import config
from mysql.connector import errorcode

TABLES = {}
TABLES['Locations'] = (
    "CREATE TABLE `Locations` ("
    "  `loc_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `loc_name` text NOT NULL,"
    "  `loc_type` int(11) NOT NULL,"
    "  PRIMARY KEY (`loc_no`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=utf8")

try:
  cnx = mysql.connector.connect(user=config.DB_USERNAME,
                                password=config.DB_PASSWORD,
                                database=config.DB_NAME,
                                host=config.DB_HOST)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    exit(1)
else:
  print("Connected successfully to database: {}".format(config.DB_NAME))
  cursor = cnx.cursor()
  def create_database(cursor):
      try:
          cursor.execute(
              "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(config.DB_NAME))
      except mysql.connector.Error as err:
          print("Failed creating database: {}".format(err))
          exit(1)

try:
    cursor.execute("USE {}".format(config.DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(config.DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(config.DB_NAME))
        cnx.database = config.DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()

## INSERT Example location data into DB
add_locations = ("INSERT INTO Locations (loc_no, loc_name, loc_type) "
                "VALUES (%s, %s, %s)")

data_locations = [('NULL', 'New York City', 1) ,
                    ('NULL', 'Warsaw', 1) ,
                    ('NULL', 'Poznan', 1) ,
                    ('NULL', 'Poland', 2) ]

cursor = cnx.cursor()
cursor.executemany(add_locations, data_locations)
## Commit data to the database
cnx.commit()
print (cursor.rowcount, "Records inserted successfully into table")
## Closing database connection.
if(cnx.is_connected()):
    cursor.close()
    cnx.close()
    print("-- MySQL connection is closed --")
