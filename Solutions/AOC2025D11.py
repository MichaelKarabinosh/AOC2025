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


def draw_graph():
    for layer, nodes in enumerate(networkx.topological_generations(network)):
        for node in nodes:
            network.nodes[node]["layer"] = layer
    pos = networkx.multipartite_layout(network,subset_key="layer")


    node_colors = []
    highlight_node = 'dac'
    highlight_node2 = 'fft'
    for node in network.nodes():
        if node == highlight_node or node == highlight_node2:
            node_colors.append('red')  # Highlight color
        else:
            node_colors.append('skyblue')  # Default color



    fig, ax = plt.subplots()
    networkx.draw_networkx(network, pos=pos, node_color=node_colors, ax=ax, with_labels=True, arrows=True)
    plt.show()


# print('Part One:', part_one())
print('Part Two:', part_two())
print(draw_graph())