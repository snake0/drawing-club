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
spark_ratio = [99.5, 91.1, 96.6, 97.9, 95.0, 99.6, 88.9, 96.4, 103.9,
        100.1, 93.4, 98.9, 101.9, 94.9, 100, 97.2, 97.2]
apache_ratio = [79.2, 75.6, 77.0, 56.3, 61.9, 65.8, 79.3, 69.4,
        62.4, 72.3, 77.7, 75.1, 81.7, 82.5, 28.4, 71.6]

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
ax.set_ylabel("Normalized Results", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=16)

ax.set_ylim(20, 115)

for i in xrange:
    spark_ratio_bar = ax.bar(i-0.5*bar_interval, spark_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color=color_red, edgecolor="black",
        label="GiantVM")
    apache_ratio_bar = ax.bar(i+0.5*bar_interval, apache_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color=color_green, edgecolor="black",
        label="Apache")

ax.legend((spark_ratio_bar, apache_ratio_bar),
        ("Spark Performance", "Apache Performance"),
        loc=0, prop={'size': 18}, ncol=2, frameon=False)

plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/giantvm-macro-perf.pdf', dpi=300)
plt.show()
