#Primeiro programa para processamento de dados
import os
import sys 
from mapreducelib import Hdfs


hdfs = Hdfs("/usr/local/Cellar/hadoop/2.7.2/bin/hadoop fs")
hdfs.ls("/TextosMachado/")
