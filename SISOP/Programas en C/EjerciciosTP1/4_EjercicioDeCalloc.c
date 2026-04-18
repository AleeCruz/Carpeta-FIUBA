#include<stdio.h>
#include<stdlib.h>

int main(){

    int cantidadDeElementos = 20;
    float *puntajes = (float*) calloc(cantidadDeElementos,sizeof(float));

    for(int i=0;i<cantidadDeElementos;i++){
        printf("El valor %d es: %.2f\n",i,puntajes[i]);
    }


    free(puntajes);
    return 0;
}