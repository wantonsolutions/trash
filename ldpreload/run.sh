#!/bin/bash

gcc -Wall -o helloworld helloworld.c
./helloworld

gcc -Wall -fPIC -shared -o printf_preload.so printf_preload.c -ldl

LD_PRELOAD=./printf_preload.so ./helloworld

LD_PRELOAD=./printf_preload.so gcc --verbose -o helloworld helloworld.c

