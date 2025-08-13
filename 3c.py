#Python program to print the first N Fibonacci numbers
n=int(input("Enter a Number"))
a=0
b=1
i=1
while(i<=n):
    c=a+b
    print(c)
    a,b=b,c
    i+=1
