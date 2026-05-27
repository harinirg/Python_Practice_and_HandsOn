N=int(input("enter the number"))
i=1
sum=0
while i<N:
    num=int(input("enter the number"))
    if num==-1:
        break
    else:
        sum+=num
    i=i+1
print("The sum of user input is:",sum)