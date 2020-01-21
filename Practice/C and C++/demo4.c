#include<stdio.h>
#include<math.h>
void main()
{
    int min,max,maxx=-99999,minn=9999,i,j;
    scanf("%d%d",&min,&max);
    for(i=min;i<=max;i++)
    {
        int flag=0;
        if(i==1)
            continue;
        for(j=2;j<=i/2;j++)
        {
            if(i%j==0)
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
             if(i>maxx)
            maxx=i;
        if(i<minn)
            minn=i;
        }
    }
    int sum=maxx+minn;
    printf("%d",sum);
}
