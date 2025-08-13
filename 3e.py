#Python program using while loop to print first N numbers divisible by 5
n=int(input("Enter a Number: "))
i=1
while(i<=n):
    if i%5==0:
        print(i,end=' ')
    i+=1
