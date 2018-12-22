#!/usr/bin/env sh
set -e

# --solver=examples/mnist/lenet_solver.prototxt : 指定了训练超参数文件
./build/tools/caffe train --solver=examples/mnist/lenet_solver.prototxt $@
