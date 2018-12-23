#!/usr/bin/env sh
set -e

./build/tools/caffe train \
    --solver=examples/imagenet/solver.prototxt \
    --snapshot=models/bvlc_reference_caffenet/caffenet_train_10000.solverstate.h5 \
    $@
