def calcFuel(fuelModule):
    fuelEntry = 0
    fuelEntry = ((lineINT//3) - 2)
    calcFuel()
file=open(".\\Inputs\\inputDay1.txt", "r")
fuel = 0
for line in file:
    lineINT = int(line)
    fuelModule = ((lineINT//3) - 2)
    calcFuel()
print(fuel)
