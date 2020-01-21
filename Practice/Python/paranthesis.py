exp=input("Enter the expression")
top=0
for ele in exp:
    if ele=='(':
        top=top+1
    else:
        top=top-1
if top==0:
    print("Balanced")
else:
    print("Unbalanced")
