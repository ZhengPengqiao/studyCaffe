#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os

#101数据集的文件夹名称
srcPath = "./data/Face/train_data"
outPath = "./data/Face"
#显示该路径下所有文件
path = os.listdir(srcPath) 
path.sort()
vp = 0.1 #测试集合取总数据前10%
ftr = open(outPath+'/'+'train_data.txt','w')
fva = open(outPath+'/'+'val_data.txt','w')
i = 0

for line in path:
    subdir = srcPath +'/'+line
    childpath = os.listdir(subdir)
    mid = int(vp*len(childpath))
    for child in childpath[:mid]:
        subpath = line+'/'+child;
        d = ' %s' % (i)
        t = subpath + d
        fva.write(t +'\n')
    for child in childpath[mid:]:
        subpath = line+'/'+child;
        d = ' %s' %(i)
        t = subpath + d
        ftr.write(t +'\n')
    i=i+1

#关闭文件流
ftr.close()
fva.close()
