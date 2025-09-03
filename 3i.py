#program to check whether given number N is N-Series(Disarium) number or not
num = input("Enter a number: ")
n = int(num)
sum = 0
for i in range(len(num)):
    digit = int(num[i])
    sum = sum+digit ** (i + 1)
if sum == n:
    print("Disarium number")
else:
    print("Not a Disarium Number")
