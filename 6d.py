# Sum of even Fibonacci numbers whose values do not exceed 4 million
limit = 4000000
a, b = 1, 2
sum_even = 0
while a <= limit:
    if a % 2 == 0:
        sum_even += a
    a, b = b, a + b
print("Sum of even Fibonacci numbers:", sum_even)
