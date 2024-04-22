#include <stdio.h>
#include <stdlib.h>

int* crea_un_entero(int valor_defecto) {
  int* var_ptr = (int*)malloc(sizeof(int));
  *var_ptr = valor_defecto;
  return var_ptr;
}

int main() {
  int* ptr = NULL;
  ptr = crea_un_entero(8);
  printf("%d\n", *ptr);
  free(ptr);
  return 0;
}
