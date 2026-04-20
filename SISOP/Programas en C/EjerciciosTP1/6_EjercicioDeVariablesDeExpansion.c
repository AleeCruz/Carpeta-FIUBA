#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char *expand_envirom_var(char* arg){

    if(arg[0]!='$'){
        return arg;
    }

    char *cadena = getenv(arg+1);

    if(cadena == NULL || strlen(cadena)==0){
        return NULL;
    }

    char *temporal = (char*)malloc((strlen(cadena)+1)*sizeof(char));

    if (temporal !=NULL){
        strcpy(temporal,cadena);
    }

    return temporal;
}



int main(){
    //Vamos a probar si funciona una variable de entorno vacia 
    setenv("$VACIA","",1);
    char *string = "$HOME";

    
    char *cadenaPointer = expand_envirom_var(string);
    
    
    if(cadenaPointer==NULL)
        printf("Valor NULL\n");
    else{
        printf("La cadena es: %s\n", cadenaPointer);
        free(cadenaPointer);
    }
    
    return 0;
}