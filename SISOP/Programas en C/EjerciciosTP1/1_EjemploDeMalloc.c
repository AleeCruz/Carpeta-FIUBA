#include<stdio.h>
#include<stdlib.h>


int main(){

    //Vamos a realizar una reserva de memoria de 4 int de manera dinamica

    int *vector = (int*)malloc (5*sizeof(int));

    vector[0] = 32;
    vector[1] = 54;
    vector[2] = 35;
    vector[3] = 213;    
    vector[4] = -124;

    //Vamos a realizar una impresion de todos los elementos del vectro dinamico

    for (int i=0; i<5; i++){    
        printf("EL numeor es: %d\n",vector[i]);
    }

    //IMportante por cada malloc que este realizando debes de realizar la corresponidiente liberacion
    free(vector);
}
