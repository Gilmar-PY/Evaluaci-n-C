#include <stdio.h>

struct estructura_t {
  char primero;
  char segundo;
  char tercero;
  short cuarto;
};

void imprime_tamn(struct estructura_t* var) {
  printf("Tam: %lu bytes\n", sizeof(*var));
}

void imprime_bytes(struct estructura_t* var) {
  unsigned char* ptr = (unsigned char*)var;
  for (int i = 0; i < sizeof(*var); i++, ptr++) {
    printf("%d ", (unsigned int)*ptr);
  }
  printf("\n");
}

int main(int argc, char** argv) {
  struct estructura_t var;
  var.primero = 'A';
  var.segundo = 'B';
  var.tercero = 'C';
  var.cuarto = 765;
  imprime_tamn(&var);
  imprime_bytes(&var);
  return 0;
}
