/**VEremos cosas importantes sobre la ejecucion del fork 
 * Al realizar fork lo que esta sucediendo es que se esta clonando el proceso
 * actual , a partir de que uno reliza un fork() inmediatamente despues 
 * tendremos 2 procesos en simultaneo  que vana aejecutar el mismo codigo 
 * es importante entender esto LOS PROCESOS ACTUALES VANA EJECUTAR EL MISMO 
 * CODIGO
 */

//Bueno para empezar vamos a tener que ejecutar librerias importantes 

#include<stdio.h>//Es la libreria standar de C que nos permite usar lo basico
#include<unistd.h>//Esta es la libreria que nos permite la creacion de los nuevos procesos de nuestro programa, puntualmente  usaremos fork de esta libreria
#include<sys/wait.h>//Vamos a pensar en esta liberria como una "Red de seguridad " esta sirve para gestionar y sincronizar losprocesos creados por fork()



int main(){
    /*Aca estamos creando una variable de tipo int , pero tranquilamente podria ser una variable de tipo pid_t como nombre de la variable 
    pid  y seguido de eso vamos a realizar una llamada a fork()*/
    int pid= fork();//



    if (pid<0){
        perror("Ocurrio un problema con el fork");
        return 1;
    }


    /**Una logica sencila para el uso de getpid and getppid 
     * Si queres saber quien soy llama getpid
     * Si queres saber quien es mi creador usas getppid 
     */
    if(pid==0){
        printf("Soy el proceso hijo y mi pid es: %d\n",getpid());
        printf("El proceso que me creo tiene el pid: %d\n",getppid());
        
    }
    else{
        printf("Soy el proceso padre y mi pid es:%d\n ",getpid());
        printf("El id de mi creador es: %d\n",getppid());
        printf("EL pid de mi hijo es: %d\n",pid);
    }







    return 0;
}



