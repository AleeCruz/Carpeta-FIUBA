/**Vamos a realizar un ejercicio que tenga que ver con la creacion 
 * de dos procesos en el cual se vana comunicar, donde el proceso padre le enviara 
 * un 43 al proceso hijo el cual el hijo empezara a duplicarlo
 */

 //Vamos a comenzar con las librerias necesarias para que el codigo funcione

 #include<stdio.h>
 #include<unistd.h>
 #include<sys/wait.h>

 
 int main (){

    //Vamos a inicializar algunas variables de apoyo
    int valor_de_pipe=0;
    int fds_padre_hijo[2];
    int READ =0;
    int WRITE=1;

    /**Ahora vamos a crear un pipe unidireccional para que 
     * el proceso padre le envie un mensaje al proceso hijo
     */

    valor_de_pipe=pipe(fds_padre_hijo);

    if(valor_de_pipe<0){
        perror("Ocurrio un error con el pipe");
        return -1;
    }

    //Ahora vamos a crear 2 procesos a partir del procesos actual 

    pid_t pid = fork();

    if(pid<0){
        perror("Ocurrio un error en el fork");
        return -1;
    }

    if(pid ==0){
        //Aca va la logica del hijo 
        //Recordatorio que el hijo unicamente va a leer 
        close(fds_padre_hijo[WRITE]);//el hijo nunca va a escribir 

        int recibido;

        read(fds_padre_hijo[READ],&recibido,sizeof(recibido));

        printf("\nSoy el hijo y mi pid es: %d\n",getpid());
        printf("Soy el hijo y acabo de recibir un %d\n",recibido);
        printf("Como un hijo voy a dupicarlo %d\n",recibido*2);

        close(fds_padre_hijo[READ]);

    }else{
        //Aca va la logica del padre 
        //Recordatorio que el padre unicamente va a escribir
        close(fds_padre_hijo[READ]);

        int escritura=43;

        write(fds_padre_hijo[WRITE],&escritura,sizeof(escritura));

        printf("\nSoy el padre y mi pid es: %d\n",getpid());
        printf("Hola soy el padre y estoy enviando el %d\n",escritura);

        close(fds_padre_hijo[WRITE]);

        wait(NULL);

    }






    return 0;
 }