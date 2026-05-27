Greet='Welcome'
index=0
length=len(Greet)
while index<length:
    letter=Greet[index]
    print(letter)
    index+=1
Greet='Morning'
for i in Greet:
    print(i)
#first number is greater than 2nd number means returns the empty string
str="Hello"
print(str[3:3])
str_1="Good day"
print(str_1[-3:-1])
str2="HELLO"
print(str2[4:0:-2])
print(str2[0:4:-2])
print(str_1[::-2])
str1='hello'
str2='guys'
print(str1+str2)
print(str1*3)
txt="He is smart guy"
if "work" in txt:
    print("Yes, it is present")
else:
    print("No, it is not present")
#Edit/Modify
Greeting='Hello, world'
new_greet='j'+Greeting[1:]
print(new_greet)

Greeting='Hello, world!'
new_greet='j'+Greeting[-6:-1]
print(new_greet)

