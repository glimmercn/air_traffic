#include <stdlib.h>
#include <string>
#include <fstream>
#include <my_random.h>

#include <CGAL/Simple_cartesian.h>
#include <CGAL/Arr_segment_traits_2.h>
#include <CGAL/Arrangement_2.h>
#include <CGAL/Arr_extended_dcel.h>
#include <CGAL/MP_Float.h>
#include <CGAL/Quotient.h>
#include <vector>

typedef float 		                                    Number_type;
typedef CGAL::Simple_cartesian<Number_type>           Kernel;
typedef CGAL::Arr_segment_traits_2<Kernel>            Traits_2;
typedef CGAL::Arr_extended_dcel<Traits_2, std::vector<int>, int, int> DCEL;
typedef Traits_2::Point_2                             Point_2;
typedef Traits_2::X_monotone_curve_2                  Segment_2;
typedef CGAL::Arrangement_2<Traits_2, DCEL>           Arrangement_2;
typedef Arrangement_2::Vertex_handle                  Vertex_handle;
typedef Arrangement_2::Vertex_const_handle            Vertex_const_handle;
typedef Arrangement_2::Vertex_iterator                Vertex_iterator;
typedef Arrangement_2::Halfedge_handle                Halfedge_handle;
typedef std::vector<Vertex_const_handle>              Path;


using namespace std;

/* function pointer types */
typedef Distribution (*Dtb_generator)(Vertex_const_handle);  
typedef Path (*Path_generator) (const Arrangement_2&, int, Vertex_const_handle) ;

void append(string s, char const *filename)
{
  ofstream file;
  file.open(filename, ios::app);
  file << s << endl;
  file.close();
}

void save_a_path(const Path& path, char const *filename)
{
  ofstream file(filename, ofstream::app);
  file << path.size() << endl;

  for (int i = 0; i < path.size(); i++) {
    file << path[i]->point() << endl;
  }

  file.close();
}

void save_paths(const vector<Path>& paths, char const *filename)
{
  ofstream file(filename, ofstream::out);
  file << paths.size() << endl;

  for (int i = 0; i < paths.size(); i++) {
    save_a_path(paths[i], filename);
  }

  file.close();
}

void save_arrangement(vector<Segment_2>& segments, char const *filename)
{
  ofstream file;
  file.open(filename);
  file << segments.size() << endl;

  for (int i = 0; i < segments.size(); i++) {
    file << segments[i].source() << ' ';
    file << segments[i].target() << endl;
  }

  file.close();
}

Vertex_const_handle random_neighbour(Vertex_const_handle vh)
{
  Arrangement_2::Halfedge_around_vertex_const_circulator curr = vh->incident_halfedges();
  int ran_step = random_pick(vh->data());

  for (int i = 0; i < ran_step; i++) {
    curr++;
  }
  
  return curr->source();
   
}

vector<Segment_2> random_arrangement(Arrangement_2& arr, int n)
{
  //random generator
  int MIN = 0;
  int MAX = 800;

  //generate a list of segments
  vector<Segment_2> segments;
  for (int i=0; i < n; i++) {
    double x1 = rand() % MAX;
    double y1 = rand() % MAX;
    double x2 = rand() % MAX;
    double y2 = rand() % MAX;
    Segment_2 s(Point_2(x1, y1), Point_2(x2, y2));
    segments.push_back(s);
  }
	
  //insert the segment list into arr
  CGAL::insert(arr, segments.begin(), segments.end());
  return segments;	
}

// for each vertex, assign a route distribution to it
void weighted_route(Arrangement_2& arr, Dtb_generator dtbg)
{
  Vertex_iterator vit ;

  for (vit = arr.vertices_begin(); vit != arr.vertices_end(); vit++) {
    vit->set_data(dtbg(vit));
  }

}

Distribution one_major_dtb(Vertex_const_handle vh)
{
  int deg = vh->degree();
  assert(deg > 0);
  Distribution dtb(deg, 1);  
  int major = rand() % deg;
  dtb[major] += deg - 1;
  return dtb;
}

Distribution uniform_dtb(Vertex_const_handle vh)
{
  int deg = vh->degree();
  Distribution dtb(deg, 1);
  return dtb;
}

//from vh, generate a random path according to Distributions on the vertices of the arrangement.
Path random_path(const Arrangement_2& arr, int length, Vertex_const_handle vh)
{
  Path path; 
  path.push_back(vh);
  
  for (int i = 0; i < length; i++) {
    vh = random_neighbour(vh);
    path.push_back(vh);
  }

  return path;
}

//return a simple(non-repeating) path from arrangement
Path random_simple_path(const Arrangement_2& arr, int length, Vertex_const_handle vh)
{
  Arrangement_2::Halfedge_around_vertex_const_circulator curr;
  Path path; 
  Vertex_const_handle last = vh;
  Vertex_const_handle nei;
  path.push_back(vh);

  for (int i = 0; i < length; i++) {
    int TIMES = 10;

    while (TIMES != 0) {
      nei = random_neighbour(vh);
      if (nei != last) {
        last = vh;
        vh = nei;
        path.push_back(vh);
        break;
      }
      TIMES--;
    }
  }

  return path;
}


void push_iter(Vertex_const_handle& vh, int step) 
{
  for (int i = 0; i < step; i++) {
    vh++;
  }
}

void generate_data(
    char const *arrFilename,   //the file saves the arrangement.
    unsigned int arrSize,      //the number of segments in the arrangement.
    char const *pathFileName,  //the file saves the random path.
    unsigned int nPath,        //the number of paths will be generated.
    Dtb_generator dtb_generator,
    Path_generator path_generator,
    unsigned int pLenMod,    //the length (the number of vertices) of a path is a random number in [0, 1, ..., pLenMod-1] plus pLenBase.
    unsigned int pLenBase
    )
{
  Arrangement_2 arr;
  vector<Segment_2> segs = random_arrangement(arr, arrSize);
  weighted_route(arr, dtb_generator);
  
  save_arrangement(segs, arrFilename);

  vector<Path> paths;

  for (int i = 0; i < nPath; i++) {
    int nVertex = arr.number_of_vertices();
    int nStep = rand() % nVertex;
    Arrangement_2::Vertex_const_iterator vh = arr.vertices_begin();
    push_iter(vh, nStep);

    int nLen = rand() % pLenMod + pLenBase;
    Path path = path_generator(arr, nLen, vh);
    paths.push_back(path);
  }

  save_paths(paths, pathFileName);
    
}


