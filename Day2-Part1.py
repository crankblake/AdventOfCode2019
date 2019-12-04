# How many elements each list should have 
n = 4 
file = open(".\\Inputs\\inputDay2.txt", "r")
file = file.read()
file = (file.split(','))
#converting string array to int aray
for i in range(0, len(file)):
    file[i] = int(file[i])
print(file)
myList = [file[i * n:(i + 1) * n] for i in range((len(file) + n - 1) // n )] 
#using list comprehension to seperate into chunks of 4 numbers 
#print(myList) 
for opcode in myList:
    #elementHEAD = int(opcode[0])
    #print("\noperand is", elementHEAD)
    if opcode[0] == 1:
        #print("we got 1")
        #inputIndex = 0
        #for input in range(0,len(opcode) - 1):
        #for input in opcode:
        for index, input in enumerate(opcode):
            print("\nopcode is", opcode)
            print("index is", index)
            print("input is", input)
            #inputIndex += 1
            if index == 1:
                opcode[3] = opcode[1] + opcode[2]
                print("opcode is now",opcode)
    if opcode[0] == 2:
        for index, input in enumerate(opcode):
            print("\nopcode is", opcode)
            print("index is", index)
            print("input is", input)
            #inputIndex += 1
            if index == 1:
                opcode[3] = opcode[1] * opcode[2]
                print("opcode is now",opcode)
        #print("we got 2")
    if opcode[0] == 99:
        for index, input in enumerate(opcode):
            print("\nopcode is", opcode)
            print("index is", index)
            print("input is", input)
            break
        print("opcode is 99, stopping...")
        break
    elif opcode[0] != 99 and opcode[0] != 1 and opcode[0] != 2:
        print("\ncould not match correct operand for", opcode[0])
print(myList)
 