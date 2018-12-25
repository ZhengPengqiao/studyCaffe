#!/bin/bash

if [ "$#" != "1" ]
then
    echo "Used:"
    echo "  "$0 filename
    exit
fi

echo "test image file = "$1

./build/examples/cpp_classification/classification.bin \
    examples/Face/lenet.prototxt \
    examples/Face/lenet_iter_10000.caffemodel \
    data/Face/face_mean.binaryproto \
    data/Face/synset_words.txt \
    $1