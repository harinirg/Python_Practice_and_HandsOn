# Count lower case, upper case and non-letters
string = input("Enter the string: ")
lower = 0
upper = 0
non_letter = 0
for ch in string:  
    if ch.islower():
        lower += 1       
    elif ch.isupper():
        upper += 1       
    else:
        non_letter += 1
print("Lower case letters", lower)
print("Upper case letters", upper)
print("Non - letters:", non_letter)