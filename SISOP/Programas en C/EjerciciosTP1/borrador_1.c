

//Vamos a realizar una copia de cadena de caracteres de un string original  a una copia


#include <stdio.h>
#include<stdlib.h>


static char *
expand_environ_var(char *arg)
{
    // tu código acá

    if(arg[0]!='$'){
        return arg;
    }else{
        char *valor = getenv(arg+1);
        if (valor==NULL){
            valor = "CadenaStringVacia";
            return valor;
        }

    }

    return arg;
}




int main(){
    

    char *string = expand_environ_var("$USER\n");

    printf("\nLa cadena de string que tenemos es: %s\n",string);
    






    return 0;
}
