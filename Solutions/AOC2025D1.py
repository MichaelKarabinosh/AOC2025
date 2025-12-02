with open('../Inputs/InputFile1', 'r') as file:
    lines = file.readlines()
newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)


def part_1():
    counter = 0
    number_pos = 50
    for code in newlines:
        rotation = code[0]
        number = int(code[1:])

        if rotation == 'R':
            number_pos += int(number)
        if rotation == 'L':
            number_pos -= int(number)

        if number_pos > 99:
            number_pos = (number_pos - 100) % 100
        if number_pos < 0:
            number_pos = (100 + number_pos) % 100
        if number_pos == 0:
            counter+= 1
    return counter

def part_2():
    counter2 = 0
    number_pos = 50
    for code in newlines:
        rotation = code[0]
        number = int(code[1:])
        for _ in range(number):
            if rotation == 'L':
                number_pos = (number_pos - 1 + 100) % 100
            else:
                number_pos = (number_pos + 1) % 100
            if number_pos == 0:
                counter2 += 1
    return counter2

print('Part One:', part_1())
print('Part Two:', part_2())
