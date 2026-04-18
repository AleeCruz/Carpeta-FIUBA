#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *expand_environ_var(char *arg) {
    // 1. Si NO empieza con '$', devolver arg sin cambios
        if (arg[0]!='$'){
            return arg;
        }
    // 2. Saltar el '$' para obtener el nombre de la variable
    //    Pista: arg + 1

    // 3. Usar getenv() para obtener el valor
        char *string = getenv(arg+1);//Vamos a pasar el "$LaCadenaDeTextoSinElSignoDolar"

       
    // 4. Si no existe o es vacía, devolver NULL
        if (string ==NULL){
            return NULL;
        }

    // 5. Copiar el valor con calloc + strcpy y devolverlo
        char *cadena = (char*)malloc((strlen(string)+1)*sizeof(char));

        strcpy(cadena,string);
        return cadena;
}

int main() {
    char *casos[] = {"$HOME", "echo", "$NOEXISTE", "$USER", NULL};

    for (int i = 0; casos[i] != NULL; i++) {
        char *resultado = expand_environ_var(casos[i]);
        if (resultado == NULL)
            printf("NULL\n");
        else{
            printf("%s\n", resultado);
            if (casos[i][0] == '$')
                free(resultado);
        }
           
    }
    return 0;
}