#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main() {
    int pipefd1[2];
    int pipefd2[2];

    if (pipe(pipefd1) == -1 || pipe(pipefd2) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid_t pid1 = fork();
    if (pid1 == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid1 == 0) { // Child process 1: bat
        close(pipefd1[0]);
        dup2(pipefd1[1], STDOUT_FILENO);
        close(pipefd1[1]);
        close(pipefd2[0]);
        close(pipefd2[1]);

        char *argv[] = {"/usr/bin/bat", "--paging=never", "--language=c", "--style=plain", "/home/newton/Documents/programming/c-programming/hello.c", NULL};
        execvp(argv[0], argv);
        perror("execvp bat");
        exit(EXIT_FAILURE);
    }

    pid_t pid2 = fork();
    if (pid2 == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid2 == 0) { // Child process 2: lolcat
        close(pipefd1[1]);
        dup2(pipefd1[0], STDIN_FILENO);
        close(pipefd1[0]);

        close(pipefd2[0]);
        dup2(pipefd2[1], STDOUT_FILENO);
        close(pipefd2[1]);

        char *argv[] = {"/snap/bin/lolcat", NULL};
        execvp(argv[0], argv);
        perror("execvp lolcat");
        exit(EXIT_FAILURE);
    }

    close(pipefd1[0]);
    close(pipefd1[1]);
    close(pipefd2[1]);

    char buffer[1024];
    ssize_t count;
    while ((count = read(pipefd2[0], buffer, sizeof(buffer))) > 0) {
        write(STDOUT_FILENO, buffer, count);
    }

    close(pipefd2[0]);

    waitpid(pid1, NULL, 0);
    waitpid(pid2, NULL, 0);

    return 0;
}