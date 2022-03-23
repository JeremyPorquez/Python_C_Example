An example of how to create a shareable object and import in Python.


To compile:

    gcc -o shareable.so -shared shareable.c 
    gcc -o basic_function_linux.so -shared -fPIC -O2 basic_function.c

Run main.py