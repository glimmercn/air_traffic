#include <stdlib.h>
#include <iostream>
#include <vector>

#include <segments.h>

using namespace std;

int main(int argc, const char *argv[])
{
  int data = 2;

  /* random simple path */
  if (data == 1) 
    data_generater(
        "30_arr.data",
        30,
        "100_simple_paths.data",
        100,
        one_major_dtb,
        random_simple_path,
        7,
        4);
  /*random path(not simple) */
  if (data == 2)
    data_generater(
        "20_arr.data",
        20,
        "50_paths.data",
        50,
        uniform_dtb,
        random_path,
        9,
        4);

  return 0;

}



