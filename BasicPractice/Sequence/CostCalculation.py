price=float(input("Enter the price of the item:"))
quantity=int(input("Enter the quantity"))
cost=price*quantity
print("Total cost: ${:.2f}".format(cost))