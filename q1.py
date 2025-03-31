import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))


def triangle_area(a, b, c):
   
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2  # Semi-perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
        return area
    else:
        return "Invalid triangle sides"


result = triangle_area(a, b, c)
print(f"Area of the triangle: {result}")
