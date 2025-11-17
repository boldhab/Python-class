def even_odd(num):
    if num%2==0:
        x="even"
        return  x
    else:
        x="odd "
        return x

even=int(input("Enter the number "))
number=even_odd(even)
print(f"The number is {even}: {number}")