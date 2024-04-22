#include <stdio.h>

int* crea_un_entero(int valor_defecto) {
  int var = valor_defecto;
  return &var;
}

int main() {
  int* ptr = NULL;
  ptr = crea_un_entero(8);
  printf("%d\n", *ptr);
  return 0;
}
