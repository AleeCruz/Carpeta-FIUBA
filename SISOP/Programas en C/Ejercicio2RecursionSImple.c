/**Se debe de trabajar  sobre el trabajo practico de la catedra de sistemas operativos 
 * el objetivo es de entender el procedimiento de los trabajso practicos 
 * y los procesos que lo abarcan 
 * En esta resolucion vamoa atrabajar sobre  una recursion dado que el trabajo lo 
 * necesita necesariamente sino sera imposible continuar 
 */





 #include<stdio.h>


//Vamos a realizar una funcion recursiva para un numero factorial 
//Cual es la solucion de una funcion recursiva ??

/*La respuesta es un caso base y un caso recursiva (ocurre cuando se llama 
a si mismo pero con un grado de porblema mas pequeño
*/
//Que era el factorial ?
//Es una funcion que se llama a si misma pero con un numero menos 
//Ejemplo
//numero * factorial(numero-1)*factorial(numero -2)*factorial(numero-3)* ...
// 5 fact(4)*fact(3)*fact(2)*fact(1)*fact(0)
int factorial(int numero){

    if(numero ==0 || numero ==1){
        return 1;
    }else {
        return numero*factorial(numero-1);
    }
    
}

/**Ahora vamos a realizar una recursion con el numero de fibonacci 
 * Que es el numero de fibonacci ?
 * 
 * Es una secuencia de numeros donde es la suma de las anteriores 
 * empezando por 0 y 1 
 * 
 *0,1,1,2,3,5,8,13,21

 */


 //Surge la pregunta cual es el caso base de un numero de fibonacci???
 //Caso Base ----> 0 y 1
 //Caso Recursivo ----> fibonacci(numero-1,numero -2);

//Entonces como planteamos la recursion en la estructura de fibonacci???
//Al colocar un numero especifico le estamos preguntando el valor exacto del numero de fibonaccio en esa posicion por ejemplo tengo 
/*Tengo la siguiente secuencia de numeros de fibonacci 
0,1,1,2,3,5,8,13,21,34,55,89,144,233
0,1,2,3,4,5,6, 7, 8, 9,10,11, 12, 13*/ 
//Basicamente estamos haciendo 
//finonacc
int fibonacci(int numero){
    if (numero ==0 ){
        return 0;
    }
    if (numero ==1){
        return 1;
    }
    else {
        return fibonacci(numero-1)+fibonacci(numero-2);
    }
}
 
int main(){

int numeroDePrueba = 13;

   printf("Vamos a ver un ejemplo concreto sobre la recursion\n");
   printf("El factorial de un %d es: %d\n ",numeroDePrueba,factorial(numeroDePrueba));


   printf("La secuencia de fibonacci del numero %d es : %d\n",numeroDePrueba,fibonacci(numeroDePrueba));
    return 0;
 }



