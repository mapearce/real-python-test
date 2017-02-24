import sqlite3

#create cars.db
conn = sqlite3.connect("cars.db")

#get the cursor
cursor = conn.cursor()

#Used this when I mislabeled the table "population"
#cursor.execute(""" DROP TABLE population""")

#create the table
cursor.execute(""" CREATE TABLE Inventory
				(Make TEXT, Model TEXT, Quantity INT)
				""")

#close db connection
conn.close()