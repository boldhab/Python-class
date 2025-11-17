def add(x,y):
    z=x+y
    return z
def subract(x,y):
    z=x-y
    return z
def multiply(x,y):
    z=x*y
    return z
def divided(x,y):
    z=x/y
    return z

x=int(input("enter the number of x "))
y=int(input("enter the number of y "))


print(f"sum {x}and{y}{add(x,y)}")
print(f"sumtract {x} and {y}(x,y):{subract(x,y)}")
print(f"multiply {x} and {y}(x,y):{multiply(x,y)}")
print(f"division {x} and {y}(x,y):{divided(x,y)}")