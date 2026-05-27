import math
radius=float(input("Enter the radius of the circle: "))
angle=float(input("Enter the angle in degrees (for sector area): "))
print(f"Radius:{radius}")
diameter=2*radius
area=math.pi*radius*radius
print(f"Diameter: {diameter}")
circumference=2*math.pi*radius
print(f"Circumference: {circumference}")
sectorArea=(angle/360)*area
arcLength=(angle/360)*circumference
print(f"Srector Area for {angle} degrees:{sectorArea}")
print(f"Arc Length for {angle} degrees: {arcLength}")