#include <stdio.h>

int main() {



}





/**Debo de agregar lo siguiente a la funcion de expand_environ_var
 * 


 * 	if (arg[0] != '$') {
		return arg;
	}

	if (strcmp(arg + 1, "?") == 0) {
		extern int status;
		char buf[16];
		snprintf(buf, sizeof(buf), "%d", status);
		arg = realloc(arg, strlen(buf) + 1);
		strcpy(arg, buf);
		return arg;
	}

	char *valor = getenv(arg + 1);

	if (valor == NULL) {
		valor = "";
	}

	arg = realloc(arg, strlen(valor) + 1);
	strcpy(arg, valor);
	return arg;
 * 
 * 
 */





 /**Ademas debo de agregar lo siguiente a la funcion parse_exec
  * 
  * 
  * 
  * 		if (strlen(tok) == 0) {
                free(tok);
                continue;
            }



            Mas alla del codigo lo importante es entender que esta pasando.
  */
