import random
inputFile = open("InputFile.txt", "w+")
for i in range(7):
    seatsReserved = random.randint(1, 15)
    inputFile.write('{} {}{}'.format("R"+'{:04d}'.format(i), seatsReserved, '\n'))
inputFile.close()
