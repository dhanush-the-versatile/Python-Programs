'''python program to demonstrate arithametic operator,relational operators,
assignment operators,logical operators, bitwise operators,membership and identity operators'''
a=int(input("enter value of 'a' : "))
b=int(input("enter value of 'b' : "))
print("arithametic operators")
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)
print("Relational operators")
print(a==b,a>b,a<b,a!=b,a>=b,a<=b)
print("assignment operators")
a=b
a+=b
a-=b
a*=b
a/=b
a//=b
a%=b
a**=b
print(a)
print(b)
print("Logical Operators")
print(69>143 and 47<69)
print("Bitwise operators")
print(b<<5)
print(b>>5)
print("Membership operators")
print("x" in "xyz")
print("x" not in "xyz")
print("Identity Operators")
c=255
d=255
print(c is d)
