#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/O101
DATA=data/O101
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/O101_train_lmdb \
  $DATA/O101_mean.binaryproto

echo "Done."
