import numpy as np
import matplotlib.pyplot as plt
from color import *

font_size=20
font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)
plt.subplots_adjust()

x = ["sort", "terasort", "wordcount", "nweight", "als", "bayes", "gbt",
        "kmeans", "lda", "linear", "svm", "rf", "pca", "svd", "pagerank", "AVG"]
cpu_ratio_baseline = [9.64, 20.4, 19.5, 52.1, 37.7, 27.5, 17.5, 27, 45.6,
        7.2, 13.4, 20.2, 12.3, 3.4, 49.2, 24.2]
cpu_ratio_giantvm = [17.5, 24.5, 24.8, 55.4, 41.1, 37.2, 23, 32.3, 49.8,
        12.4, 19.2, 28.5, 17.4, 10.2, 51.2, 29.6]

xrange = np.arange(len(x));

title = ""
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['///', '\\\\\\', '----', '//////',
           '++++', 'xxxxxx', '\\\\\\\\\\\\', '----']

bar_width = 0.35
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

ax.set_title(title, fontdict=font)

plt.xticks(xrange, x, rotation=50)
ax.set_ylabel("CPU Utilization", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=16)

ax.set_ylim(0, 65)

for i in xrange:
    cpu_ratio_baseline_bar = ax.bar(i-0.5*bar_interval, cpu_ratio_baseline[i], width=bar_width*bar_zoom,
        bottom=0, color=color_red, edgecolor="black",
        label="CPU Ratio Baseline")
    cpu_ratio_giantvm_bar = ax.bar(i+0.5*bar_interval, cpu_ratio_giantvm[i], width=bar_width*bar_zoom,
        bottom=0, color=color_green, edgecolor="black",
        label="CPU Ratio GiantVM")

ax.legend((cpu_ratio_baseline_bar, cpu_ratio_giantvm_bar),
        ("CPU Util w/o Yanni", "CPU Util w/ Yanni"),
        loc=0, prop={'size': 18}, ncol=2, frameon=False)

plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/giantvm-macro-util.pdf', dpi=300)
plt.show()
