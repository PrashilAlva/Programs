num=int(input())

temp=num
spacec=0
oddc=1
for a in range(0,num-1):
    oddc=oddc+2

print(oddc)
for i in range(0,num):
    for j in range(0,spacec):
        print(" ",end="")
    for k in range(0,oddc):
        print(k+1,end="")
    spacec=spacec+1
    oddc=oddc-2
    print()

