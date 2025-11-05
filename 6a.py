# Python script to take input as number N, and find out the largest digit L
import itertools as it
N=(list(it.permutations([6,7,9],3)))
print(N)
x=[]
for i in N:
    m=0
    for j in i:
        m=m*10+j
    x.append(m)
print(x)
print("The Largest number L:", max(x))
