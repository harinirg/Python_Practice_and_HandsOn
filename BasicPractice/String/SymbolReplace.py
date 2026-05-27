# Replace special symbols with #
str1 = input("Enter the string: ")
result = ""
for ch in str1:
    if ch.isalnum() or ch.isspace():
        result += ch
    else:
        result += "#"
print(result)