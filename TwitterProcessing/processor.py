# Processador de Linguagem Natural baseado em Tweets!
"""
    About twitterprocessor
Version:    0.0.1 (April/2016)
Author:     Vinicius Mesel (vmesel)
Oficial:    Github.com/vmesel/DataProcessing/
License:    MIT
Support:    Python 3+
"""
from twitter import *
import settings
import urllib.request

t = Twitter(auth=OAuth(settings.token, settings.tokensecret, settings.consumerkey, settings.consumersecret))
s = t.search.tweets(q="#guerracivil")

#for tweet in s:
#    print(tweet['text'])

print(s[0])

#with open("twitter-return.txt","a") as f:
    #print(str(f.read()))
#    data = f.read()

#    print(json.load(data))
    #p = f.read()
    #print(p)
    #json.load(p)
    #file = f.read()
    #j = json.load(file)

#    f.close()




# Este é um recurso útil para podermos postar toda vez que nosso crawler parsear algo de interessante
#t.statuses.update(status="Olá Mundo, tweet via API do Twitter")
