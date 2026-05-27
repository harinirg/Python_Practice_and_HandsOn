q = input("Enter quantities: ").split(",")
p = input("Enter prices: ").split(",")

total = 0

for i in range(len(q)):
    total = total + int(q[i]) * float(p[i])

print("Total value of the inventory:", total)