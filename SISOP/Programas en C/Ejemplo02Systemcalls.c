#include<stdio.h>


int main(){

    printf("Soy un proceso y mi PID es %d\n",getpid());
    int a=4;
    printf("Ademas el valor de la variable a es: %d\n",a);
    //Esta es la linea de codigo principal  que devuelve un valor donde 
    //obtenemos 2 procesos un PADRE y UN HIJO
    int i=fork();

    a=5;



    //La seccion del error en caso de que no funcionara corretamnete el fork()
    if (i<0)
    {
        printf("Error en fork! %d\n",i);
        exit(-1);
    }


    //Seccion del codigo que significa que funciona solamente para el hijo
    if (i>0)
    {
        a =6;
        printf("[PADRE] mi PID es %d\n",getpid());
        printf("[PADRE] a=%d\n",a);
    }
    //Seccion del proceso que solo fucniona para el padre
    else
    {
        printf("[HIJO] mi PID es: %d\n",getpid());
        printf("[HIJO]: a = %d\n",a);
    }
    
    
    printf("Terminado\n\n");



//La pregunta principal es ¿Que es lo que imprime exactamente ?


    exit(0);
}