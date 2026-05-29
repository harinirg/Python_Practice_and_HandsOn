#try_except_else
try:
    a=int(input("Enter the number"))
    b=int(input("Enter the b:"))
    c=a/b
    print(c)
except Exception:
    print("Cant be divide by Zero")
    print(Exception)
else:
    print("I will execute when no exception occurs")

#######################################################

#try_except_else_finally
try:
    a=int(input("Enter the number"))
    b=int(input("Enter the b:"))
    c=a/b
    print(c)
except Exception:
    print("Cant be divide by Zero")
    print(Exception)
else:
    print("I will execute when no exception occurs")
finally:
    print("I am excecuting")

#################################################3

# file_try_finally
try:
    fh=open("test.txt","w")
    try:
        fh.write("This line is about Exception Handling")
    finally:
        print("Going to close file")
        fh.close()
except IOError:
    print("Error:Can't find the file")
else:
    print("I will execute when no ex exception occurs")
finally:
    print("I am executing")

###################################################################

#File not found try_exception_else_finally
try:
    fh=open("invalid/test.txt","w")
    try:
        fh.write("This line is about Exception Handling")
    finally:
        print("Going to close file")
        fh.close()
except IOError:
    print("Error:Can't find the file")
else:
    print("I will execute when no ex exception occurs")
finally:
    print("I am executing")

####################################################################3

#Raising_Keyword

try:
    num=int(input("Enter a positive integer"))
    if(num<0):
        raise ValueError("This is negative number")
except ValueError as e:
    print(e)
print("I am Successfully handled")


