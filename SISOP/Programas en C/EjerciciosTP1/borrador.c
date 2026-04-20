#include <stdio.h>

extern char **environ;

int main() {
    int n = 0;
    while (environ[n] != NULL) {
        n++;
    }
    printf("Cantidad de variables: %d\n", n);
    return 0;
}
