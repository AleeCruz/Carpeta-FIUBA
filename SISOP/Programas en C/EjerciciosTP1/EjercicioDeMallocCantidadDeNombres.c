#include<stdio.h>
#include<stdlib.h>


int main(){

    int n;
    printf("Cuantas letras tiene tu nombre?");
    scanf("%d",&n);


    char *nombre = (char*)malloc(n*sizeof(char));

    printf("Ingrese su nombre:");
    scanf("%s",nombre);

    printf("Tu nombre es: %s\n",nombre);

    for (int i=n;i>=0;i--){
        printf("%c",nombre[i]);
    }

    printf("\n");

    free(nombre);

    return 0;
}