"""
    About twitterprocessor
Description: Processador de Linguagem Natural baseado em Tweets!
Version:    0.0.2 (April/2016)
Last Mod:   14-04-16
Author:     Vinicius Mesel (vmesel)
Oficial:    Github.com/vmesel/DataProcessing/
License:    MIT
Support:    Python 3+
"""

from twitter import *
import settings
import json
import time

# Este é um recurso útil para podermos postar toda vez que nosso crawler parsear algo de interessante
#t.statuses.update(status="Iniciando apuração do Impeachment via API no Twitter com Processamento de Linguagem Natural! Próximo GruPy-SP Terá a apuração dos dados!")

print("Iniciando parseamento de Tweets!")

def Scrapping():
    t = Twitter(auth=OAuth(settings.token, settings.tokensecret, settings.consumerkey, settings.consumersecret))
    s = t.search.tweets(q="#impeachment",count=100)
    numeroInicial = 0

    statuses = s['statuses']
    tweet = []

    for status in statuses:
        if "RT" in status['text']:
            status.clear()
        else:
            if "pt" in status['lang']:
                listing = open("crawled-twitter.txt","r+")
                if str(status['id']) not in listing.read():

                    #print("########################################### Tweet ########################################### ")
                    listing.write("{}\n".format(str(status['id'])))
                    #print("Tweet ID: " + str(status['id']))
                    tweet.append(str(status['id']))
                    #print("Hora: " + status['created_at'])
                    tweet.append(status['created_at'])
                    #print(status['user']['screen_name'])
                    tweet.append(status['user']['screen_name'])
                    try:
                        #print(status['source'])
                        tweet.append(status['source'])
                    except:
                        #print("Source Failed")
                        tweet.append("Source Failed")
                    hashtags = []
                    for hashtag in status['entities']['hashtags']:
                        hashtags.append(hashtag['text'])
                    #print(hashtags)
                    tweet.append(hashtags)
                    #print(status['retweet_count'])
                    tweet.append(status['retweet_count'])
                    #print(status['favorite_count'])
                    tweet.append(status['favorite_count'])
                    palavras = []


                    for palavra in status['text'].split(" "):
                        if "#" in palavra:
                            pass
                        else:
                            palavras.append(palavra)
                    try:
                        #print(palavras)
                        tweet.append(palavras)
                    except:
                        #print("Parsing Failed")
                        tweet.append("Parsing Failed")

                    file = open("apuracao.txt", "r+")

                    # ID, Horario, Usuario, Fonte, Hashtags, Retweets, Favoritos, Palavras, Contagem,
                    #print(tweet)
                    try:
                        print(str(tweet) + ";\n\r\n\r\n\r")
                        file.write(str(tweet) + ";\n\r\n\r\n\r")
                        tweet[:]
                    except:
                        print(str(tweet) + ";\n\r\n\r\n\r")
                        file.write(str(tweet).decode('utf-8') + ";\n\r\n\r\n\r")
                        tweet[:]

                    file.close()
                    NumeroFinal = numeroInicial + 1
                    print(NumeroFinal)

                else:
                    pass

while True:
    try:
        Scrapping()
    except:
        print("Estamos aguardando o Twitter nos liberar daqui alguns minutos!")
        time.sleep(900)
        Scrapping()
