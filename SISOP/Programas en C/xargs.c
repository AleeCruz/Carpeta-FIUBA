#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#ifndef NARGS
#define NARGS 4
#endif

int
main(int argc, char *argv[])
{
	if (argc < 2) {
		fprintf(stderr, "Uso: %s <comando>\n", argv[0]);
		exit(1);
	}

	char *cmd = argv[1];
	char *args[NARGS + 2];
	args[0] = cmd;

	char *line = NULL;
	size_t cap = 0;
	ssize_t len;
	int count = 0;

	while ((len = getline(&line, &cap, stdin)) != -1) {
		if (len > 0 && line[len - 1] == '\n') {
			line[len - 1] = '\0';
			len--;
		}

		args[1 + count] = strdup(line);
		count++;

		if (count == NARGS) {
			args[1 + count] = NULL;

			pid_t pid = fork();
			if (pid < 0) {
				perror("fork");
				exit(1);
			}
			if (pid == 0) {
				execvp(cmd, args);
				perror("execvp");
				exit(1);
			}
			wait(NULL);

			for (int i = 0; i < count; i++) {
				free(args[1 + i]);
				args[1 + i] = NULL;
			}
			count = 0;
		}
	}

	if (count > 0) {
		args[1 + count] = NULL;

		pid_t pid = fork();
		if (pid < 0) {
			perror("fork");
			exit(1);
		}
		if (pid == 0) {
			execvp(cmd, args);
			perror("execvp");
			exit(1);
		}
		wait(NULL);

		for (int i = 0; i < count; i++) {
			free(args[1 + i]);
			args[1 + i] = NULL;
		}
	}

	free(line);

	return 0;
}