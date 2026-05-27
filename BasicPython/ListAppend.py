listA=[]
n=int(input("Enter the number of element"))
for i in range(0,n):
    print("Enter the element No-{}".format(i+1))
    elm=int(input())
    listA.append(elm)
print("The entered list is :\n",listA)