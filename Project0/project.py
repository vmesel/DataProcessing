#Primeiro programa para processamento dos textos adquiridos e passar de Windows 1252 para UTF-8
import os
import sys 
from mapreducelib import MapReduce

job = MapReduce("/usr/local/Cellar/hadoop/2.7.2/libexec/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar",\
"/usr/local/Cellar/hadoop/2.7.2/bin/hadoop")


#job.run_map("mapper.py","/TextosMachado/","/Transcoding/")
job.run_map_reduce("mpprog.py", "rdprog.py","/TextosMachado/","/Transcoding/")

