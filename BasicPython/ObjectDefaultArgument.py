class Circle:
    def __init__(self, radius=1.0, color='red'):
        self.radius = radius
        self.color = color
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def setRadius(self, radius):
        self.radius=radius
    def setColor(self, color):
        self.color = color
    def getArea(self):
        return 3.14159*self.radius*self.radius
    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"   
circle1 = Circle()
print(circle1)
circle2 = Circle(2.5)
print(circle2)
circle3 = Circle(3.5, 'Blue')
print(circle3)
#######################################
class Circle:
    def __init__(self, radius=1.0, color='red'):
        self.radius = radius
        self.color = color
    @classmethod
    def withRadius(cls, radius):
        return cls(radius)
    def withRadiusandColor(cls, radius, color):
        return cls(radius, color)
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def getArea(self):
        return 3.14159*self.radius*self.radius
    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"
circle1 = Circle()
print(circle1)
circle2 = Circle(2.5)
print(circle2)
circle3 = Circle(3.5, 'Blue')
print(circle3)
############################################
class circle:
    def __init__(self,*args):
        if len(args)==0:
            self.radius = 1.0
            self.color = "red"
        elif len(args)==1:
            self.radius = args[0]
            self.color = "red"  
        elif len(args)==2:
            self.radius = args[0]
            self.color = args[1]   
        else:
            raise ValueError("Too many arguments")
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def setRadius(self,radius):
        self.radius = radius
    def setColor(self,color):
        self.color=color
    def getArea(self):
        return 3.14*self.radius*self.radius
    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"


circle1 = circle()
print(circle1)
circle2 = circle(2.5)
print(circle2)
circle3 = circle(3.5,"blue")
print(circle3)

