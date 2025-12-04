import copy
with open('../Inputs/InputFile4', 'r') as file:
    lines = file.readlines()
newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

grid = []

for line in newlines:
    elements = list(line)
    grid.append(elements)
    # print(elements)


def count_rolls(grid,xpos,ypos):
    count = 0
    if ypos > 0 and xpos > 0:
        if grid[ypos-1][xpos-1] == '@':
            count += 1
    if ypos > 0:
        if grid[ypos-1][xpos] == '@':
            count += 1
    if ypos > 0 and xpos < len(grid[ypos]) -1:
        if grid[ypos-1][xpos+1] == '@':
            count += 1
    if xpos > 0:
        if grid[ypos][xpos-1] == '@':
            count += 1
    if xpos < len(grid[ypos]) -1:
        if grid[ypos][xpos+1] == '@':
            count += 1
    if ypos < len(grid[ypos]) - 1 and xpos > 0:
        if grid[ypos+1][xpos-1] == '@':
            count += 1
    if ypos < len(grid[ypos]) -1:
        if grid[ypos+1][xpos] == '@':
            count += 1
    if ypos < len(grid[ypos]) - 1 and xpos < len(grid[ypos]) - 1:
        if grid[ypos+1][xpos+1] == '@':
            count += 1
    # print(grid[ypos][xpos], ypos,xpos, count)
    if count < 4:
        return True

    return False

def part_one():
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                if count_rolls(grid,x,y):
                    total += 1
    return total

def part_one_modified(grid1):
    total = 0
    copied_grid = copy.deepcopy(grid1)
    for y in range(len(grid1)):
        for x in range(len(grid1[y])):
            if grid1[y][x] == '@':
                if count_rolls(grid1,x,y):
                    total +=1
                    copied_grid[y][x] = 'x'
    return [copied_grid, total]

def part_two():
    master_total = 0
    ans = part_one_modified(grid)
    master_total += ans[1]
    while ans[1] >= 1:
        ans = part_one_modified(ans[0])
        master_total += ans[1]
    return master_total

print('Part One:', part_one())
print('Part Two:', part_two())




