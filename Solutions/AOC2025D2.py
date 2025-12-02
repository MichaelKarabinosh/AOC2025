import math

with open('../Inputs/InputFile2', 'r') as file:
    line = file.readline().strip()
newlines = line.split(',')


def is_invalid(line):
    half = int(len(line) / 2)
    return line[0:half] == line[half:]

def part_one():
    count = 0

    for numpair in newlines:
        numpair2 = numpair.split('-')
        num1 = int(numpair2[0])
        num2 = int(numpair2[1])

        for i in range(num1, num2+1):
            if is_invalid(str(i)):
                count += i
    return count

def part_two():
    masterset = []

    for numpair in newlines:
        numpair2 = numpair.split('-')
        num1 = int(numpair2[0])
        num2 = int(numpair2[1])

        for i in range(num1, num2+1):
            for r in range(1,int((len(str(i))/2)) + 1):
                if is_invalid2(r, str(i)):
                    masterset.append(i)

    list2 = list(set(masterset))
    total = 0
    for num in list2:
        total += num
    return total



def is_invalid2(n,line):
    cur = 0
    masterset = []
    num = (len(line)/n)
    if not num.is_integer():
        return False

    for r in range(0, int(len(line)/n)):
        masterset.append(line[cur+n*r:cur+n*r+n])
    return len(list(set(masterset))) == 1

print('Part One:', part_one())
print('Part Two:', part_two())
