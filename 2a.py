#Python Program to find largest among 3 numbers
a=int(input("enter value of 'a' : "))
b=int(input("enter value of 'b' : "))
c=int(input("enter value of 'c' : "))
if a>b and a>c:
   print("a is largest")
elif b>c:
    print("b is largest")
else: print("c is largest")
