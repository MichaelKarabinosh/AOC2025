from collections import deque
import math

with open('../Inputs/InputFile8', 'r') as file:
    lines = file.readlines()
    newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

nums = []
for line in newlines:
    split = line.split(',')
    num1 = int(split[0])
    num2 = int(split[1])
    num3 = int(split[2])
    p1 = (num1,num2,num3)
    nums.append(p1)


distances = []
for i in range(len(nums)):
    x1,y1,z1 = nums[i]
    for j in range(i):
        if i != j:
            x2,y2,z2 = nums[j]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            distances.append((distance, i, j)) # important that im appending the index of the box and not the actual coordinates (dealing with tuples makes life a lot harder)

# print(distances)
distances.sort()

adjacent1 = [[] for _ in range(len(nums))]

def connected(circuit1, circuit2):
    visited = set()
    list1 = [circuit1]
    while list1: # while list is truthy/ not empty
        x = list1.pop() # grab last element of list
        if x == circuit2:
            return True
        if x not in visited:
            visited.add(x)
        for next_circuit in adjacent1[x]:
            if next_circuit not in visited:
                list1.append(next_circuit)
    return False


def circuit_box_sizes():
    visited = set()
    junc_sizes = []
    for start in range(len(nums)):
        if start not in visited:
            size = 0
            queue = deque([start])
            visited.add(start)
            while queue:
                x = queue.popleft()
                size += 1
                for next_circuit in adjacent1[x]:
                    if next_circuit not in visited:
                        visited.add(next_circuit)
                        queue.append(next_circuit)
            junc_sizes.append(size)
    return sorted(junc_sizes)


def both_parts():
    answers = []
    connections = 0
    checked = 0
    for dist, i, j in distances:

        if checked == 1000:  # upper bound
            product1 = circuit_box_sizes()[-1] * circuit_box_sizes()[-2] * circuit_box_sizes()[-3]
            answers.append(product1)

        if not connected(i, j): # if not alr connected add circuit1 to circuit2 and circuit2 to circuit1
            adjacent1[i].append(j)
            adjacent1[j].append(i)
            connections += 1

            if connections == len(nums) - 1: # if we have made as many connection as possible, return product of the last two
                product2 = nums[i][0] * nums[j][0]
                answers.append(product2)
                return answers

        checked += 1

answer = both_parts()
print('Part One:',answer[0])
print('Part Two:',answer[1])