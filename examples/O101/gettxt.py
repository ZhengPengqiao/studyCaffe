#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os

#101数据集的文件夹名称
data = "./data/O101"
#显示该路径下所有文件
path = os.listdir(data) 
path.sort()
vp = 0.1 #测试集合取总数据前10%
ftr = open(data+'/'+'train.txt','w')
fva = open(data+'/'+'val.txt','w')
i = 0

for line in path:
    subdir = data +'/'+line
    childpath = os.listdir(subdir)
    mid = int(vp*len(childpath))
    for child in childpath[:mid]:
        subpath = data+'/'+line+'/'+child;
        d = ' %s' % (i)
        t = subpath + d
        fva.write(t +'\n')
    for child in childpath[mid:]:
        subpath = data+'/'+line+'/'+child;
        d = ' %s' %(i)
        t = subpath + d
        ftr.write(t +'\n')
    i=i+1

#关闭文件流
ftr.close()
fva.close()
