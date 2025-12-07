with open('../Inputs/InputFile6', 'r') as file:
    lines = file.readlines()
newlines = []
for line in lines:
    line = line.strip('\n')
    line = line.replace('  ', ' ')
    line2 = line.split(' ')
    line2 = list(filter(None, line2))
    newlines.append(line2)

with open('../Inputs/InputFile6', 'r') as file: # better to not parse out spaces and other null vals for p2
    lines = file.readlines()
newlines2 = []
for line in lines:
    line = line.strip('\n')
    newlines2.append(line)


def part_one():
    total = 0

    for i in range(0, len(newlines[0])):
        operator = newlines[len(newlines)-1][i]

        if operator == '+':
            subtotal = 0
        else: subtotal = 1

        for j in range(0, len(newlines)-1):
            if operator == '*':
                subtotal *= int(newlines[j][i])
            if operator == '+':
                subtotal += int(newlines[j][i])
        total += subtotal
    return total

def create_horiz_list():
    str_horiz = ''
    list2 = []
    for i in range(0, len(newlines2[0])):
        for j in range(len(newlines2) - 1):
            str_horiz += newlines2[j][i]
        list2.append(str_horiz.strip())
        str_horiz = ''
    return list2

def part_two(): # too lazy to comment this lol
    total = 0
    counter = 0

    list2 = create_horiz_list()

    operators = newlines[len(newlines) - 1]
    operator = operators[counter]

    if operator == '+':
        subtotal = 0
    else: subtotal = 1

    for i in range(len(list2)):
        if list2[i] != '':
            if operator == '*':
                subtotal *= int(list2[i])
            if operator == '+':
                subtotal += int(list2[i])
        else:
            counter += 1
            operator = operators[counter]
            total += subtotal
            if operator == '+':
                subtotal = 0
            else:
                subtotal = 1
    total += subtotal
    return total

print('Part One:', part_one())
print('Part Two:', part_two())
