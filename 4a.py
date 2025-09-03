#Python program to add two 3x3 matrices using nested loops.
matrix1= [ 
    [1, 2, 7],
    [6, 9, 4],
    [3, 8, 0]
    ]
matrix2=[
    [7,8,1],
    [5,9,1],
    [4,7,4]
    ]
matrix3=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
for i in range(0,3):
    for j in range(0,3):
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
        print(matrix3[i][j],end='  ')
    print()   
