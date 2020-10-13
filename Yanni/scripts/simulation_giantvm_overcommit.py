import numpy as np
import matplotlib
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

overcommit = np.array([
    [133, 145, 159, 169, 185, 194, 207, 218, 225, 227],
    [134, 143, 158, 168, 180, 191, 201, 209, 217, 219],
    [135, 144, 156, 167, 177, 187, 194, 203, 209, 211],
    [131, 143, 154, 163, 173, 182, 190, 196, 201, 202],
    [133, 143, 151, 160, 170, 177, 185, 190, 191, 193],
    [132, 140, 148, 157, 167, 172, 178, 183, 185, 185],
    [128, 136, 144, 155, 162, 168, 171, 177, 180, 180],
    [129, 135, 143, 150, 155, 163, 168, 170, 170, 171],
    [125, 133, 140, 147, 152, 157, 161, 165, 165, 166],
    [124, 131, 138, 145, 148, 151, 156, 156, 156, 158],
    [122, 128, 135, 141, 144, 147, 151, 151, 152, 155],
])

for i in range(len(overcommit)):
    overcommit[i] = overcommit[i][::-1]

ax.set_ylabel("#Machines", fontdict=font)
ax.set_xlabel("Over Commitment Ratio", fontdict=font)
ax.xaxis.set_label_position('top')
im, cbar = heatmap(overcommit, machines, ratio, ax=ax,
                   cmap="PuOr")
cbar.set_clim(120, 230)
texts = annotate_heatmap(im, valfmt="{x:d}", threshold=210)

fig.tight_layout()
plt.savefig('../../imgs/simulation_giantvm_overcommit.pdf', dpi=300)
plt.show()
