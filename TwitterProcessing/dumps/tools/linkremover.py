import os
import sys
import re

f = open("dbs/database1.txt","r+")
padrao = re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
k = open("dbs/database1-sl.txt","w")


for linha in f:
    Procura = re.search(padrao, linha)
    if Procura == "None":
        k.write(linha + "\n")
    else:
        k.write(re.sub(padrao, "", linha) + "\n")
