# Criado por: vmesel
# Serve para processar o database não-falho e extrair as informações de texto para PLN
# -*- coding: utf-8 -*-

from sqlite3 import connect
import unicodedata
import codecs

connection = connect("dbs/database2.db")

f = open("dbs/database2.txt","w")

cursor = connection.cursor()

cursor.execute("SELECT TWEET FROM TWEET")

for tweet in cursor.fetchall():
	f.write(tweet[0] + "\n")

f.close()
connection.commit()
