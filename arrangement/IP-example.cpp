#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <segmental_arr_network.h>

using namespace std;

int main(int argc, const char *argv[])
{
  generate_data(
     "15.arr",
     15,
     "100_ip_simple.paths",
     100,
     one_major_dtb,
     random_simple_path,
     7,
     4);
  return 0;
}


