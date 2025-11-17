#Write a function that takes an integer minute and converts it to seconds.
def convert(minute):
    second=minute*60
    return second
min=int(input("enter the mnute"))
time=convert(min)
print(f"the change of {min} in to second is {time}")