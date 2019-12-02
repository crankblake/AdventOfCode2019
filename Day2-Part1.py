# How many elements each list should have 
n = 4 
file=open(".\\Inputs\\inputDay2.txt", "r")
file = file.read()
file = (file.split(','))
#using list comprehension to seperate into chunks of 4 numbers
myList = [file[i * n:(i + 1) * n] for i in range((len(file) + n - 1) // n )]  
#print(myList) 
for element in myList:
    elementHEAD = int(element[0])
    print("\noperand is", elementHEAD)
    if elementHEAD == 1:
        print("we got 1")
        for input in opcode:
            if input[] == 1
    if elementHEAD == 2:
        print("we got 2")
    if elementHEAD == 99:
        print("we got 99")
    elif elementHEAD != 99 and elementHEAD != 1 and elementHEAD != 2:
        print("could not match correct operand for", elementHEAD)
 