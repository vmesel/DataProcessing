from re import compile
from collections import Counter
import nltk

regex = compile("\w+")

arq = open("dbs/database.txt")

# ----------- OP1
"""
artigos = "A O AS OS".split()

for x in arq:
    x = regex.findall(x)
    try:
        if x[0] in artigos:
            pessoa = x[1]
            resto = x[2:]
            print(x[0], pessoa, resto,"\n")
    except:
        pass
"""
# ----------- OP2
# Achar jeito de calcular quais palavras estão com maior frequência e que servem de adjetivos
"""
lista = []
for x in arq:
    saida = regex.findall(x.lower())
    for y in saida:
        lista.append(y)

conta = Counter(lista)
maisquemil = []
for item in conta:
    if conta[item] < 10:
        pass
    else:
        maisquemil.append("[{},{}]".format(item,conta[item]))

f = open("palavras-imp.txt","w")
f.write(str(maisquemil))
f.close()
"""
# ----------- OP3
texto = arq.read()

a = nltk.wordpunct_tokenize(texto)

a = nltk.Text(a)

a.concordance("economistas")

#print(Counter(a))
