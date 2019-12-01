from array import array
array_num = array('i')
def calcFuel(fuelModule):
    fuelEntry = ((fuelModule//3) - 2)
    array_num.append(fuelEntry)
    if fuelEntry > 8:
        calcFuel(fuelEntry)
file=open(".\\Inputs\\inputDay1.txt", "r")
for line in file:
    lineINT = int(line)
    calcFuel(lineINT)
print(sum(array_num))