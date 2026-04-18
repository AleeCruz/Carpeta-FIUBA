#include<stdio.h>
#include<stdlib.h>




int main(){

    int *numeros = (int*) malloc(2*sizeof(int));

    numeros[0]=12;
    numeros[1]=39;

    //AHora vamos a extender esa parte de la memoria para que podamos agregar mas de un solo bloque

    int *temporal = (int*)realloc(numeros, 10*sizeof(int));

    if(temporal != NULL){
        numeros = temporal;
        for(int i=2;i<10;i++){
            numeros[i] = 0;
        }
    }

    for(int j=0;j<10;j++){
        printf("EL valor numeros[%d]: %d\n",j,numeros[j]);
    }



    free(numeros);

    return 0;   
}