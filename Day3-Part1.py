import numpy as np
file = open(".\\Inputs\\inputDay3TEST.txt", "r")
wire1 = file.readlines(1)
wire2 = file.readlines(2)
wire1Array = wire1[0].split(',')
wire2Array = wire2[0].split(',')
array = np.ones([10,10], dtype=str)
column = 0
row = 9
centralPort = row,column
array[centralPort] = 'O' 
np.set_printoptions(threshold=np.sys.maxsize)
print(array)

pointer = centralPort
for command in wire1Array:
    dir = command[0]
    dist = int(command[1])
    print(dir)
    if dir == 'R':
        for num in dist:
            array[column + 1, row] = 'R'
            dist -= 1
