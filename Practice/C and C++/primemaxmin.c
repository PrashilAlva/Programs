#include<stdio.h>
void main()
{
    int min=999999,max=-9999999,low,high,i,j;
    scanf("%d%d",&low,&high);
    for(i=low;i<=high;i++)
    {
        int flag=0;
        for(j=2;j<=(i/2);j++)
        {
            if(i%j==0)
                flag=1;
                break;
        }
        if(flag==0)
        {
            if(i<min)
                min=i;
            if(i>max)
                max=i;
        }

    }
    int sum=min+max;
    printf("%d",sum);
}
