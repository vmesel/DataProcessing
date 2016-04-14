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

t = Twitter(auth=OAuth(settings.token, settings.tokensecret, settings.consumerkey, settings.consumersecret))
s = t.search.tweets(q="#guerracivil")


statuses = s['statuses']


for status in statuses:
    if "RT" in status['text']:
        status.clear()
    else:
        if "pt" in status['lang']:

            print("########################################### Tweet ########################################### ")
            print("Tweet ID: " + str(status['id']))
            print("Hora: " + status['created_at'])
            print(status['user']['screen_name'])
            print(status['source'])
            hashtags = []
            for hashtag in status['entities']['hashtags']:
                hashtags.append(hashtag['text'])
            print(hashtags)
            print(status['retweet_count'])
            print(status['favorite_count'])
            palavras = []


            for palavra in status['text'].split(" "):
                if "#" in palavra:
                    pass
                else:
                    palavras.append(palavra)
            print(palavras)
        # Aqui que nós vamos implementar a parte de parseamento de palavras e definição de adjetivos


# Este é um recurso útil para podermos postar toda vez que nosso crawler parsear algo de interessante
#t.statuses.update(status="Olá Mundo, tweet via API do Twitter")
