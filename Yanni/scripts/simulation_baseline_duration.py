import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from heatmap import *

# sphinx_gallery_thumbnail_number = 2

fig, ax = plt.subplots()
fig.set_size_inches(7.85, 7.85)
font_size = 20
font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium', size=font_size)

plt.tick_params(labelsize=font_size)

ratio = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]
machines = range(700, 920, 20)

duration = np.array([
    [789, 790, 798, 801, 802, 803, 813, 818, 825, 827],
    [775, 776, 780, 782, 788, 788, 794, 806, 808, 810],
    [766, 770, 772, 772, 779, 780, 784, 787, 791, 792],
    [755, 756, 759, 762, 763, 763, 773, 777, 778, 782],
    [746, 749, 749, 751, 752, 755, 762, 765, 766, 767],
    [736, 741, 742, 743, 746, 747, 750, 755, 757, 758],
    [725, 728, 728, 729, 735, 738, 743, 744, 746, 750],
    [720, 722, 723, 726, 728, 728, 732, 733, 735, 737],
    [711, 714, 715, 716, 721, 721, 723, 725, 726, 728],
    [703, 708, 708, 709, 712, 714, 714, 717, 720, 721],
    [699, 699, 701, 702, 706, 706, 709, 709, 709, 712],
])

ax.set_ylabel("#Machines", fontdict=font)
ax.set_xlabel("Over Commitment Ratio", fontdict=font)
ax.xaxis.set_label_position('top')
im, cbar = heatmap(duration, machines, ratio, ax=ax,
        cmap="PuOr", cbarlabel="")
cbar.set_clim(650, 850)
texts = annotate_heatmap(im, valfmt="{x:d}", threshold=800)

fig.tight_layout()
plt.savefig('../../imgs/simulation_baseline_duration.pdf', dpi=300)
plt.show()
