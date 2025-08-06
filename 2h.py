#python script to take five subject marks and print the grade for the student.
marks1=int(input("Enter the Marks of subject 1:"))
marks2=int(input("Enter the Marks of subject 2:"))
marks3=int(input("Enter the Marks of subject 3:"))
marks4=int(input("Enter the Marks of subject 4:"))
marks5=int(input("Enter the Marks of subject 5:"))
total=(marks1+marks2+marks3+marks4+marks5)/5
if 100<=total>=90 :
    print("S Grade for",total,"Percenatge")
elif 89<=total>=80 :
    print("A Grade for",total,"Percenatge")
elif 79<=total>=70:
    print("B Grade for",total,"Percenatge")
elif 69<=total>=60:
    print("C Grade for",total,"Percenatge")
elif 59<=total>=50:
    print("D Grade for",total,"Percenatge")
elif 49<=total>=35:
    print("E Grade for",total,"Percenatge")
else: print("You are failed")
