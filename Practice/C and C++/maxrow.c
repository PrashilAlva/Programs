#include<stdio.h>
void main()
{
    int a[20][20],n,i,j,m,maxrow=-999;
    scanf("%d",&n);
    scanf("%d",&m);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
            scanf("%d",&a[i][j]);
    }
    for(i=0;i<n;i++)
    {
        maxrow=-999;
        for(j=0;j<m;j++)
        {
            if(a[i][j]>=maxrow)
                maxrow=a[i][j];
        }
        printf("%d\t",maxrow);
    }
}
