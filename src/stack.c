#include <stdlib.h>  
#include <stdio.h>  
#include <string.h>  


int foo(char *str)  {  
    char buffer[100];
    strcpy(buffer, str);
    return 1;  
}  


int main()  {  
    char str[400];  
    FILE *badfile; 
    badfile = fopen("/home/zamyang/program/computer_security/src/output/badfile", "r");  
    fread(str, sizeof(char), 320, badfile); 
    foo(str);  
    printf("Returned Properly\n");  
    return 0;  
}
