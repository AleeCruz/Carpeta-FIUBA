#include<stdlib.h>
#include<stdio.h>
#include<string.h>



//Vamos a ver sobre el lo que es calloc y como poder usarla para nuestro fines practicos 
/**Veremos que strcpy lo que hace es copiar una cadena de texto desde 
 * strcpy(destino,origen)
 */
int main(){
    char *origen = "Hola Mundo";
    char *destino = (char*)malloc((strlen(origen)+1)*sizeof(char));

    printf("%s\n",origen);


    strcpy(destino,origen);


    

    printf("%s\n",destino);

    free(destino);
    return 0;
}