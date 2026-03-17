#include<stdio.h>


int main(){
    
    int fds[2];

    int msg=42;


    int r = pipe(fds);

    if (r<0){
        perror("Error de pipe");
        exit(-1);
    }

    printf("Lectura: %d, Escritura: %d\n",fds[0],fds[1]);





    return 0;
}