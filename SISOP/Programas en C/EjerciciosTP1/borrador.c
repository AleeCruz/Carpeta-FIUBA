//Vamos a hacer un ejercicios simmple del uso de malloc con el cual 
//Nosotros vamos a reservar una cantidad de memoria que nos permita simular un array estatico


#include<stdio.h>
#include<stdlib.h>


int main(){

    
    //vamos a hacer una reserva de memoria 
    int *arreglo = (int*)malloc (4*sizeof(int));
    
    arreglo[0] = 32;
    arreglo[1] = 54;
    arreglo[2] = 35;
    arreglo[3] = 213;


    printf("Los numero asignado es: %d\n",arreglo[0]);
    printf("Los numero asignado es: %d\n",arreglo[1]);
    printf("Los numero asignado es: %d\n",arreglo[2]);
    printf("Los numero asignado es: %d\n",arreglo[3]);


    return 0;
}
