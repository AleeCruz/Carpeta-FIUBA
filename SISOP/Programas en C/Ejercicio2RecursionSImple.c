#include<stdio.h>

//Para entender sobre la recursion debeemos de aprneder sobre los fundamentos 
/**Vamos a realizar los ejercicios del numero factorial y el de fibonacci */

/*Para resover un ejercicio de recursion se necesitan 2 cosas 
IMPORTANTES:
    -Un caso BASE 
    -Un Caso recursivo
    
    */

/**QUe hace el factorial exactamente ?
 * 
numero *factorial(n-1) *factorial(n-2)
 */


 int factorial(int numero){
    
    if(numero==0 || numero ==1){
        return 1;
    }
    else {
        return numero * factorial(numero-1);
    }
 }



int main(){

    int numeroDePrueba=5;

    printf("EL factorial de ");


    return 0;
}