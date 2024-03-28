class MyClass:
    x=12
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} ({self.age})"
    def myFun(self):
        print("Hello", self.name)
    

obj=MyClass("Amit",24)
# print(obj.myFun())
obj.myFun()