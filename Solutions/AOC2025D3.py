with open('../Inputs/InputFile3', 'r') as file:
    lines = file.readlines()
newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

def find_max(line):
    return "".join(sorted(line,reverse=True))[0]


def hyp_iterate(line):
    max = 0
    for i in range(len(line) - 1): # basically just take the number at index i and then splice from index i to rest of string, and compare these vals to find max
        num = int(line[i] + find_max(line[i+1:]))
        if num > max:
            max = num
    return max

def part_one():
    total = 0
    for coltage in newlines:
        total += hyp_iterate(coltage)
    return total

def part_two():
    total = 0
    for colage in newlines:
        total += int(hyp_iterate2(colage))
    return total

def hyp_iterate2(line):
    numbers_left = 12
    index = 0
    str = ""
    length= len(line)
    while numbers_left > 0:
        # print(line[index:(15-numbers_left) + 1])
        max = find_max(line[index:(length-numbers_left) + 1]) # sample numbers are easier to explain. in the beginning we have 15 numbers and 12 left to choose. this means we can only pick the max from the first 4 digits. then since we've chosen a digit, left to choose -1 and the numbers in the string go down depending on where in the 4 digits we spliced. repeat until number is formed.
        str += max
        index = line[index:(length-numbers_left) + 1].index(max) + index + 1
        # print(index)
        numbers_left -= 1
    return str

print('Part One:', part_one())
print('Part Two:', part_two())
