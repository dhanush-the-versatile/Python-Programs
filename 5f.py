#program to take input as vehicle Number N and check whether N is Fancy number or not.
N=(input("Enter Vehicle Number: "))
if len(N)==4:
    def fancy_number():
        for i in range(0, 4):
            if N[i] == N[i+1] == N[i+2] == N[i+3]:
                return True
            return False
else: print("Invalid Vehicle number!")

if fancy_number():
    print(N,"is a Fancy Number!")
else:
    print(N," is not a Fancy Number.")
