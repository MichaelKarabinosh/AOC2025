import networkx


with open('../Inputs/InputFile11', 'r') as file:
    lines = file.readlines()
    newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

network = networkx.DiGraph() # directed graph means nodes are one way
dict = {}
for line in newlines:
    split = line.split(':')
    placeholder = split[1].split(' ')
    placeholder.pop(0) # include falsy value added
    dict[split[0]] = placeholder
    for item in placeholder:
        network.add_edge(split[0], item) # add all edges

def part_one(): # lol thanks networkx
    part_one_answer = 0
    for path in networkx.all_simple_paths(network, source='you', target='out'): # lol thanks networkx
        # print(path)
        part_one_answer += 1
    return part_one_answer

def part_two():
    part_two_answer = 0
    for path in networkx.all_shortest_paths(network, source='svr', target='out'):
        if 'dac' in path and 'fft' in path:
            part_two_answer += 1
    return part_two_answer


# print('Part One:', part_one())
print('Part Two:', part_two())