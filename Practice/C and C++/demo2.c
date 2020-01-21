#include<stdio.h>
void main()
{
    int a[50][50],n,m,maxrow=-99999,i,j;
    scanf("%d%d",&n,&m);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
            scanf("%d",&a[i][j]);
    }
    for(i=0;i<n;i++)
    {
        maxrow=-99999;
        for(j=0;j<m;j++)
            if(maxrow<a[i][j])
            maxrow=a[i][j];
        printf("%d",maxrow);
    }
}
