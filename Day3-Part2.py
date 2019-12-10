import time
startTime = time.time()
import numpy as np
import scipy.spatial.distance as mdist

file = open(".\\Inputs\\inputDay3TEST.txt", "r")
wire1 = file.readlines(1)
wire2 = file.readlines(2)
wire1Array = wire1[0].split(',')
wire2Array = wire2[0].split(',')
dt = np.dtype(('U2'))
array = np.empty([10,10], dtype=dt)
#array = np.empty([30000,30000], dtype=object)
array.fill('__')
column = 0
row = 9
#column =  15000
#row = 15000
centralPort = [(row,column)]
array[centralPort[0]] = 'CP'
arrayStepsWire1 = []
arrayStepsWire2 = []  
#np.set_printoptions(threshold=np.sys.maxsize)
for index, command in enumerate(wire1Array):
    #print("\nindex is", index)
    #print("command is", command)
    dir = command[0]
    #print("dir is", dir)
    dist = int(command[1:])
    #arrayStepsWire1.append((index,dist))
    #print("dist is", dist)
    if dir == 'R':
        for i in range (0, dist):
            #print("dist is", dist)
            #print("i is", i)
            print("row, column", row,column)
            array[row, column + 1] = 'R1'
            column += 1
    if dir == 'U':
        for i in range (0, dist):
            #print("dist is", dist)
            #print("i is", i)
            #print("row, column", row,column)
            array[row - 1, column] = 'U1'
            #print("row, column", row, column)
            row -= 1
    if dir == 'L':        
        for i in range (0, dist):
            #print("row, column", row,column)
            array[row, column - 1] = 'L1'
            column -= 1
    if dir == 'D':
        for i in range (0, dist):
            #print("row, column", row,column)
            array[row + 1, column] = 'D1'
            row += 1
    arrayStepsWire1.append((index,dist)) 
column = 0
row = 9 
#column =  15000
#row = 15000           
for index, command in enumerate(wire2Array):
    #print("\nindex is", index)
    #print("command is", command)
    dir = command[0]
    dist = int(command[1:])
    #print("dir is", dir)
    #print("dist is", dist)
    skip = False
    if dir == 'R':
        for i in range (0, dist):
            if array[row, column + 1] == 'U1' or array[row, column + 1] == 'D1':
                array[row, column + 1] = 'XX'
                arrayStepsWire2.append((index,column + 1))
                skip = True   
            else:
                array[row, column + 1] = 'R2'
            column += 1
    if dir == 'U':
        for i in range (0, dist):
            if array[row - 1, column] == 'L1' or array[row - 1, column] == 'R1':
                array[row - 1, column] = 'XX'
                arrayStepsWire2.append((index,row - 1))
                skip = True   
            else:
                array[row - 1, column] = 'U2'
            row -= 1
    if dir == 'L':        
        for i in range (0, dist):
            if array[row, column - 1] == 'U1' or array[row, column - 1] == 'D1':
                array[row, column - 1] = 'XX'
                arrayStepsWire2.append((index,column - 1))
                skip = True   
            else:
                array[row, column - 1] = 'L2'
            column -= 1
    if dir == 'D':
        for i in range (0, dist):
            if array[row + 1, column] == 'L1' or  array[row + 1, column] == 'R1':
                array[row + 1, column] = 'XX'
                arrayStepsWire2.append((index,row + 1))
                skip = True   
            else:
                array[row + 1, column] = 'D2'
            row += 1
    if skip == False:                     
        arrayStepsWire2.append((index,dist))   
#print(array)
arrayCross = []
for i, row in enumerate(array):
    for j, value in enumerate(row):
        #print("row and value index", i, j)
        #print("row and value", row, value)
        if value == 'XX':
            arrayCross.append((i,j))
#print(arrayCross)
manDistArray = []
for i, coordinate in enumerate(arrayCross):
    manDistNewEntry = mdist.cityblock(centralPort, arrayCross[i])
    #print("Manhattan value is", manDistNewEntry)
    manDistArray.append(manDistNewEntry)
    #print(manDistNewEntry)
print("Manhattan value is", min(manDistArray))
print("--- %s seconds ---" % (time.time() - startTime))
