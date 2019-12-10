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
arrayCross = [(4, 6), (6, 3)]
for i, intersection in enumerate(arrayCross):
    column = 0
    row = 9
    print("\nintersection", intersection)  
    for index, command in enumerate(wire1Array):
        dir = command[0]
        dist = int(command[1:])
        skip = False
        if dir == 'R':
            for i in range (0, dist):
                #if array[row, column0 == intersection:
                    #print("got a match for array[row, column +1] and intersection", array[row,column + 1], intersection)
                print("row, column", row,column)
                if (row, column) == intersection:
                    print("got a match for array[row, column -1] and intersection", row, column, intersection)
                    skip = True
                    arrayStepsWire1.append((row,column)) 
                array[row, column + 1] = 'R1'
                column += 1
        if dir == 'U':
            for i in range (0, dist):
                #if array[row, column] == intersection:
                    #print("got a match for array[row, column -1] and intersection", array[row - 1,column], intersection)
                print("row, column", row,column)
                if (row, column) == intersection:
                    print("got a match for array[row, column -1] and intersection", row, column, intersection)
                    skip = True
                    arrayStepsWire1.append((row,column)) 
                array[row - 1, column] = 'U1'
                row -= 1
        if dir == 'L':        
            for i in range (0, dist):
                #if array[row, column] == intersection:
                    #print("got a match for array[row, column -1] and intersection", array[row,column - 1], intersection)
                print("row, column", row,column)
                if (row, column) == intersection:
                    print("got a match for array[row, column -1] and intersection", row, column, intersection)
                    skip = True
                    arrayStepsWire1.append((row,column)) 
                array[row, column - 1] = 'L1'
                column -= 1
        if dir == 'D':
            for i in range (0, dist):
                #if array[row, column] == intersection:
                    #print("got a match for array[row + 1, column] and intersection", array[row + 1,column], intersection)
                print("row, column", row,column)
                if (row, column) == intersection:
                    print("got a match for array[row, column -1] and intersection", row, column, intersection)
                    skip = True
                    arrayStepsWire1.append((row,column)) 
                array[row + 1, column] = 'D1'
                row += 1
        if skip == False:
            arrayStepsWire1.append((index,dist)) 
column = 0
row = 9           
for index, command in enumerate(wire2Array):
    dir = command[0]
    dist = int(command[1:])
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


'''arrayCross = [(25, 557), (84, 4630), (121, 4108), (131, 5212), (203, 4987), (203, 5244), (215, 12995), (299, 1281), (299, 1472), (354, 5413), (354, 5427), (354, 5545), (516, 4543), (516, 4742), (516, 4987), (549, 5545), (579, 5287), (615, 557), (622, 5870), (622, 5883), (646, 5212), (646, 5758), (776, 12564), (810, 5758), (882, 436), (985, 5212), (1023, 5451), (1075, 13070), (1374, 13190), (1374, 13664), (1374, 13773), (1423, 13643), (1423, 13664), (1423, 13768), (1423, 13773), (1533, 13053), (1533, 13070), (1533, 13353), (1552, 13353), (2157, 13343), (2157, 13653), (2198, 13263), (2324, 13263), (2342, 13343), (2342, 13431), (2342, 13636), (2342, 13755), (2382, 13765), (2474, 13343), (2474, 13431), (2474, 13636), (2474, 13755), (2474, 13761), (2533, 13197), (2646, 11941), (2646, 11948), (2646, 12011), (2646, 12071), (2646, 12133), (2646, 12297), (2805, 14049), (2848, 11739), (2856, 12326), (2879, 12326), (2951, 12326), (2972, 12475), (2972, 12620), (2972, 12792), (2972, 12804), (2972, 12908), (2972, 12965), (2972, 13156), (2972, 13171), (3013, 13969), (3041, 11739), (3051, 11739), (3075, 12011), (3075, 12110), (3075, 12183), (3075, 12200), (3155, 11714), (3155, 11739), (3300, 12463), (3305, 12463), (3328, 12489), (3339, 12697), (3379, 12697), (3424, 12982), (3435, 11624), (3435, 11689), (3457, 13215), (3459, 11880), (3578, 11880), (3635, 11458), (3635, 11508), (3635, 11689), (3635, 11807), (3767, 11426), (3808, 11426), (13552, 3973), (14018, 2238), (14224, 4547), (14224, 4791), (14363, 1965), (14363, 2018), (14363, 2238), (14388, 4364), (14405, 4943), (14473, 4079), (14473, 4364), (14494, 2831), (14684, 12673), (14684, 12766), (14684, 12785), (14804, 4108), (14848, 12535), (14850, 675), (14850, 852), (14850, 971), (14899, 12995), (14966, 12408)]'''
'''column = 0
row = 9          
for i, intersection in enumerate(arrayCross):
    for index, command in enumerate(wire1Array):
        dir = command[0]
        dist = int(command[1:])
        if dir == 'R':
            for i in range (0, dist):
                #if array[row, column + 1] == intersection:
                 #   print("got a match for array[row, column +1] and intersection", array[row,column + 1], intersection)
                print("row, column", row,column)
                array[row, column + 1] = 'R1'
                column += 1
        if dir == 'U':
            for i in range (0, dist):
                array[row - 1, column] = 'U1'
                row -= 1
        if dir == 'L':        
            for i in range (0, dist):
                array[row, column - 1] = 'L1'
                column -= 1
        if dir == 'D':
            for i in range (0, dist):
                array[row + 1, column] = 'D1'
                row += 1
        arrayStepsWire1.append((index,dist))''' 