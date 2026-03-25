#include<stdio.h>
#include<unistd.h>


int main(){

    int mi_pid = getpid();
    int pid_padre = getppid();

    
    printf("Este es mi Procces ID : %d\n",mi_pid);
    printf("Este es el procces ID de mi padre que me llamo : %d\n",pid_padre);



    return 0;
}