#include<stdio.h>
void main()
{
    int n,low=0,high=1,count=1;
    scanf("%d",&n);
    if(n==1)
        printf("%d",low);
    else if(n==2)
        printf("%d\t%d",low,high);
    else
    {
        printf("%d\t%d\t",low,high);
        while(count<=(n-2))
        {
            int temp=low+high;
            printf("%d\t",temp);
            low=high;
            high=temp;
            count++;
        }
    }
}
