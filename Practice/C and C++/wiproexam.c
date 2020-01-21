#include<stdio.h>
void main()
{
    int s[50],n,k,top=-1,count=0,i,arr[50],j=0;
    scanf("%d",&n);
    scanf("%d",&k);
    int temp=n;
    while(temp)
    {
        s[++top]=temp%10;
        temp=temp/10;
        count++;
    }
    for(i=top;i>-1;i--)
    {
        arr[j]=s[i];
        j++;
    }
    int start=k%count;
    for(i=0;i<count;i++)
    {
        if(start>=count)
        {
            start=0;
            printf("%d",arr[start]);
        }
        else
            printf("%d",arr[start]);
        start++;
    }
}
