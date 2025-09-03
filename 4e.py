for i in range(1,6):
    for j in range(1,5):
        if((j==1 or j==4)  and i!=1)or ((i==1 or i==3) and (j>1 and j<4)):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
