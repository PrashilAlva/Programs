class Person:
    id = ""
    name = ""
    address = ""

    def displaydetails(self):
        print("ID:", self.id, "\nName:", self.name, "\nAddress:", self.address)

class Student(Person):
    course = ""
    fees = ""

    def displaydetails(self):
        print("ID:", self.id, "\nName:", self.name, "\nAddress:",
              self.address, "\nCourse", self.course, "\nFees:", self.fees)

class Staff(Person):
    year_of_joining = ""
    salary = ""

    def displaydetails(self):
        print("ID:", self.id, "\nName:", self.name, "\nAddress:", self.address,
              "\nYear of Joining", self.year_of_joining, "\nSalary:", self.salary)


print("Enter the Two Student and Three Staff Details")
obj = list()
for i in range(0, 2):
    print("Enter the Student ", i+1, " Details")
    inputt = input(
        "Enter the ID, Name, Address, Course and Fees for Student (Space separated input)\n")
    Stud = Student()
    Stud.id, Stud.name, Stud.address, Stud.course, Stud.fees = inputt.split()
    obj.append(Stud)

for i in range(0, 3):
    print("Enter the Staff ", i+1, " Details")
    inputt = input(
        "Enter the ID, Name, Address, Year of Joining and Salary for Student (Space separated input)\n")
    Staf = Staff()
    Staf.id, Staf.name, Staf.address, Staf.year_of_joining, Staf.salary = inputt.split()
    obj.append(Staf)

print("Details are...")

for ele in obj:
    print("-------------------------------------------------------------------------------------------")
    ele.displaydetails()
    print("-------------------------------------------------------------------------------------------")