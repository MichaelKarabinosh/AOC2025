import math

with open('InputFile1', 'r') as file:
    lines = file.readlines()

newlines = []

for line in lines:
    line = line.strip('\n')
    newlines.append(line)



def part_1():
    counter = 0
    numberPos = 50
    for code in newlines:
        rotation = code[0]
        number = int(code[1:])

        if rotation == 'R':
            numberPos += int(number)
        if rotation == 'L':
            numberPos -= int(number)
        print(numberPos, 'pos')

        if numberPos > 99:
            numberPos = (numberPos - 100) % 100
        if numberPos < 0:
            numberPos = (100 + numberPos) % 100
        if numberPos == 0:
            counter+= 1
    return counter

def part_2():
    counter = 0
    numberPos = 50
    for code in newlines:
        rotation = code[0]
        number = int(code[1:])
        prev = numberPos

        if rotation == 'R':
            numberPos += int(number)
        if rotation == 'L':
            numberPos -= int(number)

        if numberPos > 99:
            numberPos = (numberPos - 100) % 100
        if numberPos < 0:
            numberPos = (100 + numberPos) % 100
        counter += math.floor((prev+number)/100)
    return counter

print(part_1())
print(part_2())
