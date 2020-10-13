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
gini_baseline = [0.18, 0.14, 0.26, 0.03, 0.05, 0.06, 0.06, 0.14, 0.04,
        0.22, 0.1, 0.05, 0.07, 0.30, 0.01, 0.114]
gini_giantvm = [0.04, 0.14, 0.17, 0.03, 0.01, 0.03, 0.07, 0.11, 0.04,
        0.2, 0.15, 0.04, 0.14, 0.28, 0.03, 0.0987]

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
ax.set_ylabel("Gini Coefficient", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=16)

ax.set_ylim(0, 0.35)

for i in xrange:
    gini_baseline_bar = ax.bar(i-0.5*bar_interval, gini_baseline[i], width=bar_width*bar_zoom,
        bottom=0, color=color_red, edgecolor="black",
        label="Gini Baseline")
    gini_giantvm_bar = ax.bar(i+0.5*bar_interval, gini_giantvm[i], width=bar_width*bar_zoom,
        bottom=0, color=color_green, edgecolor="black",
        label="Gini PLLM", alpha=0.7)

ax.legend((gini_baseline_bar, gini_giantvm_bar),
        ("Gini w/o Yanni", "Gini w/ Yanni"),
        loc=0, prop={'size': 18}, ncol=2, frameon=False)

plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/giantvm-macro-gini.pdf', dpi=300)
plt.show()
