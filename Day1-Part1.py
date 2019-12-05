file = open(".\\Inputs\\inputDay1.txt", "r")
fuel = 0
for line in file:
    lineINT = int(line)
    fuel = fuel + ((lineINT//3) - 2)
print(fuel)

