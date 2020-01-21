import sqlite3 as db

connect=db.connect("PY_Assignment_Prashil_Alva")
cursor=connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Student_Details ( Reg_no INT,Student_Name VARCHAR(50),Branch VARCHAR(4),Batch INT, SEM1_marks INT,PRIMARY KEY (Reg_no) )")
while(True):
    ch=input("1.Enter Student Details\n2.Add 5 Marks as Grace\n3.Delete the Student Who has Scored least marks\n4.Display all Student Details\n5.Exit\n")
    if ch=="1":
        print("Enter the 5 Student Details...")
        for i in range(0,5):
            inputt=input("Enter the Register no, Name, Branch, Batch, Total marks scored in SEM-1\n")
            data=inputt.split(" ")
            cursor.execute("INSERT INTO Student_Details(Reg_no,Student_Name,Branch,Batch,SEM1_marks) VALUES (?,?,?,?,?)",(int(data[0]),data[1],data[2],int(data[3]),int(data[4])))
            connect.commit()
    
    elif ch=="2":
        cursor.execute("UPDATE Student_Details SET SEM1_marks=SEM1_marks+5")
        connect.commit()
        print("Grace Marks added Successfully....")
    
    elif ch=="3":
        cursor.execute("DELETE FROM Student_Details WHERE SEM1_marks=(SELECT MIN(SEM1_marks) FROM Student_Details)")
        connect.commit()
        print("Student with least marks deleted successfully...")

    elif ch=="4":
        dataa=cursor.execute("SELECT * FROM Student_Details")
        row=dataa.fetchall()
        if len(row)==0:
            print("No record exists...")
        else:
            print("Student Details are....")
            for ele in row:
                print("-------------------------------------------------------------------------------")
                print("Reg. No:{0}\nName:{1}\nBranch:{2}\nBatch:{3}\nTotal marks scored in SEM_1:{4}".format(ele[0],ele[1],ele[2],ele[3],ele[4]))
                print("-------------------------------------------------------------------------------")

    elif ch=="5":
        exit()

    else:
        print("Invalid Choice...")

