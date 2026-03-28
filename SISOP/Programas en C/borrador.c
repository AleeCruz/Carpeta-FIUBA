//Vamos a hacerlo de nuevo para que quede claro la lectura y la escritura de los procesos correspondientes 



#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>


int main(){
    //Debemos crear un vector de 2 posiciones para la los fds
    int fds_padre_hijo[2];
    int valor_de_pipe=0;
    int READ = 0;
    int WRITE = 1;

    //Ahora vamos a crear nuestro pipe con el vector de dos coordenadas 

    valor_de_pipe = pipe(fds_padre_hijo);

    if(valor_de_pipe<0){
        perror("Ocurrio un erro con el pipe ");
        return 1;
    }

    //Ahora vamos a clonar ambos procesos 
    pid_t pid = fork();

    if(pid<0){
        printf("Ocurrio un error en la creacion de los procesos\n");
        return;
    }

    if(pid ==0 ){
        //La unica tarea del hijo es que solo pueda leer 
        close(fds_padre_hijo[WRITE])


    }else{
        //La unica tarea del padre es que solo pueda escribir 


    }




    return 0;
}