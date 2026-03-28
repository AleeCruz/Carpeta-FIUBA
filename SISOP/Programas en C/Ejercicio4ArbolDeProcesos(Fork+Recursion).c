#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

/*
 * Crea una cadena de procesos de profundidad `n`.
 * Cada proceso imprime su nivel y su PID,
 * luego crea un hijo que hace lo mismo con n-1.
 */
void cadena(int nivel, int max)
{
    printf("Nivel %d — PID %d\n", nivel, getpid());

    if (nivel == max) {   /* caso base: ya llegamos al fondo */
        printf("Nivel %d — soy la hoja, no creo más hijos\n", nivel);
        return;
    }

    pid_t pid = fork();   /* crear hijo */

    if (pid == 0) {
        /* el hijo continúa la cadena */
        cadena(nivel + 1, max);
        return;
    }

    /* el padre espera al hijo antes de terminar */
    wait(NULL);
}

int main(void)
{
    cadena(1, 100);   /* cadena de 4 niveles */
    return 0;
}


