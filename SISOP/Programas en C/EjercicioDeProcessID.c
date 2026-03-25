#include<stdio.h>
#include<unistd.h>

int main(){

    int mi_pid = getpid();
    int pid_padre = getppid();

    printf("Hola soy el proceso actual y este es mi pid: %d\n",mi_pid);
    printf("EL proceso de mi padre es: %d\n",pid_padre);



    return 0;
}