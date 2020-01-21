#include<stdio.h>
void main()
{
    int a,b,c,d,key,count=1,sume=0,sumo=0;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    int tot=a+b+c+d;
    int temp1,temp2,temp3,temp4;
    while(a||b||c||d)
    {
        temp1=a%10;
        temp2=b%10;
        temp3=c%10;
        temp4=d%10;
        a=a/10;
        b=b/10;
        c=c/10;
        d=d/10;
        if(count%2==0)
            sume+=temp1+temp2+temp3+temp4;
        else
            sumo+=temp1+temp2+temp3+temp4;
        count++;
    }
    key=tot-sume-sumo;
    printf("%d",key);
}
