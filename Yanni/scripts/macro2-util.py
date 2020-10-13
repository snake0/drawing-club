import numpy as np
import matplotlib.pyplot as plt
from color import *

font_size=20
font = {'size': font_size, 'family': 'HelveticaNeue', 'weight': 'medium'}
plt.rc('font', family='HelveticaNeue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)

x = ["apache", "apache-build", "openssl", "Blowfish", "MD5", "povray",
        "7zip", "AVG"]
giantvm_cpu_ratio = [32.5, 32.9, 36.3, 35.5, 35.5, 35, 38.3, 35.1]
naive_cpu_ratio = [29, 30, 34.1, 33, 33, 33.9, 33.4, 32.3]

xrange = np.arange(len(x));

title = ""
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['///', '\\\\\\', '----', '//////',
           '++++', 'xxxxxx', '\\\\\\\\\\\\', '----']

bar_width = 0.45
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

ax.set_title(title, fontdict=font)

plt.xticks(xrange, x, rotation=20)
ax.set_ylabel("CPU Utilization", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=font_size)

ax.set_ylim(25, 40)

for i in xrange:
    naive_cpu_ratio_bar = ax.bar(i-0.5*bar_interval, naive_cpu_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color=color_red, edgecolor="black",
        label="CPU Ratio Baseline")
    giantvm_cpu_ratio_bar = ax.bar(i+0.5*bar_interval, giantvm_cpu_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color=color_green, edgecolor="black",
        label="CPU Ratio GiantVM")

ax.legend((naive_cpu_ratio_bar, giantvm_cpu_ratio_bar),
        ("CPU Util w/o Yanni", "CPU Util w/ Yanni"),
        loc=1, prop={'size': 16}, ncol=2, frameon=False)

plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/macro2-util.pdf', dpi=300)
plt.show()
