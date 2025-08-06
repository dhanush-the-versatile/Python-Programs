'''Python script to print whether the roots are equal, distinct or complex
for given coefficients a, b and c for quadratic equation'''
b=int(input("Enter coefficient of 'x' : "))
a=int(input("Enter coefficient of 'x^2' : "))
c=int(input("Enter the constant value: "))
if b**2-4*a*c>0:
    print("Roots are Real and distinct")
elif b**2-4*a*c<0:
    print("Roots are Complex")
else : print("Roots are Equal")
