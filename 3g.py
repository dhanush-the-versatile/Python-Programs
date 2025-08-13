'''program to take input as integer N and check whether N is Pronic Number or not'''
n = int(input("Enter Integer: "))
i = 1
while i * (i + 1) <= n:
    if i * (i + 1) == n:
        print("The given integer is a pronic number")
        break
    i += 1
else:
    print("The given integer is not a pronic number")
