# Write a program to print the reverse of number.
num = int(input("Enter a Number: "))
a = 0
b = 0
c = 0
while (num > 0):
    a = num % 10
    b = b * 10 + a  
    num = num // 10
print("The Reversed Number is", b)
