def max_two(a, b):
    if a > b:
        return a
    else:
        return b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
maximum = max_two(num1, num2)
print(f"The maximum of {num1} and {num2} is: {maximum}")


