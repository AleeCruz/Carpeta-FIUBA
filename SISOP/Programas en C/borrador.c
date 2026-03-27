#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    pid_t pid = fork();   /* crear el proceso hijo */

    if (pid < 0) {
        perror("fork");
        return 1;
    }

    if (pid == 0) {
        /* este bloque lo ejecuta el HIJO */
        printf("Soy el hijo, mi PID es %d\n",getpid());
    } else {
        /* este bloque lo ejecuta el PADRE */
        printf("Soy el padre, mi PID es %d, y cree un hijo con PID %d\n",
               getpid(), pid);
        wait(NULL);   /* esperar a que el hijo termine */
    }

    return 0;
}