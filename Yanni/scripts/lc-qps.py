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
lc_qps = [1, 530.09375/532.525, 517.775/532.525]

xrange = np.arange(len(x));

bar_width = 0.35
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

plt.xticks(xrange, x)
ax.set_ylabel("Normalized QPS", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=font_size)

ax.set_ylim(.96, 1.02)

for i in xrange:
    qps_bar = ax.bar(i, lc_qps[i], width=bar_width*bar_zoom,
        bottom=0, color=color_red, edgecolor="black")

plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/lc-qps.pdf', dpi=300)
