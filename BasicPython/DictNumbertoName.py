def number_name(Input):
    rev = 0
    while Input != 0:
        rev = (rev * 10) + (Input % 10)
        Input = int(Input / 10)
    d = {0: 'zero',1: 'one',2: 'two',3: 'three',4: 'four',5: 'five',6: 'six',7: 'seven',8: 'eight',9: 'nine'}
    while rev != 0:
        rem = rev % 10
        print(d.get(rem), end=" ")
        rev = int(rev / 10)
Input = int(input("Enter the number: "))
number_name(Input)