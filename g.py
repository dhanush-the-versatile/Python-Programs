#Write a program to swap two numbers without using a temporary variable.
a=int(input("Enter the value of 'a' : "))
b=int(input("Enter the value of 'b' : "))
a=a+b
b=a-b
a=a-b
print("The Value of 'a' is : ",a)
print("The Value of 'b' is : ",b)
