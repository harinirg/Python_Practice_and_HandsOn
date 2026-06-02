def sum_odd_even(start,end):
    even=0
    odd=0
    for num in range(start,end):
        if(num%2==0):
            even+=num
        else:
            odd+=num
    absolute=abs(even-odd)
    print(f"The sum of odd numbers from {start} to {end} is: {odd}")
    print(f"The sum of even numbers from {start} to {end} is : {even}")
    print(f"The absolute difference between the two sums is:{absolute}")
start=int(input("Enter the start/:"))
end=int(input("Enter end value:"))
sum_odd_even(start,end)