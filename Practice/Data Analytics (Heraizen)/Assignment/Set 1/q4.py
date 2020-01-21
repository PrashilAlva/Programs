first=0
next=1

temp=0
print(first,next,end=",")

while(temp!=34):
    temp=first+next
    if temp==34:
        print(temp)
        break
    print(temp,end=",")
    first=next
    next=temp
