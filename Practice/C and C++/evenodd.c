#include<stdio.h>
void main()
{
    int a[50],ori[50],n,i,j=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        if(a[i]%2==0)
        {
            ori[j]=a[i];
            j++;
        }
    }
    for(i=0;i<n;i++)
    {
        if(a[i]%2!=0)
        {
            ori[j]=a[i];
            j++;
        }
    }
    for(i=0;i<n;i++)
        printf("%d\t",ori[i]);
}
