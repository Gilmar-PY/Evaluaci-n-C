#define SUST(a, b) a -b

int main(int argc, char** argv) {
  int x = 7;
  int y = 3;
  int z = SUST(x, y);
  return 0;
}