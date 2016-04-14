#!/usr/bin/env python3
#Primeiro programa para processamento dos textos adquiridos e passar de Windows 1252 para UTF-8
from os import system
import sys 
from mapreducelib import MapReduce, Hdfs

#hadoop = Hdfs("/usr/local/Cellar/hadoop/2.7.2/bin/hadoop fs")

system("hadoop dfs -rm -r /Transcoding/")

#hadoop.rm_dir("/Transcoding/")

# Importo as bibliotecas do MapReduce
#job = MapReduce("/usr/local/Cellar/hadoop/2.7.2/libexec/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar","/usr/local/Cellar/hadoop/2.7.2/bin/hadoop")


system("hadoop jar /usr/local/Cellar/hadoop/2.7.2/libexec/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper ~/GitHub/DataProcessing/Project0/mapper.py -input /TextosMachado/contos/ -output /Transcoding/")

#job.run_map("~/GitHub/DataProcessing/Project0/mapper.py",\
#"/TextosMachado/contos/"\
#,"/Transcoding/")

