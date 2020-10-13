import numpy as np
import matplotlib.pyplot as plt
from color import *

font_size=26
font = {'size': font_size, 'family': 'HelveticaNeue', 'weight': 'medium'}
plt.rc('font', family='HelveticaNeue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(6.5, 4)
plt.subplots_adjust()

x = ["naïve co-location", "Yanni"]
lc_latency = [2031455.692/1976033.625, 1975565.927/1976033.625]
lc_95latency = [3195470.417/2332104.538, 2344859.067/2332104.538]
lc_99latency = [4752269.695/2514224.813, 3464523.773/2514224.813]
lc_999latency = [5658748.351/2633488.885, 4364897.765/2633488.885]

xrange = np.arange(len(x));

bar_width = 0.2
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

plt.xticks(xrange, x)
ax.set_ylabel("Normalized Latency", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=font_size)

ax.set_ylim(.8, 2.5)

for i in xrange:
    latency_bar = ax.bar(i-3*bar_interval/2, lc_latency[i], width=bar_width*bar_zoom,
        bottom=0, color=color_red, edgecolor="black")
    latency95_bar = ax.bar(i-bar_interval/2, lc_latency[i], width=bar_width*bar_zoom,
        bottom=0, color=color_blue, edgecolor="black")
    latency99_bar = ax.bar(i+bar_interval/2, lc_99latency[i], width=bar_width*bar_zoom,
        bottom=0, color=color_green, edgecolor="black")
    latency999_bar = ax.bar(i+3*bar_interval/2, lc_999latency[i], width=bar_width*bar_zoom,
        bottom=0, color=color_indigo, edgecolor="black")

ax.legend((latency_bar, latency95_bar, latency99_bar, latency999_bar),
        ("Avgerage", "95th Percentile", "99th Percentile", "99.9th Percentile"),
        prop={"size":17}, loc="upper right")

plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/lc-latency.pdf', dpi=300)
