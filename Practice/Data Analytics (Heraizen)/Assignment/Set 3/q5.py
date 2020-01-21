while(True):
    ch=input("1.Interrogative or Assertive\n2.Exit\n")
    if ch=="1":
        sentence=input("Enter the Sentence?\n")
        if sentence.startswith("Do") or sentence.startswith("Does") or sentence.startswith("Is") or sentence.startswith("Are"):
            print("The entered Sentence is Interrogative...")
        else:
            print ("The entered Sentence is Assertive....")
    elif ch=="2":
        exit()
    else:
        print("Invalid Choice")

