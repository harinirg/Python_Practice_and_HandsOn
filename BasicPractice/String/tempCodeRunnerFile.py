# Program to print lowercase letters first and uppercase letters next
string = input("Enter the string: ")
lower = ""
upper = ""
for ch in string:
    if ch.islower():
        lower = lower + ch
    else:
        upper = upper + ch
result = lower + upper
print(result)