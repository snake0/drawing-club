import numpy as np
import matplotlib.pyplot as plt
from color import *

font_size=20
font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)

x = ["apache", "apache-build", "openssl", "Blowfish", "MD5", "povray",
        "7zip", "AVG"]
giantvm_ratio = [69.3, 91.2, 92.8, 80.6, 92.7, 93.9, 59.0, 82.7]
naive_ratio = [58.8, 75.9, 82.4, 68.4, 70.2, 81.2, 80.4, 73.9]

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
ax.set_ylabel("Normalized Results", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=font_size)

ax.set_ylim(50, 100)

for i in xrange:
    naive_ratio_bar = ax.bar(i-0.5*bar_interval, naive_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color=color_red, edgecolor="black")
    giantvm_ratio_bar = ax.bar(i+0.5*bar_interval, giantvm_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color=color_green, edgecolor="black")

ax.legend((naive_ratio_bar, giantvm_ratio_bar),
        ("Performance w/o Yanni", "Performance w/ Yanni"),
        loc=0, prop={'size': 16}, ncol=2, frameon=False)

plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/macro2-perf.pdf', dpi=300)
plt.show()
