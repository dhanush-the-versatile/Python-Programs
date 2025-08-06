#python script to read the person age from user and display Person status
age=int(input("Enter Age of a person"))
if age>60:
    print("Senior Citizen")
elif 25<=age<=59:
    print("working citizen")
elif 16<=age<=24:
    print("College Students")
elif 4<=age<=15:
    print("School kids")
elif 1<=age<=3:
    print("Play kid")
else: print("Invalid")
