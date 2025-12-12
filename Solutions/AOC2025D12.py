with open('../Inputs/InputFile12', 'r') as file:
    lines = file.readlines()
    newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

common_list = [[0,1,0],[1,0,1],[0,1,0]] # essentially create a 3x3 map of alternating 1s and 0s

def count_parity(list): # parity problems hold a special place in my heart, love to see it featured in advent this year. essentially, it's a spin on the classic fitting dominoes on a chessboard
    counter_zero = 0
    counter_one = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == '#': #if we see a block there, check the common list for a 1 or 0, then count the 1s and 0s.
                if common_list[i][j] == 0:
                    counter_zero += 1
                if common_list[i][j] == 1:
                    counter_one += 1
    # print(list,counter_zero,counter_one)
    return counter_zero, counter_one





def make_parity_dict():
    dict1 = {}
    counter = 0
    for i in range(0,len(newlines)):
        line = newlines[i]
        if 'x' not in line:
            list = []
            if ':' in line:
                for j in range(1,4): # find the colon and then the three entries below it are our box instructions
                    list.append(newlines[i+j])
                dict1[counter] = count_parity(list)
                counter += 1
    return dict1


def can_fit(order,size,dict1): #essentially, if the number of ones and zeros combined is below the size of the present, it can fit
    counter_zero = 0
    counter_one = 0
    for i in range(len(order)):
        pairing = dict1[i] #basically we'll have something like 4,2 which means that box combo takes up 4 0s and 2 1s of space, so let's multiply that by the number of boxes in the area
        counter_zero_to_append = pairing[0] * int(order[i])
        counter_one_to_append = pairing[1] * int(order[i])
        counter_zero += counter_zero_to_append
        counter_one += counter_one_to_append
    if counter_one + counter_zero <= size:
        return True
        #
        # if counter_one % 2 == 0 and counter_zero % 2 == 0: this is for when i thought the problem was more complex than it actuallywas lol
        #     print(counter_zero, counter_one, order, size)
        #     return True
        # elif counter_one % 2 == 1 and counter_zero % 2 == 1:
        #     print(counter_zero, counter_one, order, size)
        #     return True
    return False



def part_one():
    counter = 0
    index = 30  # index right after the present manual is finished
    parity_dict = make_parity_dict()
    for i in range(index,len(newlines)):
        items = newlines[i].split(':')
        area_num_1, area_num_2 = items[0].split('x')
        area = int(area_num_1) * int(area_num_2)
        order = items[1].split(' ')
        order.pop(0) # keeping an extra element at the beginning for some reason
        if can_fit(order,area,parity_dict):
            counter += 1
    return counter


print('Part One:', part_one())



