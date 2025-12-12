import networkx
from matplotlib import pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

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
        part_one_answer += 1
    return part_one_answer


def num_paths_between_nodes(source, destination):
    sort_order = list(networkx.topological_sort(network))
    path_counts = {}
    for node in network.nodes():
        path_counts[node] = 0
    path_counts[source] = 1


    for node in sort_order: #check through nodes in sequential order
        if node == destination: # can stop once destination reached
            break

        if path_counts[node] > 0: #update neighbors
            for successor in network.successors(node):
                path_counts[successor] += path_counts[node]

    return path_counts[destination]

def part_two():
    dac_to_fft = num_paths_between_nodes("dac", "fft")
    fft_to_dac = num_paths_between_nodes("fft", "dac")
    answer = 0
    if dac_to_fft > 0:
        answer = num_paths_between_nodes("svr", "dac") * dac_to_fft * num_paths_between_nodes("fft", "out") # basically this is a 3 segment process that is dependent on the location of fft and dac between svr and out. we are multiplying because for nodes between a through b, the nodes through a to c can be found by nodes(a,b) * nodes(b,c)
    elif fft_to_dac > 0:
        answer = num_paths_between_nodes("svr", "fft") * fft_to_dac * num_paths_between_nodes("dac", "out")
    return answer


print('Part One:', part_one())
print('Part Two:', part_two())
