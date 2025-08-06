#Write a Python program to compute distance between two points in a 2- dimensional Coordinate system.
x1=int(input("Enter 'x1' Co-ordinate Value: "))
x2=int(input("Enter 'x2' Co-ordinate Value: "))
y1=int(input("Enter 'y1' Co-ordinate Value: "))
y2=int(input("Enter 'y2' Co-ordinate Value: "))
d=(((x2-x1)**2)+((y2-y1)**2))**0.5
print("The Distance is ",d)
