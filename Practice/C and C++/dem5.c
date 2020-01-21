#include<stdio.h>
void main()
{
    int n,s[5],top=-1,temp,i;
    scanf("%d",&n);
    while(n)
    {
        temp=n%2;
        s[++top]=temp;
        n=n/2;
    }
    for(i=top;i>-1;i--)
        printf("%d",s[i]);
}
