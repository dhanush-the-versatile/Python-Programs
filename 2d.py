#Python Program to display all prime numbers within an interval
num = int(input("Enter a Number: "))
for n in range(2, num):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)
