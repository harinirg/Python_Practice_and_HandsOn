String=input("Enter the String")
c=0
for i in String:
    c+=1
print(c)
for i in range(2):
    print(String, end="")
print()
for i in range(1):
    print(String[i])
for i in range(3):
    print(String[i], end="")

