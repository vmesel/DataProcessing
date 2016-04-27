#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os
import sys

def readAndTranscode(fileToRead):
    k = open(fileToRead + "-output","w")
    for line in open(fileToRead,"r"):
        repre = eval(line).decode()
        repre = repre.replace("\n","")
        k.write(repre + "\n")

readAndTranscode("dbs/hallo2.txt")
