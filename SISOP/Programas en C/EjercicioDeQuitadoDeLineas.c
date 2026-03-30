#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *linea = NULL;
    size_t capacidad = 0;
    ssize_t len;

    while ((len = getline(&linea, &capacidad, stdin)) != -1) {
        /* Eliminar el \n del final */
        if (len > 0 && linea[len -1] == '\n')
            linea[len-1] = '\0';

        printf("Leí: '%s'\n", linea);
    }

    free(linea);   /* liberar memoria */
    return 0;
}