
import ctypes
# to create C type ka array

class DynamicList:
    def __init__(self):
        self.n=0
        self.size=1
        #create a c type array with size=self.size
        self.List=self.__make__array(self.size)
    
    def __make__array(self,size):
        #creates a C type array(static,referential) with size (capacity).
        return (size * ctypes.py_object)()
    
    #create length function
    def __len__(self):
        return self.n
    def append(self,item):
        if self.n==self.size:
            #resize
            self.__resize(self.size*2)
        self.List[self.n]=item
        self.n=self.n+1
    def __resize(self,newsize):
        #create a new array with new size
        List2=self.__make__array(newsize)
        self.size=newsize

        #now copy the content of List to list2
        for i in range(self.n):
            List2[i]=self.List[i]
        #Assign TO List
        self.List=List2

    def __str__(self):
        result='' 
        for i in range(self.n):
            result=result + str(self.List[i])+','
        return result
L=DynamicList()
# print(type(L))
L.append('abc')
L.append('abc2')
L.append(True)

print(L)