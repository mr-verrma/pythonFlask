# myList=["Mac","Windows",'XP','Window 7','Linux']


# for i in myList:
#     print(i,end=' ')

#Calculate Factorial N! as a input

user_input=int(input())

def fac(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

print(fac(user_input))