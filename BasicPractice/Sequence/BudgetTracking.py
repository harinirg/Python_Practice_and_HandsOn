income=float(input("Enter your monthly income: "))
expense=input("Enter your expenses (space-separated): ")
expense_list=expense.split()
total=0
for i in expense_list:
    total += float(i)
remain=income-total
print("Remaining budget:{:.2f}".format(remain))




