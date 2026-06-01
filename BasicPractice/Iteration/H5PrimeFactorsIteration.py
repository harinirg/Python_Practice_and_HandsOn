num = int(input("Enter the element"))
factor = 2
while num > 1:
    while num % factor == 0:
        print(factor, end=" ")
        num = num // factor
    factor = factor + 1
print()