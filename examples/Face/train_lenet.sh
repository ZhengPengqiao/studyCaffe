#!/usr/bin/env sh
set -e

# --solver=examples/Face/lenet_solver.prototxt : 指定了训练超参数文件
./build/tools/caffe train --solver=examples/Face/lenet_solver.prototxt $@
