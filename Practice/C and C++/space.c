#include<stdio.h>
#include<string.h>
void main()
{
    char ch[1000];
    gets(ch);
    int i,count=0;
    for(i=0;ch[i]!='\0';i++)
    {
        if(ch[i]==' ')
            count++;
    }
    printf("%d",count);
}
