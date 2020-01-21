#include<stdio.h>
void main()
{
    int a[50],i,j,n,suml,sumr,k;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        suml=0;
        sumr=0;
        for(j=0;j<i;j++)
            suml=suml+a[j];
        for(k=i+1;k<n;k++)
            sumr=sumr+a[k];
        if(sumr==suml)
            break;
    }
    printf("%d",a[i]);
}
