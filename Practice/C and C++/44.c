#include<stdio.h>
void main()
{
    int n1,n2,n3,n4;
    scanf("%d%d%d%d",&n1,&n2,&n3,&n4);
    int totsum=n1+n2+n3+n4,count=1;
    int esum=0,osum=0,temp1,temp2,temp3,temp4;
    while(n1!=0||n2!=0||n3!=0||n4!=0)
    {
        temp1=n1%10;
        temp2=n2%10;
        temp3=n3%10;
        temp4=n4%10;
        n1=n1/10;
        n2=n2/10;
        n3=n3/10;
        n4=n4/10;
        if(count%2==0)
            esum=esum+temp1+temp2+temp3+temp4;
        else
            osum=osum+temp1+temp2+temp3+temp4;
        count++;
    }
    int key=totsum-esum-osum;
    printf("%d",key);
}
