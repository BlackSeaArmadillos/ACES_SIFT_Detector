CXXFLAGS = --std=c++17
CFLAGS = -c
#OBJ_FILES = $(shell find src/ -name "*.o")
#find_keypoints.o
OBJ_FILES = match_features.o image.o sift.o
CPP_FILES = $(shell find src/ -name "*.cpp")
EXE_NAME = main
BUILD_FOLDER = build
IDIR = ./inc
IFLAGS = -I$(IDIR)


build/$(EXE_NAME): $(OBJ_FILES)
	$(CXX) $(CXXFLAGS) $^ -o $@
#rm -f *.o


%.o: src/%.cpp
	mkdir -p $(BUILD_FOLDER)
	$(CXX) $(CXXFLAGS) $(CFLAGS) $^ -o $@ $(IFLAGS)


.PHONY: clean
clean:
	rm -rf *.o main build

