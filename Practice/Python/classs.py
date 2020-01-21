class Student:

    def setname(self,name):
        self.name=name

    def setcoll(self,coll):
        self.coll=coll

    def getname(self):
        return self.name
    
    def getcoll(self):
        return self.coll


stud1=Student()
stud1.setname("Mahesh")
stud1.setcoll("AIET")

stud2=Student()
stud2.setname("Prashil")
stud2.setcoll("MITE")

print("Student 1 Details:\nName: ",stud1.getname(),"\nCollege: ",stud1.getcoll())