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
import sys
import sqlite3 as sql
import re



print("Iniciando parseamento de Tweets!")


class Scrapper:
    def Scrapping(search,ofile):
        try:


            # Linux only
            #if path.exists("processed/") == False:
            #    system("mkdir processed/")

            #if path.exists("processed/" + ofile + ".txt") == False:
                #systemstring = "touch processed/" + ofile + ".txt"
                #system(systemstring)


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
                        #systemstringcrawled = "touch " + TweetsListed
                        #system(systemstringcrawled)
                        listing = open(TweetsListed,"r+")
                        if str(status['id']) not in listing.read():

                            palavras = []

                            #for palavra in status['text'].split(" "):
                            #    if "#" in palavra:
                            #        pass
                            #    else:
                            #        palavras = palavras + (palavra)

                            #palavras = palavras.split("'")
                            statusone = status['text'].split('"')
                            statustwo = re.sub('[\"\']', '', status['text'])

                            try:
                                connection = sql.connect("database.db")
                                cursor = connection.cursor()
                                stringTweet = 'INSERT INTO "TWEET"("IDTWEET", "DATA", "USUARIO", "HASHTAGS", "RETWEETS", "FAVORITOS", "TWEET") VALUES("{}","{}","{}","{}","{}","{}","{}");'.format(str(status['id']),str(status['created_at']), str(status['user']['screen_name']), str(status['entities']),str(status['retweet_count']),str(status['favorite_count']),str(statustwo))
                                print(stringTweet)
                                cursor.execute(str(stringTweet))
                                connection.commit()
                            except ValueError:
                                pass

                            listing.write(str(status['id'])+ "\n")


                        else:
                            pass

        except ValueError:
            print("Exception: " + str(ValueError))
            print("O programa voltará a rodar em alguns instantes")
