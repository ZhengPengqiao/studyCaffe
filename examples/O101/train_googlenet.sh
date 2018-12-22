#!/usr/bin/env sh
set -e

# --solver=examples/O101/googlenet_solver.prototxt : 指定了训练超参数文件
./build/tools/caffe train --solver=examples/O101/googlenet_solver.prototxt $@
