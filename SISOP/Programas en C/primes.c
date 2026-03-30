/**
 * Ahora podremos trabajar con la interfaz y la correspondiente logica de primes
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>


#define READ 0
#define WRITE 1

void
filtro(int fds_in)
{
	/**
	 * Inicializamos las variables correspondietes y leemos desde el proceso
	 *  padre de entrada
	 *
	 */

	int p;
	ssize_t bites_lectura = read(fds_in, &p, sizeof(p));

	if (bites_lectura == 0) {
		exit(0);
	}
	if (bites_lectura < 0) {
		printf("Ocurrio un error con la lectura");
		close(fds_in);
		exit(1);
	}
	printf("primo %d\n", p);
	fflush(stdout);

	/**
	 * Creacion de los nuevos fds y los pipes correspondientes
	 */

	int fds[2];
	int pipes_r = pipe(fds);

	if (pipes_r < 0) {
		perror("Ocurrio un error en la en la creacion del pipe en la "
		       "recursion\n");
		exit(0);
	}

	pid_t pid = fork();

	if (pid < 0) {
		perror("Ocurrio un error con la creacion de procesos\n");
		exit(0);
	}

	if (pid == 0) {
		// Aca va la Logica del hijo
		close(fds[WRITE]);
		close(fds_in);

		filtro(fds[READ]);

		close(fds[READ]);
		exit(0);

	} else {
		// Aca va la logica del padre
		// Lo que nunca va a realizar el padre es LEER
		close(fds[READ]);

		int numero;
		ssize_t bites_lectura = read(fds_in, &numero, sizeof(numero));

		while (bites_lectura > 0) {
			if (numero % p != 0) {
				write(fds[WRITE], &numero, sizeof(numero));
			}
			bites_lectura = read(fds_in, &numero, sizeof(numero));
		}


		close(fds_in);
		close(fds[WRITE]);


		wait(NULL);
	}
}


int
main(int argc, char *argv[])
{
	if (argc < 2) {
		printf("Ocurrio un error con la Interfaz\n");
		printf("Intenta con el comando: %s <n>\n", argv[0]);
		return -1;
	}

	int numeroRecibido = atoi(argv[1]);

	// Ahora vamos a obligar al usuario a usar numeros mayores o iguales que 2

	if (numeroRecibido < 2) {
		printf("Error debes de ingresar numero mayores o iguales que "
		       "2\n");
		return 0;
	}


	int fds_principal[2];

	int pipe_principal = pipe(fds_principal);

	if (pipe_principal < 0) {
		perror("Ocurrio un error con la creacion del pipe\n");
		return -1;
	}

	// Ahora vamosa crear nuevos procesos a partir del actual

	pid_t pid = fork();

	if (pid < 0) {
		perror("Ocurrio un problema con el fork pricipal\n");
		return -1;
	}


	if (pid == 0) {
		// Aca va la logica del hijo............
		// Recordar que el primer filtro nunca va a escribir

		close(fds_principal[WRITE]);
		/*
		int numeroleido;
		read(fds_principal[READ],&numeroleido,sizeof(numeroleido));
		printf("El valor recibido del padre fue %d\n",numeroleido);
		*/

		filtro(fds_principal[READ]);

		close(fds_principal[READ]);
		return 0;


	} else {
		// Aca va la logica del padre...............
		// Recordar que el padre nunca va a leer asi que es importante tener eso en cuenta
		close(fds_principal[READ]);

		for (int i = 2; i <= numeroRecibido; i++) {
			write(fds_principal[WRITE], &i, sizeof(i));
		}

		close(fds_principal[WRITE]);

		wait(NULL);
	}


	return 0;
}
