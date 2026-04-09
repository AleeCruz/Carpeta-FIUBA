#include<stdio.h>

#include<stdlib.h>



static char * variable_de_entorno(char *arg) {

    if (arg == NULL){
        printf("No se encontro ninguna la variable de entorno\n");
    }else
        return arg +1;
    
}


int main(){

    char *valor = variable_de_entorno("$USER");
    printf("En Progreso\n");

    printf("Valor de variable de entorno: %s\n",valor);

    return 0;
}