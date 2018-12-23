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

if os.path.exists(savePath):
    print("savePath is exist:", sys.argv[2])
else:
    os.makedirs(savePath)
    print("savePath is create:", sys.argv[2])

binfile=open(fileName,'rb')
buf=binfile.read()
index=0
magic,numImages,numRows,numColumns=struct.unpack_from('>IIII',buf,index)
print(magic,numImages,numRows,numColumns)

index+=struct.calcsize('>IIII')
for image in range(0,numImages):
    im=struct.unpack_from('>784B',buf,index)
    index+=struct.calcsize('>784B')
    im=np.array(im,dtype='uint8')
    im=im.reshape(28,28)
    im=PIL.Image.fromarray(im)
    im.save(savePath+'/train_%s.bmp'%image,'bmp')