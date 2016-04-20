from re import compile
from collections import Counter
import nltk

regex = compile("\w+")

arq = open("database2.txt")

# ----------- OP1
    artigos = "A O AS OS".split()

    for x in arq:
        x = regex.findall(x)
        try:
            if x[0] in artigos:
                pessoa = x[1]
                resto = x[2:]
                print(x[0], pessoa, resto)
        except:
            pass

# ----------- OP2
lista = []
for x in arq:
    saida = regex.findall(x.lower())
    for y in saida:
        lista.append(y)

print(Counter(lista))

# ----------- OP3
texto = arq.read()

a = nltk.wordpunct_tokenize(texto)

a = nltk.Text(a)

a.concordance("impeachment")
#print(Counter(a))
