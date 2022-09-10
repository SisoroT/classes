#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/*
1. Briefly describe the semantics of the following Unix system calls:

a. fork() - creates a new(child) process by duplicating the calling(parent)
            process. The parent process and child process execute concurrently.

            The child process is an exact duplicate of the parent except:
                - the child has a unique process ID and unique parent process ID
                - the child has its own copy of the parent's data space, stack,
                and heap

b. exit() - terminates the calling process

c. getpid() - returns the process ID of the calling process

d. getppid() - returns the process ID of the parent of the calling process

e. waitpid() - pauses execution of the calling process until a child process
               has been terminated.

f. execl() - Replaces the current process's image and code with a new process's
             image and code.
*/

// 2. Write a C program that uses each of the above system calls at least once.
int main(int argc, char *argv[]) {
  int status;

  // fork a child process
  pid_t pid = fork();

  // error occurred
  if (pid < 0) {
    fprintf(stderr, "Fork Failed");
    return 1;
  }
  // child process
  else if (pid == 0) {
    printf("Child: pid = %d\n", getpid());
    printf("Child: ppid = %d\n", getppid());
    execl("/bin/who", "who", NULL);
  }
  // parent process
  else {
    // parent will wait for the child to complete
    waitpid(pid, &status, 0);
    // display all pids
    printf("\nParent: pid = %d\n", getpid());
    printf("Parent: ppid = %d\n", getppid());
    printf("Parent: child pid = %d\n", pid);
    printf("Child Complete");
  }
  exit(0);
}
