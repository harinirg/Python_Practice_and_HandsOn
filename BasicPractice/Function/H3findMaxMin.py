def findMax(*numbers):
    max = numbers[0]

    for i in numbers:
        if max < i:
            max = i

    return max
def findMin(*numbers):
    min = numbers[0]

    for i in numbers:
        if min > i:
            min = i

    return min
numbers = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Maximum:", findMax(*numbers))
print("Minimum:", findMin(*numbers))