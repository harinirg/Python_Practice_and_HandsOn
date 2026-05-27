#append,insert,extent,delete pos,delete value,modify,ascending sort, descending sort,dispaly
# Menu Driven List Operations

listA = []
while True:
    print("1. Append an element")
    print("2. Insert an element")
    print("3. Append a list to given list")
    print("4. Modify")
    print("5. Delete by Position")
    print("6. Delete by Value")
    print("7. Ascending Sort")
    print("8. Descending Sort")
    print("9. Display")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    # Append
    if choice == 1:
        value = input("Enter element to append: ")
        listA.append(value)
        print("The element is appended")
    #Insert
    elif choice==2:
        pos=int(input("Enter the position:"))
        value=input("Enter the element to ibe inserted: ")
        listA.insert(pos,value)
        print("The element is inserted")
    #Append a List with other List
    elif choice == 3:
        newList = input("Enter list elements separated by space: ").split()
        listA.extend(newList)       
        print("Another list appended")
    #Modify
    elif choice==4:
        pos=int(input("Enter the position to modify:"))
        value=input("Enter the value:")
        listA[pos]=value

    #Delete by position
    elif choice==5:
        pos=int(input("Enter the position to delete:"))
        listA.pop(pos)
        print("Element deleted")    
    # Delete by Value
    elif choice == 6:
        value = input("Enter value to delete: ")
        listA.remove(value)
        print("Value deleted")
    # Ascending Sort
    elif choice == 7:
        listA.sort()
    # Descending Sort
    elif choice == 8:
        listA.sort(reverse=True)
    # Display List
    elif choice == 9:
        print("List Elements:", listA)
    # Exit
    elif choice == 10:
        break
    else:
        print("Invalid Choice")    
