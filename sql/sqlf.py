#import sqlite3 library

import sqlite3

#create connection object
conn = sqlite3.connect("new.db")

#get the cursor
cursor = conn.cursor()

try:
	#insert data
	cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
	cursor.execute("INSERT INTO populations VALUES('San Fran', 'CA', 800000)")

	#commit the changes
	conn.commit

except sqlite3.OperationalError:
	print "Oy vey! Something went wrong...try again!"

#close the connecction
conn.close()