output = 0
val = 19690720

def program(noun, verb):
    #we are going to travel through the loop after every 4 iterations with n
    n = 4 
    file = open(".\\Inputs\\inputDay2.txt", "r")
    file = file.read()
    file = (file.split(','))
    #converting string array to int aray
    for i in range(0, len(file)):
        file[i] = int(file[i])
    #initial setup
    #file[1] = 41
    #file[2] =  12
    file[1] = noun
    file[2] = verb
    #print("Here's the list after initial setup", file)
    #myList = [file[i * n:(i + 1) * n] for i in range((len(file) + n - 1) // n )] 
    #using list comprehension to seperate into chunks of 4 numbers 
    for fileIndex, f in enumerate(file):
        #print("\n\nfileIndex is", fileIndex)
        #print("f is", f)
        if fileIndex % n != 0:
            #print("starting over at", fileIndex)
            continue
        if file[fileIndex] == 1:
            #print("we got a 1 operand")
            changeIndex1 = int(fileIndex) + 1
            changeIndex2 = int(fileIndex) + 2
            changeIndex3 = int(fileIndex) + 3
            valueIndex1 = file[changeIndex1]
            valueIndex2 = file[changeIndex2]
            storeIndex = file[changeIndex3]
            file[storeIndex] = file[valueIndex2] + file[valueIndex1]
            #print("file is now",file)
        if file[fileIndex] == 2:
            #print("we got a 2 operand")
            changeIndex1 = int(fileIndex) + 1
            changeIndex2 = int(fileIndex) + 2
            changeIndex3 = int(fileIndex) + 3
            valueIndex1 = file[changeIndex1]
            valueIndex2 = file[changeIndex2]
            storeIndex = file[changeIndex3]
            file[storeIndex] = file[valueIndex2] * file[valueIndex1]
            #print("file is now",file)
        if file[fileIndex] == 99:
            #print("we got a 99 operand... stopping")
            #print("file is now",file)
            break
        elif file[fileIndex] != 99 and file[fileIndex] != 1 and file[fileIndex] != 2:
            #print("\ncould not match correct operand for", file[fileIndex])
    print("\n\nnoun is", file[1])
    print("verb is", file[2])
    print("position[0] is", file[0])
    output = position[0]
    if file[0] == 19690720:
        print("position[0] is equal!")
        result = (100 * file[1]) + file[2]
        print("result is", result)
        run == False
#program(41, 12)
x = 0
y = 0

while run == True:
    val = program(x, y)
    if (output < val):
        x += 1


