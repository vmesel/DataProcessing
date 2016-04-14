#!/usr/bin/env python3

from sys import stdin
import io

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='win1252')
texto = stdin.read()

print(texto)

#texto = str(texto).decode("win1252")
#textoencodado = []


#for linha in texto:
#	linha = linha.strip()
#	print(linha)
#	textoencodado = linha.append()
#	open("hello.txt", "w").write(textoencodado)
