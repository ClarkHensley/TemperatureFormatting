#!/usr/bin/env python3

import csv
import os
import matplotlib.pyplot as plt
import matplotlib.colors as col


class Point:

    def __init__(self, y, z, t):
        self.y = round(float(y), 5)
        self.z = round(float(z), 5)
        self.t = float(t)


colors = ["purple", "blue", "cyan", "green", "yellow", "red", "gray"]
levels = len(colors) - 1
cwd = os.path.dirname(os.path.realpath(__file__))

thresholds = [100, 250, 500, 750, 1000, 2000]
myMap, myNorm = col.from_levels_and_colors(thresholds, colors, extend="both")

with open("blt_feb_extract_COORDS.csv", mode="r") as file:

    csvFile = csv.reader(file)
    lines = []

    for line in csvFile:
        lines.append(line)

    csvData = lines[6:]
    plots = {}

    for line in csvData:
        temp = Point(line[2], line[3], line[4])
        x = float(line[1])

        if x in plots:
            plots[x].append(temp)

        else:
            temp_arr = []
            temp_arr.append(temp)
            plots[x] = temp_arr


for plot in plots:
    ys = []
    zs = []
    ts = []
    for d in plots[plot]:
        ys.append(d.y)
        zs.append(d.z)
        ts.append(d.t)
    plt.tricontourf(ys, zs, ts, levels=levels, cmap=myMap, norm=myNorm)
    curr_plot = plt.gcf()
    plt.show()
    curr_plot.savefig(os.path.join(cwd, f"TemperatureData-{plot}.png"))
