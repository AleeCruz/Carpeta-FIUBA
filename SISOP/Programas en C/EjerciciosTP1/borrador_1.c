#include<stdio.h>
#include<stdlib.h>


int main(){

    setenv("$VACIO","",1);


    printf("La variable de entorno es %s\n",getenv("$VACIO"));

    //Vamos a ver otro ejemplo concreto 

    setenv("$ValorInvalido","AJIOJIO",1);

    printf("EL valor de la variable es: %s\n",getenv("$ValorInvalido"));

    return 0;
}