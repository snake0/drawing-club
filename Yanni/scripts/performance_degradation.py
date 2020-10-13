import numpy as np
import matplotlib.pyplot as plt
from color import *

font_size = 35

font = {'size': font_size, 'family': 'HelveticaNeue', 'weight': 'medium'}
plt.rc('font', family='HelveticaNeue', weight='medium', size=font_size)

fig, ax = plt.subplots()
fig.set_size_inches(10, 7.85)
fig.subplots_adjust(top=.95,bottom=.15,right=.95,left=.15)

apache = [630, 657, 632, 624, 639, 582, 452, 321, 617, 639, 644, 637, 635]
iperf = [342, 334, 344, 344, 321, 322, 297, 302, 344, 345, 332, 332, 345]
redis = [6896.55, 6993.01, 6060.61, 6578.95, 6134.97, 5952.38, 6097.56, \
        3952.57, 4310.34, 5882.35, 6060.61, 6493.51, 6329.11]
x = range(len(apache))

apache_max = max(apache)
iperf_max = max(iperf)
redis_max = max(redis)
for i in x:
    apache[i] = apache[i] * 1.0 / apache_max
    iperf[i] = iperf[i] * 1.0 / iperf_max
    redis[i] = redis[i] * 1.0 / redis_max

dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
colors = [color_red, color_blue, color_green]
marker_size = 12
labelx = -0.15
downtime_draw = []
total_draw = []
linewidth = 4

#ax.set_title("Performance degradation during migration")
ax.plot(x, apache, fillstyle='none', linestyle='-', marker=dot_style[0],\
        markersize=marker_size, linewidth=linewidth, label='apache',\
         color=colors[0])
ax.plot(x, iperf, fillstyle='none', linestyle='-', marker=dot_style[1],\
        markersize=marker_size, linewidth=linewidth, label='iperf',\
         color=colors[1])
ax.plot(x, redis, fillstyle='none', linestyle='-', marker=dot_style[2],\
        markersize=marker_size, linewidth=linewidth, label='redis',\
         color=colors[2])
ax.set_xlabel("Time/s",fontdict=font)
ax.set_ylabel("Normalized QPS",fontdict=font)
plt.tick_params(axis='both', which='major')
ax.legend(loc=0)
ax.grid()

plt.xticks(x)
# ax.set_xticklabels(labels, rotation = 30)
#plt.tight_layout()
plt.savefig('../../imgs/performance_degradation.pdf', dpi=300)
plt.show()
