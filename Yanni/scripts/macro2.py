import numpy as np
import matplotlib.pyplot as plt

font_size=28
font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(14, 10)
plt.subplots_adjust(top=0.95, right=0.95)

x = ["apache", "apache-build", "openssl", "Blowfish", "MD5", "povray",
        "compress-7zip", "AVG"]
giantvm_ratio = [69.3, 91.2, 92.8, 80.6, 92.7, 93.9, 59.0, 82.7]
naive_ratio = [58.8, 75.9, 82.4, 68.4, 70.2, 81.2, 80.4, 73.9]
giantvm_cpu_ratio = [32.5, 32.9, 36.3, 35.5, 35.5, 35, 38.3, 35.1]
naive_cpu_ratio = [29, 30, 34.1, 33, 33, 33.9, 33.4, 32.3]
giantvm_gini = [0.11, 0.12, 0.07, 0.08, 0.08, 0.09, 0.09, 0.09]
naive_gini = [0.2, 0.19, 0.22, 0.22, 0.22, 0.23, 0.22, 0.21]

xrange = np.arange(len(x));

title = ""
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['///', '\\\\\\', '----', '//////',
           '++++', 'xxxxxx', '\\\\\\\\\\\\', '----']

bar_width = 0.2
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

ax.set_title(title, fontdict=font)

plt.xticks(xrange, x, rotation=30)
ax.set_ylabel("Normalized Results", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=font_size)

ax.set_ylim(20, 110)

ax2 = ax.twinx()
ax2.set_ylabel("Gini Coefficient", fontdict=font)
ax2.tick_params(axis='both', which='major', labelsize=font_size)

ax2.set_ylim(0, 0.5)

first_arrow = False
for i in xrange:
    giantvm_ratio_bar = ax.bar(i+1.5*bar_interval, giantvm_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color="#AAAAAA", edgecolor="black")
    naive_ratio_bar = ax.bar(i+0.5*bar_interval, naive_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color="#DDDDDD", edgecolor="black")
    giantvm_cpu_ratio_bar = ax.bar(i-1.5*bar_interval, giantvm_cpu_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color="#80f20d", edgecolor="black",
        label="CPU Ratio GiantVM", hatch='/')
    naive_cpu_ratio_bar = ax.bar(i-1.5*bar_interval, naive_cpu_ratio[i], width=bar_width*bar_zoom,
        bottom=0, color="#f76e6e", edgecolor="black",
        label="CPU Ratio Baseline")
    naive_gini_bar = ax2.bar(i-0.5*bar_interval, naive_gini[i], width=bar_width*bar_zoom,
        bottom=0, color="#56A0D7", edgecolor="black",
        label="Gini Baseline", hatch='\\')
    giantvm_gini_bar = ax2.bar(i-0.5*bar_interval, giantvm_gini[i], width=bar_width*bar_zoom,
        bottom=0, color="#1DDC73", edgecolor="black",
        label="Gini GiantVM", alpha=0.7)
    if (not first_arrow):
        for b1 in naive_ratio_bar:
            (x1,y1),(x2,y2) = b1.get_bbox().get_points()
        for b2 in giantvm_ratio_bar:
            (x3,y3),(x4,y4) = b2.get_bbox().get_points()
        ax.annotate(
            '',xytext=((x3+x4)/2, y2),
            xy=((x3+x4)/2, y4),
            arrowprops=dict(arrowstyle="|-|", linewidth=3)
        )
        ax.annotate(
            'Performance improvement\ndue to the\nmitigation of\ninterference.',
            xy=((x3+x4)/2, (y2+y4)/2),
            xytext=((x3+x4)/2-1.05, y4+14),
            arrowprops=dict(arrowstyle="->", linewidth=1),
            fontsize=20,
            ha='left'
        )

        first_arrow = True

ax2.legend((giantvm_ratio_bar, naive_ratio_bar, giantvm_cpu_ratio_bar,
        naive_cpu_ratio_bar, naive_gini_bar, giantvm_gini_bar),
        ("Colocation w/ PLLM", "Colocation w/o PLLM", "CPU Util w/ PLLM",
        "CPU Util w/o PLLM", "Gini w/o PLLM", "Gini w/ PLLM"),
        loc=0, prop={'size': 20}, ncol=3, frameon=True)

plt.grid(True)
plt.tight_layout()
plt.savefig('../../imgs/macro2.pdf', dpi=300)
plt.show()
