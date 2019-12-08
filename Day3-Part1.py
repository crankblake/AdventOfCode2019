import numpy as np
import scipy.spatial.distance as mdist
file = open(".\\Inputs\\inputDay3TEST.txt", "r")
wire1 = file.readlines(1)
wire2 = file.readlines(2)
wire1Array = wire1[0].split(',')
wire2Array = wire2[0].split(',')
array = np.empty([10,10], dtype=object)
array = np.empty([10000,10000], dtype=object)
array.fill('__')
column = 0
row = 9
centralPort = [(row,column)]
array[centralPort] = 'CP' 
#np.set_printoptions(threshold=np.sys.maxsize)
pointer = centralPort
for index, command in enumerate(wire1Array):
    print("index is", index)
    print("command is", command)
    dir = command[0]
    dist = int(command[1])
    print(dir)
    if dir == 'R':
        for i in range (0, dist):
            #print("dist is", dist)
            #print("i is", i)
            array[row, column + 1] = 'R1'
            #print("row, column", row,column)
            column += 1
            #print(column,row)
            #print(array)
    if dir == 'U':
        for i in range (0, dist):
            #print("dist is", dist)
            #print("i is", i)
            array[row - 1, column] = 'U1'
            #print("row, column", row, column)
            row -= 1
            #print(column,row)
            #print(array)
    if dir == 'L':        
        for i in range (0, dist):
            array[row, column - 1] = 'L1'
            column -= 1
    if dir == 'D':
        for i in range (0, dist):
            array[row + 1, column] = 'D1'
            row += 1 
column = 0
row = 9            
for index, command in enumerate(wire2Array):
    print("index is", index)
    print("command is", command)
    dir = command[0]
    dist = int(command[1])
    print(dir)
    if dir == 'R':
        for i in range (0, dist):
            if array[row, column + 1] == 'U1' or array[row, column + 1] == 'D1':
                array[row, column + 1] = 'XX'
            else:
                array[row, column + 1] = 'R2'
            column += 1
    if dir == 'U':
        for i in range (0, dist):
            if array[row - 1, column] == 'L1' or array[row - 1, column] == 'R1':
                array[row - 1, column] = 'XX'
            else:
                array[row - 1, column] = 'U2'
            row -= 1
    if dir == 'L':        
        for i in range (0, dist):
            if array[row, column - 1] == 'U1' or array[row, column - 1] == 'D1':
                array[row, column - 1] = 'XX'
            else:
                array[row, column - 1] = 'L2'
            column -= 1
    if dir == 'D':
        for i in range (0, dist):
            if array[row + 1, column] == 'L1' or  array[row + 1, column] == 'R1':
                array[row + 1, column] = 'XX'
            else:
                array[row + 1, column] = 'D2'
            row += 1               
print(array)

arrayCross = []
for i, row in enumerate(array):
    for j, value in enumerate(row):
        #print("row and value index", i, j)
        #print("row and value", row, value)
        if value == 'XX':
            arrayCross.append((i,j))
print(arrayCross)
#import scipy.spatial.distance 
#print(mdist.cityblock(centralPort, arrayCross[0]))
#manDist
manDistArray = []
for i, coordinate in enumerate(arrayCross):
    #print(i)
    #print(arrayCross[i])
    manDistNewEntry = mdist.cityblock(centralPort, arrayCross[i])
    manDistArray.append(manDistNewEntry)
    #print(manDistNewEntry)
    #print(manDistArray)
    #print(manDist)
print("Manhattan value is", min(manDistArray))