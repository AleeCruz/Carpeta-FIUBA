#include<stdio.h>
#include<stdlib.h>



int main(int argc, int *argv[]){

    if (argc<2){
        printf("Error en el ingreso de argumentos\n");
        printf("Intenta con el comando: %s <n>\n",argv[0]);
        return -1;
    }

    int numeroRecibido = atoi(argv[1]);

    printf("El argumento recibido fue: %d\n",numeroRecibido);

    return 0;
}