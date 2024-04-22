#include <stdio.h>

void func(int a) {
  a = 9;
}

int main(int argc, char** argv) {
  int x = 6;
  printf("Antes de llamar a la funcion: %d\n", x);
  func(x);
  printf("Despues de llamar a la funcion: %d\n", x);
  return 0;
}