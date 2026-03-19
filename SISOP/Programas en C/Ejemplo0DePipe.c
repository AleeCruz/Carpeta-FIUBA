#include <stdio.h>

int main (){

    int fds[2];
    int msg = 42;


    int r = pipe(fds);


    if(r<0){
        perror("Error en el pipe");
        exit(-1);
    }

    printf("Lectura: %d, Escritura: %d\n",fds[0],fds[1]);


    //Esta linea lo que hace es que se queda bloqueda dado que 
    //No hay nada para leer entonces no podemos hacer nada
    //read (fds[0], &msg , sizeof(msg));// ?????





    //Ahora vamos a escribir en el pipe ¿Como?
    //Vamos a escribir  en el pipe 
    //Teoricamente se estaria hablando a si mismo lo cual no tiene 
    //sentido pero podemos verlo como un ejemplo simple
    write(fds[1],&msg ,sizeof(msg));

    int recibido = 0;


    read (fds[0],&recibido,sizeof(recibido));

    printf("Recibi: %d\n",recibido);





    return 0;
}