#include<stdio.h>
#include<stdlib.h>

int main(){

    char *valor = getenv("HOME");



    if (valor == NULL){
        printf("Buen intento pero esa variable de entorno no existe jaja\n");
    }else{
        printf("Ten tu codigo de variable de entorno: %s\n",valor);
    }

    return 0;
}