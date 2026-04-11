#include <stdio.h>
#include<stdlib.h>


char *expand_environ_var(char *arg){

    if (arg[0] != '$'){
        return arg;    
    }else{
        char *valor = arg+1;
        char *string = getenv(valor);
        if (string = NULL){
            return string;
        }else{
            arg = string;
            return arg;
        }
    }


    
    
   
}


int main(){

    printf("%s\n",expand_environ_var("$USER"));



    return 0;
}
