sentence = "Hello all good day all all Hello good"
liste=sentence.split()
dictio = dict()

for ele in liste:
    if ele not in dictio:
        dictio[ele] = 1
    else:
        dictio[ele] += 1

print('Word Count is:')
for ele in dictio:
    print(ele, ' : ', dictio[ele])

print(len(dictio))

maxx=-99999
maxele=""
minn=99999
minele=""

for ele in dictio:
    if dictio[ele]>maxx:
        maxx=dictio[ele]
        maxele=ele
    if dictio[ele]<minn:
        minn=dictio[ele]
        minnele=ele

print("Element with maximum occurance is :",maxele)
print("Element with minimum occurance is :",minnele)


