with open('../Inputs/InputFile7', 'r') as file:
    lines = file.readlines()
newlines = []
newlinesmaster = []
for line in lines:
    line = line.strip('\n')
    for char in line:
        newlines.append(char)
    newlinesmaster.append(newlines)
    newlines = []

startpos = newlinesmaster[0].index('S')
newlinesmaster[0][startpos] = '|'

def part_one(): # strategy here is to basically animate the beam moving through the input and count every time a tachyon or whatever they're called is hit
    counter =0
    for i in range(len(newlinesmaster)):
        for q in range(len(newlinesmaster[i])):
            if newlinesmaster[i][q] == '|' and i != len(newlinesmaster[i]) and newlinesmaster[i+1][q] != '^':
                newlinesmaster[i+1][q] = '|'
            if newlinesmaster[i][q] == '^' and newlinesmaster[i-1][q] == '|':
                counter += 1
                newlinesmaster[i][q-1] = '|'
                newlinesmaster[i][q+1] = '|'
                newlinesmaster[i+1][q - 1] = '|'
                newlinesmaster[i+1][q + 1] = '|'
    return counter


def count(list, ypos, xpos, masterdict): # brain is too fried to comment on this; basically just recursively searched through each entry finding beam breaks
    len1 = len(list)
    sublen = len(list)
    if ypos >= len1:
        return 1
    if (ypos, xpos) in masterdict:
        return masterdict[ypos, xpos]
    counter = 0
    if list[ypos][xpos] == '^':
        if xpos - 1 >= 0:
            counter += count(list, ypos, xpos - 1, masterdict)
        if xpos + 1 < sublen:
            counter += count(list, ypos, xpos + 1, masterdict)
    else:
        counter = count(list, ypos + 1, xpos, masterdict)
    masterdict[ypos, xpos] = counter
    return counter


def part_two():
    return count(newlinesmaster, 0, startpos, {})

print('Part One:', part_one())
print('Part Two:', part_two())