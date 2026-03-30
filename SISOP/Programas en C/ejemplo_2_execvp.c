/**
 * Vamos a ver ejemplos concretos sobre execvp
 * 
 */
 #include<stdio.h>
 #include<stdlib.h>
 #include<sys/wait.h>
 #include<unistd.h>

 int main(){
    printf("Soy el inicio del programa el padre y mi pid es: %d\n",getpid());

    pid_t pid = fork();


    if (pid<0){
        perror("Ocurrio un error en la creacion del fork");
        return -1;
    }

    if (pid==0){
        //Logica del hijo
        printf("\nSoy el hijo y vamos a  tranformarnos mi pid es: %d\n",getpid());
        
        char *args[]={"ls",NULL};
        execvp("ls",args);



        printf("Estas lineas de codigo nunca deberian de ejecutarse");
        return 0;

    }else{
        //Logica del padre
        printf("Soy el padre y mi pid es: %d\n",getpid());

        wait(NULL);

        printf("\nMi hijo ya termino  de realizar sus tareas!!\n");
        printf("Yo eh finalizado debo irme adios\n");

    }







    return 0;
 }
