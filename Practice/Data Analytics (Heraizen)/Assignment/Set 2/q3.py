n=int(input())

prime=list()

for i in range(2,n+1):
    flag=0
    for j in range(2,i//2+1):
        if i%j==0:
            flag=1
            break
    if flag==0:
        prime.append(i)

print(prime)

sum=0
for ele in prime:
    sum=sum+ele

print(sum)

squareprime=list()
for ele in prime:
    squareprime.append(ele*ele)

print(squareprime)