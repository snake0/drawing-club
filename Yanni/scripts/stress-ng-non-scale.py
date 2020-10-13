import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from color import *

font_size = 22
marker_size = 10
line_width = 2.5

fig, ax = plt.subplots()

font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium', size=font_size)
fig.set_size_inches(10, 7.85)

dot_style = ['s', 'd', 'x', '^', '.', 'D']

# Data for plotting
node = range(1, 9)
cpu = [697.09, 1511.65, 1864.27, 2787.06, 3688.54, 4052.23, 5173.72, 5669.07]
zlib = [56.63, 103.49, 161.82, 216.88, 231.41, 319.92, 374.21, 393.4]
io = [516.6, 584.89, 363.65, 172.71, 100.58, 78.98, 55.03, 29.72]
epoll = [80296.93, 3069.91, 1404.63, 936.72, 655.01, 421.08, 271.11, 362.93]
pipe = [825750.43, 71140.12, 53389.44, 41592.49, 20656.51, 19844.92, 13574.38, 12346.85]
sem = [3467682.21, 84060.71, 41202.07, 30075.55, 32524.16, 58169.42, 18394.82, 42018.73]

for i in range(1, 8):
    for l in (cpu, zlib, io, epoll, pipe, sem):
        l[i] = l[i] / l[0]

for l in (cpu, zlib, io, epoll, pipe, sem):
    l[0] = 1.0


ax.plot(node, cpu, marker=dot_style[0], markersize=marker_size, markerfacecolor="black",
        label="cpu", linewidth=line_width, color=color_green)
ax.plot(node, zlib, marker=dot_style[1], markersize=marker_size, markerfacecolor="black",
        label="zlib", linewidth=line_width, color=color_green)

ax.plot(node, io, marker=dot_style[2], markersize=marker_size, markerfacecolor="black",
        label="io", linewidth=line_width, color=color_red)
ax.plot(node, epoll, marker=dot_style[3], markersize=marker_size, markerfacecolor="black",
        label="epoll", linewidth=line_width, color=color_red)
ax.plot(node, pipe, marker=dot_style[4], markersize=marker_size, markerfacecolor="black",
        label="pipe", linewidth=line_width, color=color_red)
ax.plot(node, sem, marker=dot_style[5], markersize=marker_size, markerfacecolor="black",
        label="sem", linewidth=line_width, color=color_red)

plt.xlabel("#Node", fontdict=font)
plt.ylabel("Normalized Results", fontdict=font)
plt.tick_params(axis='both', which='major', labelsize=font_size)
#plt.title("Unscalability of GiantVM", fontdict=font)

ax.grid()

plt.yscale("log")
plt.ylim([0.001, 500])
plt.legend(loc=0, prop={'size': font_size}, ncol=3)

plt.tight_layout()
fig.savefig("../../imgs/stress-ng-non-scale.pdf", dpi=300)
plt.show()
