/*Vamos a ver un ejemplo sencillo de realloc que nos permita analizar la reasignacion de memoria del heap*/

/*Que es exactamente realloc?, es una funcion que lo unico que permite aceptar en sus parametros, el 
puntero original, y ademas reasignar el tamaño  de tu nuevo bloque de memoria*/



#include<stdio.h>
#include<stdlib.h>

int main(){
    
    //Lo unico que estamos haciendo es asignar 2 bloques de memoria de manera dinamica a un segmento del heap
    int *numeros;
    numeros = (int*)malloc(2*sizeof(int));

    //Podemos asignarle un valor a esos bloques de memoria
    numeros[0] = 12;
    numeros[1] = 84;

    printf("El valor numerico es de: %d\n",numeros[0]);
    printf("El valor numerico es de: %d\n",numeros[1]);



    //Vamos a expandir ese bloque de memoria de la siguiente manera 
    //Necesitamos asignar un nuevo bloque de memoria que nos permita expandir ese vector dinamico

    int *temporal = (int*)realloc(numeros,4*sizeof(int)); 

    if(temporal != NULL){
        numeros = temporal;
        numeros[2] = 23;
        numeros[3] = 34;   
    }



    for(int i=0;i<4;i++){
        printf("tenemos entonces: %d\n",numeros[i]);    
    }
    
    
    

    //No olvide hacer el free siempre por cada bloque de mallo se debe de realizar unbloque de free
    free(numeros);

    return 0;
}
