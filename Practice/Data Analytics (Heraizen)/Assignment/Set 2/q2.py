dictio=dict()

while(True):
    choice=int(input("1.Add Student Details\n2.Display Students\n3.Search Student\n4.Exit\n"))
    if choice==1:
        student_id=input("Enter the Student ID:")
        student_name=input("Enter the Student Name:")
        dictio[student_id]=student_name
        print("Student Detail Entered Successfully!")
    elif choice==2:
        if len(dictio)==0:
            print("Dictionary is empty!")
        else:
            for ele in dictio:
                print(ele,":",dictio[ele])
    elif choice==3:
        query=input("Enter the Student ID:")
        if query not in dictio:
            print("Entered Student ID does not exist...")
        else:
            print(query,":",dictio[query])
    elif choice==4:
        exit()
    else:
        print("Please Enter the valid option...")
