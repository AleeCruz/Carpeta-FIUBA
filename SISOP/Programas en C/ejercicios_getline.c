#include<stdio.h>
#include<stdlib.h>

int main(){
    char *buffer = NULL;//No reservamos memoria todavia
    size_t capaciadad = 0;//Tamaño actual de la memoria 
    ssize_t caracteres_leidos;


    printf("Escribir algo largo para ver como funciona: ");
    
    caracteres_leidos = getline(&buffer,&capaciadad,stdin);


    if (caracteres_leidos != -1){
        printf("Lei %zd  caracteres\n",caracteres_leidos);
        printf("EL texto es: %s\n",buffer);
        printf("Memoria total reservada: %zu\n",capaciadad);

    }

    free(buffer);

    return 0;
}