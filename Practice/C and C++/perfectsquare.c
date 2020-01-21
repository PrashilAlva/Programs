#include<stdio.h>
#include<math.h>
void main()
{
    int n,a[50],i,count=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        float sqrtt=sqrt((double)a[i]);
        int sqr=sqrtt;
        if(sqr==sqrtt)
            count++;
    }
    printf("%d",count);
}
