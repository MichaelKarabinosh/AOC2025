import itertools
import pulp

with open('../Inputs/InputFile10', 'r') as file:
    lines = file.readlines()
    newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

def do_move(combo,expected):
    length = len(expected)
    str = ''
    for i in range(length):
        str += '.'

    for subcombo in combo:
        subcombo = subcombo.strip('(').strip(')').split(',')
        for num in subcombo:
            num = int(num)
            if str[num] == '.':
                str = str[:num] + '#' + str[num + 1:]
            elif str[num] == '#':
                str = str[:num] + '.' + str[num + 1:]
    return str == expected


def part_one():
    total = 0
    for line in newlines:
        concats = line.split(' ')
        expected = concats[0].strip('[').strip(']')
        data = []
        for i in range(1, len(concats)-1):
            data.append(concats[i])
        found = False
        counter = 0
        while not found:
            counter += 1
            combinations = list(itertools.combinations(data, counter))
            # print(combinations)
            for combo in combinations:
                if do_move(combo, expected):
                    found = True
                    # print(combo)
        total += counter
    return total


def prep_rref(orig,expected):
    dummy = []
    for i in range(0,len(expected)):
        dummy.append(0)
    for num in orig:
        dummy[num] = dummy[num] + 1
    return dummy


def solve_min_presses(buttons, targets):
    output_length = len(targets)
    num_buttons = len(buttons)
    prob = pulp.LpProblem("min_presses", pulp.LpMinimize)
    x = []
    for j in range(num_buttons):
        x.append(pulp.LpVariable(f"x{j}", lowBound=0, cat='Integer'))
    # x = [pulp.LpVariable(f"x{j}", lowBound=0, cat='Integer') for j in range(num_buttons)]
    prob += pulp.lpSum(x)
    for p in range(output_length):
        prob += pulp.lpSum(x[j] for j in range(num_buttons) if p in buttons[j]) == targets[p]
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return int(pulp.value(prob.objective))

def part_two():
    total = 0
    for line in newlines:
        concats = line.split(' ')
        expected = concats[len(concats)-1].strip('{').strip('}').split(',')
        data = []
        for i in range(1, len(concats) - 1):
            datai = concats[i].strip('(').strip(')').split(',')
            data.append(datai)
        data.append(expected)
        matrix_ints = []
        for row_str in data:
            row_ints = [int(element) for element in row_str]
            matrix_ints.append(row_ints)
        for i in range(len(expected)):
            expected[i] = int(expected[i])
        sub = solve_min_presses(matrix_ints, expected)
        total += sub
    return total
print('Part One:', part_one())
print('Part Two:', part_two())