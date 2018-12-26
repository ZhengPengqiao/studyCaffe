TARGET:=classification.bin
SRC = classification.o

LINKFLAGS=-pthread -fPIC -DCAFFE_VERSION=1.0.0 -DNDEBUG -O2 -DUSE_OPENCV -DUSE_LEVELDB \
	-DUSE_LMDB -DUSE_HDF5 -I/usr/include/python2.7 -I/usr/lib/python2.7/dist-packages/numpy/core/include \
	-I/usr/local/include -I/usr/include/hdf5/serial/ -I.build_release/src -I./src -I./include \
	-I/usr/local/cuda/include -Wall -Wno-sign-compare -I/home/zpq/WorkSpace/DeepLearn/caffe/include -I/home/zpq/WorkSpace/DeepLearn/caffe/.build_release/src/
CXXFLAGS=$(LINKFLAGS)
LIBRARY_NAME=caffe
LDFLAGS=-L/usr/lib -L/usr/local/lib -L/usr/lib -L/usr/local/cuda/lib64 -L/usr/local/cuda/lib \
 	-L.build_release/lib -lopencv_shape -lopencv_stitching -lopencv_superres -lopencv_videostab \
  	-lopencv_aruco -lopencv_bgsegm -lopencv_bioinspired -lopencv_ccalib -lopencv_datasets \
	-lopencv_dpm -lopencv_face -lopencv_freetype -lopencv_fuzzy -lopencv_hdf -lopencv_line_descriptor \
	-lopencv_optflow -lopencv_video -lopencv_plot -lopencv_reg -lopencv_saliency -lopencv_stereo \
	-lopencv_structured_light -lopencv_phase_unwrapping -lopencv_rgbd -lopencv_viz -lopencv_surface_matching \
	-lopencv_text -lopencv_ximgproc -lopencv_calib3d -lopencv_features2d -lopencv_flann -lopencv_xobjdetect \
	-lopencv_objdetect -lopencv_ml -lopencv_xphoto -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs \
	-lopencv_photo -lopencv_imgproc -lopencv_core -lcudart -lcublas -lcurand -lglog -lgflags -lprotobuf \
	-lboost_system -lboost_filesystem -lm -lleveldb -lsnappy -llmdb -lhdf5_serial_hl -lhdf5_serial \
	-lopencv_core -lopencv_highgui -lopencv_imgproc -lopencv_imgcodecs -lboost_thread -lstdc++ -lopenblas \
	-L/home/zpq/WorkSpace/DeepLearn/caffe/.build_release/lib/
ORIGIN=$ORIGIN
CXX=g++
Q=
$(TARGET):$(SRC)
	$(Q)$(CXX) $< -o $@ $(LINKFLAGS) -l$(LIBRARY_NAME) $(LDFLAGS) \
		-Wl,-rpath,$(ORIGIN)/../../lib

%.o: %.cpp
	$(Q)$(CXX) $< $(CXXFLAGS) -c -o $@

clean:
	rm ./*.o $(TARGET)