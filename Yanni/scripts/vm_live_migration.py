import numpy as np
import matplotlib.pyplot as plt
from color import *

font_size = 26
marker_size = 10
line_width = 2.5
bar_width = 0.25       # the width of the bars: can also be len(x) sequence
bar_interval = bar_width * 1.1

font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium', size=font_size)

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True)
fig.set_size_inches(13, 10)
plt.subplots_adjust(top=0.97, bottom=0.15, right=0.95)

labels = ["apache", "apache-build", "openssl", "Blowfish",
        "MD5", "povray", "7zip", "redis", "phpbench"]
N = 9
working_set = [482, 683, 469, 510, 520, 510, 3791, 507, 702]
PLLM = [162, 693.6, 74.2, 78.4, 54.7, 60.1, 9943.1, 99.6, 62.2]
w_o_diff = [267.9, 1207.9, 125.7, 145.6, 130.3, 118.4, 10022.0, 133.0, 89.4]
vm_live_migration = [995.8, 2329, 838.1, 910.9, 921.4, 863.5, 5120.9, 1129, 862.9]

ind = np.arange(N)    # the x locations for the groups

for i in ind:
    #working_set_bar = ax.bar(i - bar_interval, working_set[i], bar_width, color=colors[0],
            #edgecolor="black", hatch='++')
    vm_bar = ax.bar(i + bar_interval, vm_live_migration[i], bar_width, color=color_red,
            edgecolor="black")
    diff_bar = ax.bar(i - bar_interval, w_o_diff[i], bar_width, color=color_indigo, edgecolor="black", hatch='///')
    PLLM_bar = ax.bar(i, PLLM[i], bar_width, color=color_green, edgecolor="black")
    #ax2.bar(i - bar_interval, working_set[i], bar_width, color=colors[0],
            #edgecolor="black", hatch='++')
    ax2.bar(i + bar_interval, vm_live_migration[i], bar_width, color=color_red,
            edgecolor="black")
    ax2.bar(i - bar_interval, w_o_diff[i], bar_width, color=color_indigo, edgecolor="black", hatch='///')
    ax2.bar(i, PLLM[i], bar_width, color=color_green, edgecolor="black")

ax.set_ylim(2000, 11000)  # outliers only
ax2.set_ylim(0, 1300)  # most of the data

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

# This looks pretty good, and was fairly painless, but you can get that
# cut-out diagonal lines look with just a bit more work. The important
# thing to know here is that in axes coordinates, which are always
# between 0-1, spine endpoints are at these locations (0,0), (0,1),
# (1,0), and (1,1).  Thus, we just need to put the diagonals in the
# appropriate corners of each of our axes, and so long as we use the
# right transform and disable clipping.

d = .010  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# No common y-label for two subplots, hence such hack.
ax.set_ylabel('Network Bandwidth/MB' + 50 * ' ')
#ax.set_title('Network Bandwidth Consumption')
ax2.set_title('...')
plt.xticks(ind, labels, rotation=25)
ax.legend((diff_bar, PLLM_bar, vm_bar),
        ("Yanni w/o diff compression",
        "Yanni", "VM live migration"), prop={'size': font_size}, loc=0)

plt.savefig('../../imgs/vm_live_migration.pdf', dpi=300)
plt.show()
