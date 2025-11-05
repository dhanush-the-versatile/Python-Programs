students = []

def addStudent(name):
    if name not in students:
        students.append(name)
        print(name, "added.")
    else:
        print(name, "already exists.")

def removeStudent(name):
    if name in students:
        students.remove(name)
        print(name, "removed.")
    else:
        print(name, "not found.")

def searchStudent(name):
    if name in students:
        print(name, "found.")
    else:
        print(name, "not found.")
