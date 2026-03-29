#include<stdio.h>
//Para usar el fork y el pipe debemos de usar 2 librerias muy particulares
//Que son justamente las que estan abajo
#include<sys/types.h>
#include<unistd.h>


/*
 * Tabla de FDS
 * 0: stdin (Es un FDS a algo que apunta a la cosa)
 * 1: stdout 
 * 2: stderr
 * 3: pipe_read
 * 4: pipe_write
 */




int main(){

    int fds_padre_hijo[2];//[read,write]
    int fds_hijo_padre[2];

    int msg =42;//Es el random


    //Por que deberiamos crear  los pipes antes del fork 
    //Cual es la justificacion?
    //Deberiamo crear 2 pipes para realizar la comunicacion de 
    //dos procesos

    /*Que hace el pipe concretamente ??? EL pipe crea file descriptor con 
    EL pipe intenta modelar la entrada y la salida de un file descripto 
    como la entrada y la salida del mismo .




    Que es un File Descriptor ? Es un "numero puro" . Es un apuntador para apuntar a recursos(archivo de teclado , archivo de pantalla, etc ) en resumen es como
    un puntero  que apunta a cosas o algo , que viven en cada proceso A. 
    
    Un proceso puede de tener 2 files descriptors para entrada y la salida  de datos 
    */

    //Al realizar un pipe(fds_padre_hijo)
    pipe(fds_padre_hijo);// padre-->hijo

    //No olvidar el manejo del error del primer pipe



    /**
     * Tabla de FDS
     * 0: stdin (Es un FDS a algo que apunta a la cosa)
     * 1: stdout 
     * 2: stderr
     * 3: pipe_read
     * 4: pipe_write
     */

    //Al crear otro pipe tenemos lo siguiente 

    pipe(fds_hijo_padre);//hijo-->padre

    //No olvidar el manejo del error



    /**
 * Tabla de FDS
 * 0: stdin (Es un FDS a algo que apunta a la cosa)
 * 1: stdout 
 * 2: stderr
 * 3: pipe1_read
 * 4: pipe1_write
 * 5: pipi2_read
 * 6: pipe2_write
 */

    //QUe va a suceder despues del fork()????
    //Tendremos lo siguoente .....
    pid_t p = fork();

    //No olvidar el manejo del error para el fork 


/*
 * Tabla de FDS  - Padre
 * 0: stdin (Es un FDS a algo que apunta a la cosa)
 * 1: stdout 
 * 2: stderr
 * 3: pipe1_read
 * 4: pipe1_write
 * 5: pipi2_read
 * 6: pipe2_write
 */


 /*
 * Tabla de FDS  - Hijo
 * 0: stdin (Es un FDS a algo que apunta a la cosa)
 * 1: stdout 
 * 2: stderr
 * 3: pipe1_read
 * 4: pipe1_write
 * 5: pipi2_read
 * 6: pipe2_write
 */












    //Manejar el Error
    if (p<0){
        printf("El fork no funciono correctamente");
    }


    const int READ_FD=0;
    const int WRITE_FD=1;

    if (p==0){
        //hijo
        //Tendremos que cerrar los FDS que los procesos no esten usando

        close(fds_padre_hijo[WRITE_FD]);
        close(fds_hijo_padre[READ_FD]);


        int buf_lectura;
        read(fds_padre_hijo[READ_FD],&buf_lectura, sizeof(buf_lectura));

        printf("Hijo recibe valor: %d\n",buf_lectura);


        write(fds_hijo_padre[WRITE_FD],&buf_lectura,sizeof(buf_lectura));
    
        //Debemos de realizar el cierre de los file descriptors

        close(fds_padre_hijo[READ_FD]);
        close(fds_hijo_padre[WRITE_FD]);
        
    
    }
    else{
        //padre

        //Aca tambien debemos de cerrar los FDS que no se esten usando 
        close(fds_padre_hijo[READ_FD]);
        close(fds_hijo_padre[WRITE_FD]);




        write(fds_padre_hijo[WRITE_FD],&msg,sizeof(msg));

        int buf_lectura_padre;
        read(fds_hijo_padre[READ_FD],&buf_lectura_padre,sizeof(buf_lectura_padre));

        printf("Padre recibe un valor: %d\n",buf_lectura_padre);

        //Aca tambien debemos de realizar los cierres de los FDS


        close(fds_padre_hijo[WRITE_FD]);
        close(fds_hijo_padre[READ_FD]);

    }
  









    return 0;
}




//Nos quedamos en el minuto 2:42:00