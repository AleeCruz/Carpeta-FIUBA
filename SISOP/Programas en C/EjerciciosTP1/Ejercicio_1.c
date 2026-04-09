#include<stdio.h>
#include<stdlib.h>


int main(){

    char *arg = "$HOME";

    printf("tenemos entonces : %s\n",getenv(arg+1));



    return 0;
}