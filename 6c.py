# Python script to print prime pairs within a given range

N = int(input("Enter the range (N): "))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Prime pairs are:")
for i in range(2, N):
    if is_prime(i) and is_prime(i + 2):
        print(f"({i}, {i + 2})")
