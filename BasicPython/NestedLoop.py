L=int(input("Enter the Lower: "))
U=int(input("Enter the Upper: "))
print("The Prime number btw Lower and Upper are :")
for num in range(L,U+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)
             