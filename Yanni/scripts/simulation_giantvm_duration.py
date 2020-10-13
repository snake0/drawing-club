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
    [774, 776, 777, 777, 777, 787, 787, 794, 800, 801],
    [757, 759, 761, 761, 770, 770, 775, 781, 785, 787],
    [747, 750, 751, 753, 754, 759, 762, 764, 768, 772],
    [737, 740, 741, 741, 741, 749, 750, 755, 758, 762],
    [729, 729, 732, 735, 736, 737, 742, 743, 747, 749],
    [720, 721, 723, 727, 727, 728, 734, 735, 737, 739],
    [714, 716, 716, 717, 718, 723, 725, 727, 728, 730],
    [706, 707, 708, 708, 713, 719, 720, 721, 722, 723],
    [696, 698, 702, 704, 708, 708, 709, 711, 713, 714],
    [693, 693, 693, 696, 699, 702, 705, 705, 705, 707],
    [686, 693, 693, 694, 694, 694, 696, 700, 703, 703],
])

ax.set_ylabel("#Machines", fontdict=font)
ax.set_xlabel("Over Commitment Ratio", fontdict=font)
ax.xaxis.set_label_position('top')
im, cbar = heatmap(duration, machines, ratio, ax=ax,
        cmap="PuOr")
cbar.set_clim(650, 850)
texts = annotate_heatmap(im, valfmt="{x:d}", threshold=800)

fig.tight_layout()
plt.savefig('../../imgs/simulation_giantvm_duration.pdf', dpi=300)
plt.show()
