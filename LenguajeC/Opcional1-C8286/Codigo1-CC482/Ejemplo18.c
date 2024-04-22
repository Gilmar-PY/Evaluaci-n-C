#include <stdio.h>

void func(int* a) {
  int b = 4;
  *a = 6;
  a = &b;
}

int main(int argc, char** argv) {
  int x = 13;
  int* xptr = &x;
  printf("Valor antes de llamar: %d\n", x);
  printf("Puntero antes de la llamada a la función: %p\n", (void*)xptr);
  func(xptr);
  printf("Valor despues de llamar: %d\n", x);
  printf("Puntero despues de la llamada a la funcion: %p\n", (void*)xptr);
  return 0;
}