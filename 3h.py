'''python script to take input as amount in rupees R and find out the least
number of notes N that can be possible to store in a Wallet.'''
amount=int(input("Enter the amount"))
notes=0
denominations=[2000,500,200,100,50,20,10]
for note in denominations:
    count=amount//note
    notes+=count
    amount=amount%note
print("Minimum number of notes required:",notes)
