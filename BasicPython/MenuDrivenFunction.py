#CircleArea Definition
def circle(radius):
    print("The area of Circle:",3.14*radius*radius)
#SquareAreaDefinition
def square(side):
    print("The area of Square:",side*side)
#RectangleAreaDefinition
def rectangle(length,breadth):
    print("The area of rectangle:",length*breadth)
while True:
    print("Menu Driven ")
    print("1.Circle Area")
    print("2.Square Area")
    print("3.Rectangle Area")
    print("4.Exit")
    choice=int(input("Enter the choice"))
    if(choice==1):
        radius=int(input("Enter the radius"))
        circle(radius)
    elif(choice==2):
        side=int(input("Enter the side"))
        square(side)
    elif(choice==3):
        length=int(input("Enter the length"))
        breadth=int(input("Enter the breadth"))
        rectangle(length,breadth)
    elif(choice==4):
        break
    else:
        print("Wrong choice")