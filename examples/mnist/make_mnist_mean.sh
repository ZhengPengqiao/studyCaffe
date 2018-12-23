#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/mnist
DATA=data/mnist
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/mnist_train_lmdb \
  $EXAMPLE/mnist_mean.binaryproto

echo "Done."
