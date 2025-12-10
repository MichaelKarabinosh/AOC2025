import itertools
import math

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

def do_move_p2(combo,expected):
    dummy = []
    for i in range(len(expected)):
        dummy.append('0')
    # print(dummy)
    for subcombo in combo:
        subcombo = subcombo.strip('(').strip(')').split(',')
        for num in subcombo:
            num = int(num)
            dummy[num] = str(int(dummy[num]) + 1)
    # print(dummy)
    return dummy == expected

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

def create_list(n):
    list12 = []
    for i in range(1,n+1):
        list12.append(str(i))
    return list12

def multi_combo_combo(n,orig):
    list12 = []
    for i in range(0,n):
        inter = int(orig[i])*n
        list12.append(str(inter))
    return list12

def update_super_combo(orig, multi):
    hyper_list = []
    for i in range(0,len(orig)):
        subcombo = orig[i]
        print(subcombo)
        toupdate = []
        for j in range(0,len(subcombo)):
            number = int(subcombo[j]) * multi[i]
            toupdate.append(str(number))
        hyper_list.append(toupdate)
    return hyper_list

def sum_of_multis(multi):
    counter = 0
    for num in multi:
        counter += num
    return counter


# print(update_super_combo(([('0'),('1','2'),('1','2','3')]), (1,2,3)))

def part_two():
    total = 0
    for line in newlines:
        concats = line.split(' ')
        expected = concats[len(concats)-1].strip('{').strip('}').split(',')
        # print(expected)
        data = []
        for i in range(1, len(concats) - 1):
            data.append(concats[i].strip('(').strip(')'))
        found = False
        counter = 2
        summer = 0
        while not found:
            multi_combinations = list(itertools.combinations(create_list(counter), counter))
            for i in range(0,len(multi_combinations)):
                multi = multi_combinations[i]
                combinations = list(itertools.combinations(data, counter))
                # print(combinations)
                for combo in combinations:
                    if do_move_p2(update_super_combo(combo,multi), expected):
                        found = True
                        summer = sum_of_multis(multi)
                        counter += 1
                        # print(combo)
            total += summer
    return total

# print('Part One:', part_one())
print(part_two())
#
# print(create_list(4))
# print(multi_combo_combo(4,('1','2','3','4')))
# print(list(itertools.combinations_with_replacement([1,2,3,4,5],5)))

# do_move(['(1,3)','(1,3)','(2)','(2,3)','(0,2)','(0,1)'],'[.##.]')