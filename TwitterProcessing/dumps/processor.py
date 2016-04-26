# -*- coding: utf-8 -*-
# Escrito por: Vinicius Mesel, Renan Palmeira e Eduardo Mendes
# Processador para análise de sentimentos de frases
# Data: 26 de abril de 2016
# Baseado em: http://wp-a.co/u/q09c e na modificação do Renan em: http://wp-a.co/u/8uO-

import nltk

try:
    stoparq = open("stopwords.txt","r")
    stop_words = []
    for stopPalavra in stoparq:
        stopPalavra = stopPalavra.replace("\n","")
        stop_words.append(stopPalavra)
except Exception:
    stop_words = nltk.corpus.stopwords.words('portuguese')

class ProcessadorDeSentimentos():
    def __init__(self, amostras):
        self.feature_palavras = self.pegar_palavra_features(self.pegar_palavra_em_amostra(amostras))
        self.set_treinamento = nltk.classify.apply_features(self.extrair_features, amostras)
        self.classificador = nltk.NaiveBayesClassifier.train(self.set_treinamento)

    def mostra_features(self):
        self.classificador.show_most_informative_features(self.feature_palavras)

    def classifica(self, amostra):
        if type(amostra) is str:
            amostra = amostra.split()
        return self.classificador.classify(self.extrair_features(amostra))

    def pegar_palavra_em_amostra(self, amostra):
        todas_palavras = []
        for (palavras, sentimento) in amostra:
            todas_palavras.extend(palavras)
        return(todas_palavras)

    def pegar_palavra_features(self, listaPalavras):
        listaPalavras = nltk.FreqDist(listaPalavras)
        featuresPalavra = listaPalavras.keys()
        return(featuresPalavra)

    def extrair_features(self, documento):
        palavras_documento = set(documento)
        features = {}
        for palavra in self.feature_palavras:
            features['contains(%s)' % palavra] = (palavra in palavras_documento)
        return(features)


    @classmethod
    def tokenize(cls, frases):
        global stop_words
        amostras = []
        for (frase, sentimento) in frases:
            palavras_filtradas = []
            lista_palavras = nltk.wordpunct_tokenize(frase)
            for palavra in lista_palavras:
                if palavra not in stop_words:
                    palavras_filtradas.append(palavra)
            amostras.append((palavras_filtradas, sentimento))
        return(amostras)
