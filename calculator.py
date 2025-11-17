def addition(a, b):
    z=a + b
    return z 

def subtraction(a, b):
    z=a - b
    return z

def division(a, b):
        z=a / b
        return z
    

def multiplication(a, b):
        z=a * b
        return z

a = int(input("First number: "))
b = int(input("Second number: "))

x = addition(a, b)
y = subtraction(a, b)
z = division(a, b)
r = multiplication(a, b)

print(f"The sum is: {x}")
print(f"The difference is: {y}")
print(f"The quotient is: {z}")
print(f"The product is: {r}")
  
print("Error: Please enter valid integers.")
