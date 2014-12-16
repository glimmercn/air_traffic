#include <stdlib.h>
#include <iostream>
#include <vector>

#include <segments.h>

using namespace std;

int main(int argc, const char *argv[])
{
  int data = 2;

  /* random simple path */
  if (data == 1) {
    Arrangement_2 arr;
    vector<Segment_2> segs = random_arrangement(arr, 30);
    weighted_route(arr, one_major_dtb);
  //  Arrangement_2::Vertex_const_iterator vh = arr.vertices_begin();
  //  push_iter(vh, 10);  
  //
  //  std::vector<Vertex_const_handle> path = random_simple_path(arr, 10, vh);
  //
  //  output_path(path, "helloworld");
    output_arrangement(segs, "arr.data");
    
    append("100", "paths.data");
  
    int nPath = 100;
    
    for (int i = 0; i < nPath; i++) {
      int nVertex = arr.number_of_vertices();
      int nStep = rand() % nVertex;
      Arrangement_2::Vertex_const_iterator vh = arr.vertices_begin();
      push_iter(vh, nStep);  
      
      int nLen = rand() % 23 + 2; 
      Path path = random_simple_path(arr, nLen, vh);
      output_path(path, "paths.data");   
    }
  }
  /*random path(not simple) */
  if (data == 2) {
    Arrangement_2 arr;
    vector<Segment_2> segs = random_arrangement(arr, 30);
    weighted_route(arr, one_major_dtb);
    output_arrangement(segs, "arr.data");
    
    append("200", "paths.data");
  
    int nPath = 200;
    
    for (int i = 0; i < nPath; i++) {
      int nVertex = arr.number_of_vertices();
      int nStep = rand() % nVertex;
      Arrangement_2::Vertex_const_iterator vh = arr.vertices_begin();
      push_iter(vh, nStep);  
      
      int nLen = rand() % 11 + 2; 
      Path path = random_path(arr, nLen, vh);
      output_path(path, "paths.data");   
    }
  }


  return 0;

}



