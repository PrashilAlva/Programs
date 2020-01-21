num=int(input())

continuee=1

while(True):
    sum=0
    while(num>0):
        temp=num%10
        sum=sum+temp
        num=num//10
    temp2=sum
    count=0
    while(temp2>0):
        count=count+1
        temp2=temp2//10
    if(count==1):
        break
    else:
        num=sum

print("The sum is:",sum)


        