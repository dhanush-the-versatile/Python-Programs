# Python script to take input as list L and print largest number L and total combinations C
import itertools as it
L = eval(input("Enter list of digits (e.g., [1,2,1,4]): "))
N = int(input("Enter number of digits N: "))
P = list(it.permutations(L, N))
print(P)
x = []
for i in P:
    m = 0
    for j in i:
        m = m * 10 + j
    x.append(m)
print(x)
print("The Largest number L:", max(x))
print("Total combinations C:", len(x))
