n = int(input("Enter a number : "))
odd = 0
even = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print("Even sum :", even)
print("Odd sum :", odd)