/**
 * Vamos a crear un codigo que nos permita tener una comunicacion entre tres procesos 
 * Vamos a llamar Proceso A , Proceso B y el Proceso c.
 * ¿Cuál es la responsabilidad de cada uno?
 * 
 * Proceso A: Su única responsabilidad es la creacion de de numeros que van desde 
 * el 1 hasta el 10.
 * 
 * Esos valores lo ESCRIBE  y se lo envia al proceso hijo que en este caso es B
 * 
 * 
 * Proceso B: Su unico responsabilidad es la filtracion de de los numeros que lee del 
 * proceso A (solo Lectura) ----FILTRA------ y despues ESCRIBE para el proceso C
 * 
 * Porceso C: Su unica responsabilidad es la lectura de los numeros enviados
 * por el procesos (SOLO Lectura) del proceso B ---- y luego imprime 
 */



 #include<stdio.h>
 #include<sys/wait.h>
 #include<unistd.h>

 int main (){

    //Primeros las contantes
    int READ =0;
    int WRITE =1;

    //Despues las inicializaciones basicas 
    int fds_PadreA_HijoB[2];
    int valor_pipe_1;

    
    
    //Despues de todo lo anterior nos concentramos en la creacion del pipe

    valor_pipe_1 = pipe(fds_PadreA_HijoB);
    
    if (valor_pipe_1<0){
        perror("Ocurrio un error con la creacion del pipe ");
        return -1;
    }

    //Ahora nos concentramos en la creacion de los procesos Padre(ProcesoA) e Hijo(ProcesoB)


    pid_t pid1 = fork();


    if (pid1<0){
        perror("Ocurrio un error enla inicializacion el fork");
        return -1;
    }



    if (pid1==0){

        //Aca va la logica del hijo nos referimos a Proceso B 
        //Recordatorio importante el proceso B solo lee del fds_PadreA_HijoB[READ]

        close(fds_PadreA_HijoB[WRITE]);//El proceso B Nunca escribe hacia el padre

        //Reeimplementamos la logica del principio pero para una nueva comunicacion entre el proceso B y proceso C

        int fds_PadreB_HijoC[2];
        int valor_pipe_2;

        valor_pipe_2 = pipe(fds_PadreB_HijoC);

        if (valor_pipe_2 < 0){
            perror("Ocurrio un error en la creacion de un error\n");
            return -1;
        }

        pid_t pid2 = fork();

        if(pid2<0){
            perror("Ocurrio un error con el comando fork");
            return -1;
        }


        if(pid2==0){
            //Aca va la logica del proceso Hijo nos referimos al proceso C
            //Cual es la tarea principal del Proceso C? 
            /*  -Solo Lee lo que escribio e proceso B 
                -Imprime todos lo valores que recibe 
            */
            close(fds_PadreB_HijoC[WRITE]);
            close(fds_PadreA_HijoB[READ]);
            
            int numero;

            ssize_t bytes_leidos = read(fds_PadreB_HijoC[READ],&numero,sizeof(numero));

            while(bytes_leidos>0){
                printf("Los valores impresos son: %d\n",numero);
                bytes_leidos = read(fds_PadreB_HijoC[READ],&numero,sizeof(numero));
            }
            
            close(fds_PadreB_HijoC[READ]);
            
            return 0;


        }else{
            //Aca continua la logica del proceso B nos referimos al hijo de A
            //Cuál es la tarea principal del proceso B??
            //  -Leer del fds_PadreA_HijoB[READ]
            //  -Escribir para el fds_PadreB_HijoC[WRITE]
            //  -filtrar los numeros que lee del proceso A

            close(fds_PadreA_HijoB[WRITE]);
            close(fds_PadreB_HijoC[READ]);

            int numero;

            ssize_t bytes_leidos = read(fds_PadreA_HijoB[READ],&numero,sizeof(numero));
           
            while (bytes_leidos>0)
            {
                if (numero %2 == 0){
                    write(fds_PadreB_HijoC[WRITE],&numero,sizeof(numero));
                }
                bytes_leidos=read(fds_PadreA_HijoB[READ],&numero,sizeof(numero));
            }

            close(fds_PadreA_HijoB[READ]);
            close(fds_PadreB_HijoC[WRITE]);
            
            wait(NULL);
            return 0;
            
        }


    }else{
        //Aca va la logica del Padre nos referimos al Proceso A
        close(fds_PadreA_HijoB[READ]);//Recordar que el procesoA-Padre (NO LEE)/ESCRIBE

        
        for (int i =1;i<=100;i++){
            write(fds_PadreA_HijoB[WRITE],&i,sizeof(i));
        }
        //Una vez que termina de leer cierra del FDS de 
        close(fds_PadreA_HijoB[WRITE]);
        
        //Es importante realizar un wait para evitar un proceso hijo en estado zombie
        wait(NULL);
        return 0;
    }

    
    




    return 0;
 }