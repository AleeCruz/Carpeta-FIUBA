#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {


    int fds[2];


    pipe(fds); // Creamos el pipe: fds[0] es lectura, fds[1] es escritura


    int pid = fork();

    
    if (pid < 0) {
        perror("Error en fork");
        exit(1);
    }

    if (pid == 0) {


        // --- PROCESO HIJO (RECEPTOR) ---
        close(fds[1]); // El hijo NO va a escribir, cerramos su punta de escritura
        
        int recibido;
        read(fds[0], &recibido, sizeof(int)); // Bloquea hasta que haya algo que leer
        
        printf("Hijo recibió: %d\n", recibido);
        
        close(fds[0]); // Terminamos de leer
        exit(0);



    } else {


        // --- PROCESO PADRE (EMISOR) ---
        close(fds[0]); // El padre NO va a leer, cerramos su punta de lectura
        
        int enviar = 42;
        write(fds[1], &enviar, sizeof(int));
        
        close(fds[1]); // Cerramos para avisar que no enviaremos más nada
        wait(NULL);    // Esperamos a que el hijo termine para no dejar "zombies"



    }

    return 0;
}