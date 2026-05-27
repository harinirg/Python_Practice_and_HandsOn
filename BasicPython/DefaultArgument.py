#Default paramater should be at last
def add(num1,num2,num3=4):
    out=(num1+num2)*num3
    return out
v1=int(input("Enter the 1st integer"))
v2=int(input("Enter the 2nd integer"))
result=add(v1,v2)
print("The result:",result)
