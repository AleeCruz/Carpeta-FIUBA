#include<stdio.h>

int main(){

    printf("Mi PID es: %d\n", getpid()  );

    int i = fork();


    if(i<0){
        printf("Error en fork! %d\n",i);
    }
    if (i==0){
        printf("Soy el proceso hijo y mi ID es: %d\n",getpid());
    }else{
        printf("Soy el porceso padre y mi ID es: %d\n",getpid());
    }


    printf("\nTerminado\n");

    exit(0);
    return 0;
}