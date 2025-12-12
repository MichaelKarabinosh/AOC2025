import math
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon,point
import shapely
from shapely.plotting import plot_polygon

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
        # x_points, y_points = int(pair11), int(pair12)
        x_points.append(int(pair11))
        y_points.append(int(pair12))
    xpoints1 = np.array(x_points)
    ypoints1 = np.array(y_points)
    plt.plot(x_points, y_points, marker='o', linestyle='-')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Scatter Plot of Points")
    plt.show()

def part_two():
    vertices = []
    areas = []
    for i in range(len(newlines)):
        xpoint, ypoint = map(int, newlines[i].split(','))
        vertices.append((xpoint, -ypoint))
        # print(vertices)
    polygon_a = Polygon(vertices)
    # print(polygon_a)
    # fig, ax = plt.subplots()
    # plot_polygon(polygon_a, ax=ax, add_points=True, color='blue', alpha=0.5)
    # plot_polygon(Polygon([(9,-5),(9,-3),(2,-3),(2,-5)]), ax=ax, add_points=True, color='red', alpha=0.5)
    # plt.show()
    for i in range(len(newlines)):
        x1, y1 = map(int, newlines[i].split(','))
        for j in range(i):
            x2, y2 = map(int, newlines[j].split(','))
            polygon_b = Polygon([(x1, -y1), (x1, -y2), (x2, -y2), (x2, -y1)])
            # print(polygon_b)
            if polygon_a.contains(polygon_b):
                area = (math.fabs(y2-y1)+1) * (math.fabs(x2-x1)+1)
                areas.append([area,(x1,y1),(x2,y2)])
    return sorted(areas, key=lambda x: x[0],reverse=True)[0]



print('Part One:', part_one())
part2 = part_two()
print('Part Two:', int(part2[0]))



vertices = []
areas = []
for i in range(len(newlines)):
    xpoint, ypoint = map(int, newlines[i].split(','))
    vertices.append((xpoint, -ypoint))
    # print(vertices)
polygon_a = Polygon(vertices)
x1,y1 = part2[1]
x2,y2 = part2[2]

polygon_b = Polygon([(x1, -y1), (x1, -y2), (x2, -y2), (x2, -y1)])
fig, ax = plt.subplots()
plot_polygon(polygon_a, ax=ax, add_points=True, color='blue', alpha=0.5)
plot_polygon(polygon_b, ax=ax, add_points=True, color='red', alpha=0.5)
plt.show()




