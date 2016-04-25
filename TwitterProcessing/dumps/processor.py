import nltk
#from sklearn.naive_bayes import GaussianNB

stoparq = open("stopwords.txt","r")

stop_words = []

for stopPalavra in stoparq:
    stopPalavra = stopPalavra.replace("\n","")
    stop_words.append(stopPalavra)

fraseex = "Olá, você é muito linda, quase impossível"

palavras = nltk.wordpunct_tokenize(fraseex)

fraseLimpa = []

print(str(palavras))

for palavra in palavras:
    if palavra not in stop_words:
        fraseLimpa.append(palavra)



#Amostras de Tweets Positivos e Negativos
pos_tweets = [('Eu te acho maravilhosa','positiva'), ('Ela é linda demais','positiva'), ('Ele é impossível! Não pode existir alguém igual', 'positiva')]
neg_tweets = [('Esta garota é feia','negativa'), ('O mundo é cheio de desgraça','negativa'), ('Isto está impossível de ser encontrado','negativa')]

#Amostras de Palavras
amostras = []
amostrasPalavras = []

#Define as amostras com seus sentimentos
for (frase, sentimento) in pos_tweets + neg_tweets:
    listaDePalavras = nltk.wordpunct_tokenize(frase)
    for palavra in listaDePalavras:
        if palavra not in stop_words:
            amostrasPalavras.append(palavra)
    amostras.append((amostrasPalavras, sentimento))

print(str(amostras))


#print("Frase Suja: " + str(palavras))
#print("Frase limpa: " + str(fraseLimpa))


def pegar_palavra_em_amostra(amostra):
    todas_palavras = []
    for (palavras, sentimento) in amostra:
        todas_palavras.extend(palavras)
    return(todas_palavras)

def pegar_palavra_features(listaPalavras):
    listaPalavras = nltk.FreqDist(listaPalavras)
    featuresPalavra = listaPalavras.keys()
    return(featuresPalavra)


def extrair_features(documento, featuresPalavras):
    palavras_documento = set(documento)
    features = {}
    for palavra in featuresPalavras:
        features['contains(%s)' % palavra] = (palavra in palavras_documento)
    return(features)


#print(pegar_palavra_em_amostra(amostras))
word_features = pegar_palavra_features(pegar_palavra_em_amostra(amostras))

print(extrair_features(['Ela','linda'], word_features))

# Baseado em: http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/#highlighter_890313

set_treinamento = nltk.classify.apply_features(extrair_features, amostras)
classificador = nltk.NaiveBayesClassifier.train(set_treinamento)

# Se Positivo > Negativo = Palavra Positiva
# Se Negativo > Positivo = Palavra Negativa
