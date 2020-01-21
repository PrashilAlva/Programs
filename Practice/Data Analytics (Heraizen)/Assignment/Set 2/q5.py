class LowbalanceException(Exception):
    pass

class Employee():
    def __init__(self,eid,ename,desig,bas_pay):
        self.empId=eid
        self.empName=ename
        self.designation=desig
        self.basic_pay=bas_pay
        self.hra=self.calculatehra()
        self.verify()

    def printdetails(self):
        print("Employee ID:",self.empId,"\nEmployee Name:",self.empName,"\nDesignation:",self.designation,"\nBasic Pay:",self.basic_pay,"\nHRA:",self.hra)

    def verify(self):
        try:
            if self.basic_pay<500:
                raise LowbalanceException
            else:
                print("Details You have Entered are...")
                self.printdetails()

        except LowbalanceException:
            print("Sorry, Your Balance is Too low!")

    def calculatehra(self):
        if self.designation=="Manager":
            hra=(self.basic_pay//100)*10
        elif self.designation=="Officer":
            hra=(self.basic_pay//100)*12
        else:
            hra=(self.basic_pay//100)*5
        return hra

obj=list()

while(True):
    ch=input("1.Add Employee\n2.View Employees\n3.Exit\n")
    if ch=="1":
        data=list()
        inputt=input("Enter the Employee ID, Employee Name, Designation, Basic Pay for Employee (Space Separated Input)\n")
        data=inputt.split()
        e1=Employee(data[0],data[1],data[2],int(data[3]))
        obj.append(e1)
    elif ch=="2":
        if len(obj)==0:
            print("No Records found!")
        else:
            print("Details are...")
            for ele in obj:
                print("--------------------------------------------------------------------------")
                ele.printdetails()
                print("--------------------------------------------------------------------------")
    elif ch=="3":
        exit()
    else:
        print("Invalid choice....")

    

