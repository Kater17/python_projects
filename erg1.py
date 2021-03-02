import math
import random as r

def findRows(sq,dim):
    sum = 0
    for row in sq:
        for i in range(dim-3):
            if row[i] == 1 and row[i+1] == 1 and row[i+2] == 1 and row[i+3] == 1:
                sum += 1
    return sum

def findCols(sq,dim):
    sum = 0
    for col in range(dim):
        for row in range(dim-3):
            if sq[row][col] == 1 and sq[row+1][col] == 1 and sq[row+2][col] == 1 and sq[row+3][col] == 1:
                sum += 1
    return sum

def findDiagons(sq,dim):
    sum = 0
    
    cols = [[] for i in range(dim)]
    rows = [[] for i in range(dim)]
    diag1 = [[] for i in range(dim + dim - 1)]
    diag2 = [[] for i in range(len(diag1))]
    minD = -dim + 1
    
    for x in range(dim):
        for y in range(dim):
            cols[x].append(sq[y][x])
            rows[y].append(sq[y][x])
            diag1[x+y].append(sq[y][x])
            diag2[x-y-minD].append(sq[y][x])
    
    for diagon in diag1:
        if len(diagon) >= 4:
            for l in range(len(diagon)-3):
                if diagon[l] == 1 and diagon[l+1] == 1 and diagon[l+2] == 1 and diagon[l+3] == 1:
                    sum += 1
    
    for diagon in diag2:
        if len(diagon) >= 4:
            for l in range(len(diagon)-3):
                if diagon[l] == 1 and diagon[l+1] == 1 and diagon[l+2] == 1 and diagon[l+3] == 1:
                    sum += 1
    
    return sum

def CreateSquareAndDoTheMath(dim,totSum):
    square = [[0 for x in range(dimension)] for y in range(dimension)]
    total_aces = math.ceil(pow(dimension,2) / 2)

    for i in range(total_aces):
        while(True):
            x = r.randint(0,dimension-1)
            y = r.randint(0,dimension-1)
            if square[x][y] != 1:
                square[x][y] = 1
                break
                
    return findRows(square,dimension) + findCols(square,dimension) + findDiagons(square,dimension)

dimension = int(input("Enter the dimension of the square: "))
while dimension <= 0:
    print("The dimension is not valid. Please enter a positive number")
    dimension = int(input("Enter the dimension of the square: "))

total_sum = 0

for i in range(100):
    total_sum += CreateSquareAndDoTheMath(dimension,total_sum)

print(total_sum/100)