#include<stdio.h>
void main()
{
    int n,first=0,next=1,temp,count=2;
    scanf("%d",&n);
    if(n==0)
        printf("%d",first);
    else if(n==1)
        printf("%d\t%d",first,next);
    else
         printf("%d\t%d\t",first,next);
         while(count<n)
         {
             temp=first+next;
             printf("%d\t",temp);
             first=next;
             next=temp;
             count++;
         }

}
