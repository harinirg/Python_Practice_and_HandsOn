# Sum ofodd & even numbers
def sum_even_odd(num):
    sum_even=0
    sum_odd=0
    for i in range(num+1):
        if(i%2==0):
            sum_even+=i
        elif(i%2!=0):
            sum_odd+=i
    print("Sum of even:",sum_even)
    print("Sum of odd:",sum_odd)
n=int(input("Enter the number:"))
sum_even_odd(n)

 