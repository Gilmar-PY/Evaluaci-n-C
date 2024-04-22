#include <stdio.h>

typedef struct {
  int x;
  int y;
} punto_t;

typedef struct {
  punto_t centro;
  int radio;
} circulo_t;

int main(int argc, char** argv) {
  circulo_t c;

  circulo_t* p1 = &c;
  punto_t*  p2 = (punto_t*)&c;
  int*      p3 = (int*)&c;

  printf("p1: %p\n", (void*)p1);
  printf("p2: %p\n", (void*)p2);
  printf("p3: %p\n", (void*)p3);

  return 0;
}
