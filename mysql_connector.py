#!/usr/bin/python
# Simple MySQL connector with example select query (based on mysql-connector-python library) with error handling
# prerequisites # mysql-connector-python installation: shell> pip install mysql-connector-python
# source code based on Python 3

import mysql.connector
import datetime
import config
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user=config.DB_USERNAME,
                                password=config.DB_PASSWORD,
                                database=config.DB_NAME,
                                host=config.DB_HOST,
                                port=config.DB_PORT)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = cnx.cursor()
## DB select query example
  query = ("SELECT loc_no, loc_name, loc_type FROM Locations "
         "WHERE loc_type = 1")

  cursor.execute(query)

  for (loc_no, loc_name, loc_type) in cursor:
      print("ID: {}, Localization: {}, Type: {}".format(loc_no, loc_name, loc_type))

  cursor.close()
  cnx.close()

#print ('-----------------------------------------------------------------------')
#print ('USERNAME: ', config.DB_USERNAME, 'DBNAME: ', config.DB_NAME, 'DB HOST:', config.DB_HOST)
