date=input("Enter the Current Date (mm-dd-yyyy) or (mm/dd/yyyy)\n")
if "/" in date:
    print("Changed Format\n",date.replace("/","-"))
elif "-" in date:
    print("Changed Format\n",date.replace("-","/"))
