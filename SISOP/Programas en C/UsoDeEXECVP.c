#include<stdio.h>
#include<stdlib.h>


int main(){

    char *args[] ={"-l",NULL};

    printf("Vamos a preparar la tranformacion correspondiente\n");

    execvp("ls",args);


    printf("Esta linea de codigo nunca se deberia de ejecutar\n");



    return 0;
}