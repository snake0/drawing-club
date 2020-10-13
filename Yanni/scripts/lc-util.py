import numpy as np
import matplotlib.pyplot as plt
from color import *

font_size=26
font = {'size': font_size, 'family': 'HelveticaNeue', 'weight': 'medium'}
plt.rc('font', family='HelveticaNeue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(6.5, 4)
plt.subplots_adjust()

x = ["w/o", "naïve", "Yanni"]
lc_util = [30.6147614, 36.10551394, 41.28190491]
lc_gini = [0.568788477, 0.48619563, 0.425715139]

xrange = np.arange(len(x));

bar_width = 0.35
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

plt.xticks(xrange, x)
ax.set_ylabel("CPU Utilization", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=font_size)

ax2 = ax.twinx()
ax2.set_ylabel("Gini Coefficient", fontdict=font)
ax2.tick_params(axis='both', which='major', labelsize=font_size)

ax.set_ylim(20, 50)
ax2.set_ylim(.3, .6)

for i in xrange:
    util_bar = ax.bar(i-bar_interval/2, lc_util[i], width=bar_width*bar_zoom,
        bottom=0, color=color_red, edgecolor="black")
    gini_bar = ax2.bar(i+bar_interval/2, lc_gini[i], width=bar_width*bar_zoom,
        bottom=0, color=color_green, edgecolor="black")

ax2.legend((util_bar, gini_bar), ("CPU Util", "Gini"),
        prop={"size":18}, loc="upper right", frameon=False)
plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/lc-util.pdf', dpi=300)
