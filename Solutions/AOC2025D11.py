import networkx
from matplotlib import pyplot as plt

with open('../Inputs/InputFile11', 'r') as file:
    lines = file.readlines()
    newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

network = networkx.DiGraph()# directed graph means nodes are one way

dict = {}
for line in newlines:
    split = line.split(':')
    placeholder = split[1].split(' ')
    placeholder.pop(0) # include falsy value added
    dict[split[0]] = placeholder
    for item in placeholder:
        network.add_edge(split[0], item)

def part_one(): # lol thanks networkx
    part_one_answer = 0
    for path in networkx.all_simple_paths(network, source='you', target='out'): # lol thanks networkx
        # print(path)
        part_one_answer += 1
    return part_one_answer

def part_two():
    sort_order = list(networkx.topological_sort(network))
    path_counts = {node: 0 for node in network.nodes()}
    source = 'svr'
    destination = 'dac'
    path_counts[source] = 1

    # Iterate through nodes in topological order
    for node in sort_order:
        # If the destination is reached, we can stop the overall count if we only care about it
        if node == destination:
            break

        # Update counts for neighbors
        if path_counts[node] > 0:
            for successor in network.successors(node):
                path_counts[successor] += path_counts[node]

    return path_counts[destination]


# print('Part One:', part_one())
print('Part Two:', part_two())