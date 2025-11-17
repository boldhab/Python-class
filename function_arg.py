def sum_num(x,y):
    return x+y
def area_circle(r):
    PI=3.14
    a=PI*r*r
    return a
print(area_circle(4))

def allnum  (num1,*args):
    sum=0
    for x in args:
        sum=x+sum
    return sum 
print(allnum(9,8,6,4,3,5))