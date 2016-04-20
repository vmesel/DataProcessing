from sqlite3 import connect
import codecs

connection = connect("database.db")

#f = open("database-zero.txt","w")

cursor = connection.cursor()

cursor.execute("SELECT TWEET FROM TWEET")
connection.commit()

for tweet in cursor.fetchall():
	print(tweet[0].encode())

print("ACABOUUUU!! EBAAA")
