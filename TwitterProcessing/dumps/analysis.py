import subprocess
from os import system
postagens = open("dbs/saida1-sl.txt","r")


for post in postagens:
    primeiraString = "echo '{}'".format(post)
    stringCompleta = primeiraString + " | ~/Downloads/cmd/tree-tagger-portuguese"
    processo = subprocess.Popen(stringCompleta,stdout=subprocess.PIPE)
    for linha in process.stdout.read():
        if "A" in linha:
            print(linha)
    #print(post)
