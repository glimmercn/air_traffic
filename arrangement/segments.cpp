#include <stdlib.h>
#include <iostream>
#include <vector>

#include <segments.h>

using namespace std;

int main(int argc, const char *argv[])
{
  int data = 3;

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


  return 0;

}



