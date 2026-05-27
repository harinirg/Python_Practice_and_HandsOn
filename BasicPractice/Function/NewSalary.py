#Find new Salary with help of salary hike
def new_salary(old_salary,hike):
    salary=old_salary + (old_salary *hike/100) 
    return salary
old=int(input("Enter the oldSalary:"))
hike=int(input("Enter the hike:"))
newSalary=new_salary(old,hike)
print(float(newSalary))