#include <stdio.h>

struct __attribute__((__packed__)) estructura_t {
  char primero;
  char segundo;
  char tercero;
  short cuarto;
} ;

void imprime_tamn(struct estructura_t* var) {
  // ...
}

void imprime_bytes(struct estructura_t* var) {
  // ...
}

int main(int argc, char** argv) {
  // ...
}
