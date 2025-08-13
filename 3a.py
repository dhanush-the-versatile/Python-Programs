# program to calculate GCD of two numbers
a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
if a>b:
    n=b
else : n=a
for i in range(n,0,-1):
    if a%i==0 and b%i==0:
        print("The GCD is",i)
        break
