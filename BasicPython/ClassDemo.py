class Myclass:

    def display():
        print("welcome")

    def display1(self):
        print("Hello")

    def display2(self, name):
        print("Welcome", name)
#Object
obj = Myclass()
obj1 = Myclass()
print(obj)
print(obj1)
#Method
obj.display()
obj.display1()
obj.display2("Harini")
#################
#Create property
class My_Class():
    x=5
    def display(self):
        print("I am inside the function")
obj=My_Class()
print('State:',obj.x)
print('Behaviour:')
obj.display()