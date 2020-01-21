while(True):
    ch=input("1.Singular to Plural\n2.Exit\n")
    if ch=="1":
        date=input("Enter the Singular word?\n")
        print("Plural of ",date," is:",date.replace("y","ies"))
    elif ch=="2":
        exit()
    else:
        print("Invalid Choice")
