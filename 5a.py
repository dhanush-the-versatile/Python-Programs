#program to define a function with multiple return values
def f1(a,b):
    x=a+b
    y=a-b
    z=a*b
    return x,y,z
print(f1(10,20))
