import numpy as np
import matplotlib.pyplot as plt
from color import *

font_size=20
font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)
plt.subplots_adjust(top=0.95, right=0.95)

x = ["apache", "apache-build", "openssl", "Blowfish", "MD5", "povray",
        "7zip", "AVG"]
giantvm_gini = [0.11, 0.12, 0.07, 0.08, 0.08, 0.09, 0.09, 0.09]
naive_gini = [0.2, 0.19, 0.22, 0.22, 0.22, 0.23, 0.22, 0.21]

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

ax.set_ylabel("Gini Coefficient", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=font_size)

ax.set_ylim(0, 0.3)

for i in xrange:
    naive_gini_bar = ax.bar(i-0.5*bar_interval, naive_gini[i], width=bar_width*bar_zoom,
        bottom=0, color=color_red, edgecolor="black",
        label="Gini Baseline")
    giantvm_gini_bar = ax.bar(i+0.5*bar_interval, giantvm_gini[i], width=bar_width*bar_zoom,
        bottom=0, color=color_green, edgecolor="black",
        label="Gini GiantVM")

ax.legend((naive_gini_bar, giantvm_gini_bar),
        ("Gini w/o Yanni", "Gini w/ Yanni"),
        loc=1, prop={'size': 16}, ncol=2, frameon=False)

plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/macro2-gini.pdf', dpi=300)
plt.show()
