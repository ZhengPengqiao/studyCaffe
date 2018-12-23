#!/usr/bin/python2.7
#-*- coding: UTF-8 -*-

import os
import sys
caffe_root = '/home/zpq/WorkSpace/DeepLearn/caffe'
sys.path.insert(0,caffe_root+'/python')
import caffe

if len(sys.argv) < 2:
    print("USED: ", sys.argv[0], "will_image_filename")
    os._exit(0)

MODEL_FILE = caffe_root + '/examples/mnist/lenet.prototxt'
PRETRAINED = caffe_root + '/examples/mnist/lenet_iter_10000.caffemodel'
IMAGE_FILE = os.getcwd() + "/" + sys.argv[1]

print("MODEL_FILE: "+MODEL_FILE)
print("PRETRAINED: "+PRETRAINED)
print("IMAGE_FILE: "+IMAGE_FILE)

input_image=caffe.io.load_image(IMAGE_FILE,color=False)

#print input_image
net =caffe.Classifier(MODEL_FILE, PRETRAINED)
prediction=net.predict([input_image],oversample=False)

caffe.set_mode_cpu()
print("predicted class: ", prediction[0].argmax())