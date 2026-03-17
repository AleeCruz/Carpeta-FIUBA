#include<stdio.h>

int main(){

    printf("Mi PID es: %d\n",getpid());

    int i = fork();


    if (i<0){
        printf("Ocurrio algun error con el fork\n");
        exit(0);
    }


    if(i==0){
        printf("Soy el proceso hijo y mi PID es: %d\n",getpid());
    }else{
        printf("Soy el proceso pade y mi PID es: %d\n",getpid());
    }




    printf("Esta linea de codigo se ejecutara en Padre e Hijo\n");
    printf("Terminado\n");

    return 0;
}