#include <stdio.h>

int main(int argc, char** argv) {
  int var = 1;

  int* int_ptr = NULL; // Anulacion del puntero
  int_ptr = &var;

  char* char_ptr = NULL;
  char_ptr = (char*)&var;

  printf("Antes aritmetica: int_ptr: %u, char_ptr: %u\n",
          (unsigned int)int_ptr, (unsigned int)char_ptr);

  int_ptr++;    // Paso aritmetico es usualmente 4 bytes
  char_ptr++;   // Paso aritmetico en 1 byte

  printf("Despues de la aritmetica: int_ptr: %u, char_ptr: %u\n",
          (unsigned int)int_ptr, (unsigned int)char_ptr);

  return 0;
}