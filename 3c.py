#Python program to print the first N Fibonacci numbers
n=int(input("Enter a Number"))
a=0
b=1
print(a,b,end=' ')
i=1
while(i<=n):
    c=a+b
    print(c,end=' ')
    a,b=b,c
    i+=1
