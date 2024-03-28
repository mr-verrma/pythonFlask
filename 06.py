class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def printName(self):
        print(self.fname,self.lname)
class Student(Person):
    # def __init__(self,fname,lname):
    #     super().__init__(fname,lname)
    pass
# obj=Person("Amit","Kumar")
obj=Student("Amit2","Kumar")
obj.printName()