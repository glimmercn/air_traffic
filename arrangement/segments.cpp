#include <stdlib.h>
#include <iostream>
#include <vector>

#include <segments.h>

using namespace std;

int main(int argc, const char *argv[])
{
  Arrangement_2 arr;
  vector<Segment_2> segs = random_arrangement(arr, 30);
  //std::cout <<arr.number_of_edges()  << std::endl;

  Arrangement_2::Vertex_const_iterator vh = arr.vertices_begin();
  push_iter(vh, 10);  

  std::vector<Vertex_const_handle> path = random_simple_path(arr, 10, vh);

  output_path(path, "helloworld");
  output_arrangement(segs, "hellohuman");
  
  append("50", "paths.txt");

  int nPath = 50;
  
  for (int i = 0; i < nPath; i++) {
    int nVertex = arr.number_of_vertices();

    int nStep = rand() % nVertex;
    Arrangement_2::Vertex_const_iterator vh = arr.vertices_begin();
    push_iter(vh, nStep);  
    
    int nLen = rand() % 7 + 2; 
    Path path = random_simple_path(arr, nLen, vh);
    output_path(path, "paths.txt");   
  }

  return 0;

}



