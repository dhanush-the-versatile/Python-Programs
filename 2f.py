#Python program to find the factorial of a given number
n=int(input("Enter the number for finding Factorial: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is",fact)
