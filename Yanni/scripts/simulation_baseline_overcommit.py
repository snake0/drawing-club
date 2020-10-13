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
    [144, 155, 166, 177, 193, 203, 215, 225, 232, 238],
    [143, 154, 167, 178, 187, 199, 210, 220, 228, 233],
    [145, 153, 164, 175, 188, 198, 206, 216, 221, 222],
    [142, 154, 163, 173, 185, 191, 200, 210, 214, 215],
    [144, 150, 161, 171, 180, 190, 197, 203, 206, 207],
    [142, 150, 160, 168, 180, 184, 191, 197, 202, 203],
    [138, 149, 158, 166, 173, 181, 190, 193, 193, 194],
    [141, 148, 158, 161, 171, 174, 181, 186, 186, 187],
    [137, 146, 153, 164, 164, 170, 179, 179, 182, 183],
    [137, 145, 150, 157, 162, 167, 173, 175, 175, 175],
    [135, 141, 149, 152, 159, 164, 167, 172, 172, 172],
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
plt.savefig('../../imgs/simulation_baseline_overcommit.pdf', dpi=300)
plt.show()
