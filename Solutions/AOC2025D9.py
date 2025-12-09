import math

with open('../Inputs/InputFile9', 'r') as file:
    lines = file.readlines()
    newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

def part_one():
    distances = []
    for i in range(len(newlines)):
        pair11, pair12 = newlines[i].split(',')
        for j in range(i):
            pair21,pair22 = newlines[j].split(',')
            # print(pair11, pair12)
            area = int((math.fabs((int(pair22) - int(pair12)))+1) * (math.fabs((int(pair21) - int(pair11)))+1))
            distances.append(area)
    distances.sort(reverse=True)
    return distances[0]


print('Part One:', part_one())

