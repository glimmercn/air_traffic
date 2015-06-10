#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <segmental_arr_network.h>

using namespace std;

int main(int argc, const char *argv[])
{
  generate_data(
     "20.arr",
     20,
     "100000_ip_simple.paths",
     100000,
     one_major_dtb,
     random_simple_path,
     9,
     5);
  return 0;
}


