def prime_number(start,end):
    for num in range(start,end):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
start=int(input("Enter the start number"))
end=int(input("Enter the end number"))
prime_number(start,end)