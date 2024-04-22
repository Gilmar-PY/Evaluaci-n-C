#include <stdio.h>

typedef int bool_t;
typedef bool_t (*menor_que_func_t)(int, int);

bool_t menor_que(int a, int b) {
  return a < b ? 1 : 0;
}

bool_t menor_que_modular(int a, int b) {
  return (a % 5) < (b % 5) ? 1 : 0;
}

int main(int argc, char** argv) {
  menor_que_func_t func_ptr = NULL;
  
  func_ptr = &menor_que;
  bool_t resultado = func_ptr(3, 7);
  printf("%d\n", resultado);
  
  func_ptr = &menor_que_modular;
  resultado = func_ptr(3, 7);
  printf("%d\n", resultado);
  
  return 0;
}