#include<stdio.h>
#include<stdlib.h>

int main(){


    int cantidad=0;
    float *valores;
    float suma=0;

    printf("Cuantos valores de calificacion vas a ingresar ?\n");
    scanf("%d",&cantidad);

    valores = (float*)malloc(cantidad*sizeof(float));

    for(int i=0;i<cantidad;i++){
        printf("Ingrese la calificacion %d: ",i+1);
        scanf("%f",&valores[i]);
        suma +=valores[i];
    }

    float promedio = suma/(float)cantidad;


    printf("EL promedio es de %.2f\n",promedio);


    free(valores);
    valores=NULL;
    return 0;
}