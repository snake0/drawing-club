# sphinx_gallery_thumbnail_number = 2

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import random
import statistics

giantvm_file_names = ["../cpulog/giantvm/terasort-node257.log",
    "../cpulog/giantvm/terasort-node258.log",
    "../cpulog/giantvm/terasort-node259.log",
    "../cpulog/giantvm/terasort-node260.log"]
baseline_file_names = ["../cpulog/baseline/terasort-node257.log",
    "../cpulog/baseline/terasort-node258.log",
    "../cpulog/baseline/terasort-node259.log",
    "../cpulog/baseline/terasort-node260.log"]

font_size = 30
font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium', size=font_size)

def plot_color_gradients(cpu_util, start, end):
    fig, axes = plt.subplots(nrows=4)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.1, right=0.99)
    fig.set_size_inches(15, 4)

    for ax, node in zip(axes, range(4)):
        l = []
        d = cpu_util[node]
        for ts in range(start, end):
            if (ts not in d.keys()):
                if (ts-1 not in d.keys()):
                    l.append(0)
                else:
                    l.append(d[ts-1])
            else:
                l.append(d[ts])
        l = np.vstack((l, l))

        ax.imshow(l, aspect='auto', cmap=plt.get_cmap("Greens"))
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, "Node"+str(node), va='center', ha='right',
                fontdict=font)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

    return fig

def parse_input(file_names):
    # {#Node:{timestamp:cpu_util}}
    cpu_util = dict()
    for idx in range(len(file_names)):
        cpu_util_per_node = dict()
        with open(file_names[idx]) as fp:
            line = fp.readline()
            while (line):
                line = line.split()
                ts = int(line[0])
                util = map(lambda x : int(x), line[1:])
                cpu_util_per_node[ts] = statistics.mean(util)
                line = fp.readline()
        cpu_util[idx] = cpu_util_per_node
    return cpu_util

def get_range(cpu_util):
    start = 0x0
    end = 0xFFFFFFFF
    for k in cpu_util.keys():
        if (min(cpu_util[k].keys()) > start):
            start = min(cpu_util[k].keys())
        if (max(cpu_util[k].keys()) < end):
            end = max(cpu_util[k].keys())
    return (start, end)

def main():
    cpu_util = parse_input(giantvm_file_names)
    start, end = get_range(cpu_util)
    fig = plot_color_gradients(cpu_util, start, end)
    plt.savefig("../../imgs/cpu_util_colocation_w_pllm.pdf", dpi=300)

    cpu_util = parse_input(baseline_file_names)
    start, end = get_range(cpu_util)
    fig = plot_color_gradients(cpu_util, start, end)
    plt.savefig("../../imgs/cpu_util_baseline_spark.pdf", dpi=300)
    plt.show()

main()
