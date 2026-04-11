#include<stdio.h>

#include<stdlib.h>


int main(){

    printf("Vamos a imprimir las variables de entorno\n");

    printf("HOME: %s\n",getenv("HOME"));


    printf("USER: %s\n",getenv("USER"));


    return 0;
}