'''Python program to create a person class. Include attributes like name,
country and date of birth. Implement a method to determine the person's age.'''
from datetime import datetime
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    def age(self):
        birth_date = datetime.strptime(self.dob, "%d-%m-%Y")
        today = datetime.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
p = Person("John Doe", "Australia", "01-01-2000")
print("Name:", p.name)
print("Country:", p.country)
print("Age:", p.age())
print("Date of birth:",p.dob)
