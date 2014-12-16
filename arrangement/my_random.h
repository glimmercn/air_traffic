#include <vector>
#include <stdlib.h>
typedef std::vector<int>                Distribution;

int random_pick(const Distribution& dtb) {
  int up = 0;
  int sum = 0;
  for (int i = 0; i < dtb.size(); i++) {
    sum += dtb[i];
  }

  float p = rand() / RAND_MAX * sum;

  for (int i = 0; i < dtb.size(); i++) {
    up += dtb[i];
    if (p < up)
      return i;
  }

  return dtb.size() - 1; 

}
