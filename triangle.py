def triangle(h, w):
     area=0.5 * h * w
     return area 

height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area = triangle(height, base)
print(f"The area of the triangle is: {area}")


