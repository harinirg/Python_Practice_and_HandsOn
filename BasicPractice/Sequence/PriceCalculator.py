price = int(input("Enter the price of the first item: "))
qty = int(input("Enter the quantity of the first item: "))
total = 0
total = total + (price * qty)
choice = input("Do you want to enter another item? (yes/no): ")
while choice == "yes":
    price = int(input("Enter the price of the next item: "))
    qty = int(input("Enter the quantity of the next item: "))  
    total = total + (price * qty) 
    choice = input("Do you want to enter another item? (yes/no): ")
print("Total Price:", total)