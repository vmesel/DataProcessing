from sqlite3 import connect
import codecs

connection = connect("dbs/database.db")

#f = open("processed/database.txt","w")

cursor = connection.cursor()

cursor.execute("SELECT TWEET FROM TWEET")

for tweet in cursor.fetchall():
	print(str(tweet[0]).decode('utf-8','ignore'))
	#f.write(tweet[0] + "\n")

#f.close()
#print("ACABOUUUU!! EBAAA")
connection.commit()
