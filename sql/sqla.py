#Create SQLite3 DB and Table

#import the sqlite3 library
import sqlite3

#create new DB if it doesn't already exist
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE population
				(city TEXT, state TEXT, population INT)
				""")
#close the DB connection
conn.close()