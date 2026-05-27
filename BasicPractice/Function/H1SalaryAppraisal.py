def salary_calculation(salary,appraisal):
    if(appraisal>=1 and appraisal<=4):
        total=salary*0.10
    elif(appraisal>=4.1 and appraisal<=7):
        total=salary*0.25
    elif(appraisal>=7.1 and appraisal<=10):
        total=salary*0.30
    else:
        print ("Invalid Input")
    return total
salary=int(input("Enter the Salary:"))
appraisal=float(input("Enter the appraisal rating:"))
result=salary+salary_calculation(salary,appraisal)
print(int(result))
