#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    int fd[2];

    if (pipe(fd) < 0) {        /* crear el pipe */
        perror("pipe");
        return 1;
    }

    pid_t pid = fork();

    if (pid == 0) {
        /* HIJO: solo lee */
        close(fd[1]);       /* cierra escritura */

        int numero;
        read(fd[0], &numero, sizeof(int));
        printf("Hijo recibió: %d, el doble es: %d\n", numero, numero * 2);

        close(fd[0]);       /* cierra lectura */
        return 0;
    }else{
            /* PADRE: solo escribe */
        close(fd[0]);           /* cierra lectura */

        int numero = 21;
        write(fd[1], &numero, sizeof(int));
        printf("Padre envió: %d\n", numero);

        close(fd[1]);           /* cierra escritura */
        wait(NULL);

    }

  

    return 0;
}