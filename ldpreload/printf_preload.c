#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif

#include <stdio.h>
#include <dlfcn.h>
#include <stdarg.h>

static int (*orig_printf)(const char *format, ...) = NULL;

int printf(const char *format, ...)
{
 if (orig_printf == NULL)
 {
  orig_printf = (int (*)(const char *format, ...))dlsym(RTLD_NEXT, "printf");
 }
    va_list args;
    va_start(args, format);

 // TODO: print desired message from caller. 
 orig_printf("\nConsider this function interposed on -- Stew\n");
 return vprintf(format, args);
}

static int (*orig_puts)(const char *str) = NULL;
int puts(const char *str)
{
    if (orig_puts == NULL)
    {
        orig_puts = (int (*)(const char *str))dlsym(RTLD_NEXT, "puts");
    }

    // TODO: print desired message from caller.
    return orig_puts("within my own puts");
}

static void* (*real_malloc)(size_t)=NULL;

static void mtrace_init(void)
{
    real_malloc = dlsym(RTLD_NEXT, "malloc");
    if (NULL == real_malloc) {
        fprintf(stderr, "Error in `dlsym`: %s\n", dlerror());
    }
}

static int counter = 0;

void *malloc(size_t size)
{
    if(real_malloc==NULL) {
        mtrace_init();
    }

    void *p = NULL;
    fprintf(stderr, "(%d) malloc(%d) = ", counter++, size);
    p = real_malloc(size);
    fprintf(stderr, "%p\n", p);
    return p;
}