#Python Program to display all prime numbers within an interval
a = int(input("Enter Range lower limit: "))
b = int(input("Enter Range Upper limit: "))
for n in range(a, b+1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n,end=' ')
