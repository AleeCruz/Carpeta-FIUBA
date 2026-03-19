#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>


int main(){

    int fds_padre_hijo[2];
    int fds_hijo_padre[2];


    int msg =42;//Es el random


    pid_t p = fork();

    //Manejar el Error


    if (p==0){
        //hijo

    }
    else{
        //padre


    }










    return 0;
}