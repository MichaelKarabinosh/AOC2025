import math
import matplotlib.pyplot as plt
import numpy as np

with open('../Inputs/InputFile9', 'r') as file:
    lines = file.readlines()
    newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

def part_one():
    distances = []
    for i in range(len(newlines)):
        pair11, pair12 = newlines[i].split(',')
        for j in range(i):
            pair21,pair22 = newlines[j].split(',')
            # print(pair11, pair12)
            area = int((math.fabs((int(pair22) - int(pair12)))+1) * (math.fabs((int(pair21) - int(pair11)))+1))
            distances.append(area)
    distances.sort(reverse=True)
    return distances[0]

def construct_grid():
    grid = []
    x_points = []
    y_points = []
    for i in range(len(newlines)):
        pair11, pair12 = newlines[i].split(',')
        x_points.append(int(pair11))
        y_points.append(int(pair12))
    xpoints1 = np.array(x_points)
    ypoints1 = np.array(y_points)
    plt.plot(x_points, y_points, marker='o', linestyle='-')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Scatter Plot of Points")

    plt.show()


print('Part One:', part_one())
construct_grid()

