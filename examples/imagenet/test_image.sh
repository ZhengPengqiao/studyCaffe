#!/bin/bash

if [ "$#" != "1" ]
then
    echo "Used:"
    echo "  "$0 filename
    exit
fi

echo "test image file = "$1

./build/examples/cpp_classification/classification.bin \
  models/bvlc_reference_caffenet/deploy.prototxt \
  models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel \
  data/ilsvrc12/imagenet_mean.binaryproto \
  data/ilsvrc12/synset_words.txt \
  $1