"""
    About twitterprocessor
Description: Processador de Linguagem Natural baseado em Tweets!
Version:    0.1.0 (April/2016)
Last Mod:   15-04-16
Author:     Vinicius Mesel (vmesel)
Oficial:    Github.com/vmesel/DataProcessing/
License:    MIT
Support:    Python 3+
"""

from twitter import *
import settings
import json
import time
from os import system,path

print("Iniciando parseamento de Tweets!")


class Scrapper:
    def Scrapping(search,ofile):
        try:

            if path.exists("processed/") == False:
                system("mkdir processed/")
            systemstring = "touch processed/" + ofile + ".txt"
            system(systemstring)

            t = Twitter(auth=OAuth(settings.token, settings.tokensecret, settings.consumerkey, settings.consumersecret))
            s = t.search.tweets(q=str(search),count=150)
            numeroInicial = 0

            statuses = s['statuses']
            tweet = []

            for status in statuses:
                if "RT" in status['text']:
                    status.clear()
                else:
                    if "pt" in status['lang']:
                        TweetsListed = "processed/" + ofile + "-crawled.txt"
                        systemstringcrawled = "touch " + TweetsListed
                        system(systemstringcrawled)
                        listing = open(TweetsListed,"r+")
                        if str(status['id']) not in listing.read():

                            listing.write("{}\n".format(str(status['id'])))
                            tweet.append(str(status['id']))
                            tweet.append(status['created_at'])
                            tweet.append(status['user']['screen_name'])
                            try:
                                tweet.append(status['source'])
                            except:
                                tweet.append("Source Failed")
                            hashtags = []
                            for hashtag in status['entities']['hashtags']:
                                hashtags.append(hashtag['text'])
                            tweet.append(hashtags)
                            tweet.append(status['retweet_count'])
                            tweet.append(status['favorite_count'])
                            palavras = []


                            for palavra in status['text'].split(" "):
                                if "#" in palavra:
                                    pass
                                else:
                                    palavras.append(palavra)
                            try:
                                tweet.append(palavras)
                            except:
                                tweet.append("Parsing Failed")

                            file = open("processed/"+ ofile + ".txt", "r+")

                            try:
                                file.write(str(tweet) + ";\n\r\n\r\n\r")
                            except:
                                 file.write(str(tweet).decode('win1252') + ";\n\r\n\r\n\r")

                            tweet = []


                            file.close()
                        
                        else:
                            pass

        except Exception:
            print("Exception: " + str(Exception))
            print("O programa voltará a rodar em alguns instantes")
