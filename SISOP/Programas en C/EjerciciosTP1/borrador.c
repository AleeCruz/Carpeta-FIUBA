/**Vamos a realizar un nuevo ejercico con malloc and realloc 
 * Que es lo que hace cada uno ?
 * Malloc reserva memoria que lo almacena en el HEAP
 * y realloc lo unico que hace es reasignar(ampliao reduce)
 */


 #include<stdio.h>
 #include<stdlib.h>

 int main(){

    int *numeros = malloc(2*sizeof(int));

    numeros[0]=23;
    numeros[1]=56;

    printf("Los numeros son los siguientes: %d %d\n",numeros[0],numeros[1]);
    

    return 0;
 }
