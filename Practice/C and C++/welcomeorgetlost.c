#include<stdio.h>
void main()
{
    if(fgetc(stdin)==0x0A)
        printf("Welcome");
    else
        printf("Get Lost!");
}
