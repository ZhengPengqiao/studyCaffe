#!/usr/bin/python3
# -*- coding:utf-8 -*-

from PIL import Image
import os, glob
import sys
 
def batch_image(in_dir, out_dir):
    if not os.path.exists(out_dir):
        print(out_dir, 'is not existed.')
        os.makedirs(out_dir)

    
    if not os.path.exists(in_dir):
        print(in_dir, 'is not existed.')
        os._exit(-1)

    count = 0
    for files in glob.glob(in_dir+'/*'):
        filepath, filename = os.path.split(files)
        
        if os.path.isdir(filepath+"/"+filename):
            print(filepath+'/'+filename)
            batch_image(filepath+"/"+filename, out_dir+filename+"/")
            continue

        if  filename == "README":
            continue

        out_file = os.path.splitext(filename)[0] + '.png'
        print(filepath+'/'+filename, '-->', out_dir+out_file)

        im = Image.open(files)
        new_path = os.path.join(out_dir, out_file)
        print(count, ',', new_path)
        count = count + 1
        im.save(os.path.join(out_dir, out_file))

if __name__=='__main__':
    if len(sys.argv) < 3:
        print("USED: ",sys.argv[0], "srcPath dstPath");
        os._exit(0)

    srcPath = sys.argv[1]
    dstPath = sys.argv[2]
    print("srcPath: ", srcPath)
    print("dstPath: ", dstPath)

    batch_image(srcPath, dstPath)