#include <stdio.h>

int suma(int a, int b) {
  return a + b;
}

int resta(int a, int b) {
  return a - b;
}

int main() {
  int (*func_ptr)(int, int);
  func_ptr = NULL;

  func_ptr = &suma;
  int resultado = func_ptr(5, 4);
  printf("Suma: %d\n", resultado);

  func_ptr = &resta;
  resultado = func_ptr(5, 4);
  printf("Resta: %d\n", resultado);

  return 0;
}