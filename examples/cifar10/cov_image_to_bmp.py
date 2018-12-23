#!/usr/bin/python3
#-*- coding: UTF-8 -*-

import struct
import os
import sys
import numpy as np
#import matplotlib.pyplot as plt
import PIL.Image


if len(sys.argv) == 3:
   print("ubyteFileName:", sys.argv[1])
   print("savePath:", sys.argv[2])
   print("")
else:
    print("USED: ", sys.argv[0], " ubyteFileName savePath")
    os._exit(0)

fileName=sys.argv[1]
savePath=sys.argv[2]
height = 32
width = 32

if os.path.exists(savePath):
    print("savePath is exist:", sys.argv[2])
else:
    os.makedirs(savePath)
    print("savePath is create:", sys.argv[2])
# <1 x label><3072 x pixel>

filestr=os.path.splitext(os.path.basename(fileName))[0]

print("filestr: ", filestr)

binfile=open(fileName,'rb')
buf=binfile.read()
index=0
filesize=len(buf)
array = []

while True:
    tag=struct.unpack_from('>1B',buf,index)
    print(str(tag), index, filesize)
    index+=struct.calcsize('>1B')
    arry=struct.unpack_from('>3072B',buf,index)
    index+=struct.calcsize('>3072B')
    image = PIL.Image.new("RGB",(width,height))
    for i in range(0,width):
        for j in range(0,height):
            image.putpixel((i,j),(int(arry[i*32+j]),int(arry[i*32+j+1024]),int(arry[i*32+j+2048])))
    image.save(savePath + '/' + filestr +'_%s.bmp'%index,'bmp')
    
    if index >= filesize:
        os._exit(0)