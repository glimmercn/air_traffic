#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <segmental_arr_network.h>

using namespace std;

int main(int argc, const char *argv[])
{
  int data = 4;

  /* random simple path */
  if (data == 1) 
    data_generater(
        "30.arr",
        30,
        "100_simple.paths",
        100,
        one_major_dtb,
        random_simple_path,
        7,
        4);
  /*random path(not simple) */
  if (data == 2)
    data_generater(
        "20.arr",
        20,
        "20_simple.paths",
        20,
        uniform_dtb,
        random_path,
        9,
        4);
  
  if (data == 3)
    data_generater(
        "20.arr",
        20,
        "50_simple_uniform.paths",
        50,
        uniform_dtb,
        random_simple_path,
        9,
        4);
  if (data == 4) {
    Arrangement_2 arr;
    char arrFilename[] = "example4.arr";
    int arrSize = 8;
    char pathFileName[] = "one_major_dtb_path.dat";
    unsigned int nPath = 20;
    Dtb_generator dtb_generator = one_major_dtb;
    unsigned int pLenBase = 2;
    unsigned int pLenMode = 5;
    Path_generator path_generator = random_simple_path;

	  vector<Segment_2> segs = random_arrangement(arr, arrSize);
	  weighted_route(arr, dtb_generator);
	  
	  save_arrangement(segs, arrFilename);

	  vector<Path> paths;

	  for (int i = 0; i < nPath; i++) {
	    int nVertex = arr.number_of_vertices();
	    int nStep = rand() % nVertex;
	    Arrangement_2::Vertex_const_iterator vh = arr.vertices_begin();
	    push_iter(vh, nStep);

	    int nLen = rand() % pLenMode + pLenBase;
	    Path path = path_generator(arr, nLen, vh);
	    paths.push_back(path);
	  }

	  save_paths(paths, pathFileName);
    //create and save another group of paths
    paths.clear();
    dtb_generator = uniform_dtb;
    char pathFileName2[] = "uniform_dtb_path.dat";

    for (int i = 0; i < nPath; i++) {
	    int nVertex = arr.number_of_vertices();
	    int nStep = rand() % nVertex;
	    Arrangement_2::Vertex_const_iterator vh = arr.vertices_begin();
	    push_iter(vh, nStep);

	    int nLen = rand() % pLenMode + pLenBase;
	    Path path = path_generator(arr, nLen, vh);
	    paths.push_back(path);
	  }

	  save_paths(paths, pathFileName2);
 }

  return 0;

}


