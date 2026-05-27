String=input("Enter the String:")
total_alpha=0
total_num=0
for s in String:
    if s.isnumeric():
        total_num+=1
    elif s.isalpha():
        total_alpha+=1
    else:
        pass
print("Total alpha:",total_alpha)
print("Total numeric:",total_num)