#Learning the INSERT command

#always import the library
import sqlite3

#create the connection obect
conn = sqlite3.connect("new.db")

#get the cursor
cursor = conn.cursor()

#insert data!

cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

#commit the changes
conn.commit()

#close the connection
conn.close()