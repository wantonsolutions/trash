#include<stdio.h>
#include<execinfo.h>
#include<stdlib.h>
#include <assert.h>
#include <stdint.h>
#include <signal.h>

//This is how it could be integrated with addr to line
//https://stackoverflow.com/questions/15129089/is-there-a-way-to-dump-stack-trace-with-line-number-from-a-linux-release-binary
unsigned cycles_low, cycles_high, cycles_low1, cycles_high1;

static __inline__ unsigned long long rdtsc(void)
{
    __asm__ __volatile__ ("RDTSC\n\t"
            "mov %%edx, %0\n\t"
            "mov %%eax, %1\n\t": "=r" (cycles_high), "=r" (cycles_low)::
            "%rax", "rbx", "rcx", "rdx");
}

static __inline__ unsigned long long rdtsc1(void)
{
    __asm__ __volatile__ ("RDTSC\n\t"
            "mov %%edx, %0\n\t"
            "mov %%eax, %1\n\t": "=r" (cycles_high1), "=r" (cycles_low1)::
            "%rax", "rbx", "rcx", "rdx");
}

/* Obtain a backtrace and print it to stdout. */
void
print_trace (void)
{
  void *array[10];
  char **strings;
  int size, i;

  size = backtrace (array, 10);
  strings = backtrace_symbols (array, size);
  if (strings != NULL)
  {

    printf ("Obtained %d stack frames.\n", size);
    for (i = 0; i < size; i++)
      printf ("%s\n", strings[i]);
  }

  free (strings);
}

static volatile int keepRunning = 0;
void intHandler(int dummy) {
    rdtsc();
    print_trace();
    rdtsc1();
    uint64_t start, end;
    start = ( ((uint64_t)cycles_high << 32) | cycles_low );
    end = ( ((uint64_t)cycles_high1 << 32) | cycles_low1 );
    printf("\ncycles spent printing stack trace %lu\n", end - start);    
    keepRunning++;
    printf("Will allow %d more breaks\n",10-keepRunning);

    if (keepRunning >= 10){
      exit(0);
    }
}

int fcall() {
  printf("Press ctrl+c to print stack trace\n");
  while(1){}
}

int main() {
    signal(SIGINT, intHandler);
    fcall();
}