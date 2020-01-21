import random

arr=list()
for i in range(0,16):
    arr.append(random.randint(1,75))

arr.sort(reverse=True)

print(arr)

for ele in arr:
    flag=0
    for j in range(2,(ele//2)+1):
        if ele%j==0:
            flag=1
            break
    if flag==0:
        print(ele,end=" ")