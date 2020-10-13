import numpy as np
from numpy import random
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams

import seaborn as sns
sns.set(font_scale=0.8)

R1 = np.loadtxt(open("./data/heatmap1.csv","rb"),delimiter=",",skiprows=1)
R2 = np.loadtxt(open("./data/heatmap2.csv","rb"),delimiter=",",skiprows=1)
R3 = np.loadtxt(open("./data/heatmap3.csv","rb"),delimiter=",",skiprows=1)
R4 = np.loadtxt(open("./data/heatmap4.csv","rb"),delimiter=",",skiprows=1)
R5 = np.loadtxt(open("./data/heatmap5.csv","rb"),delimiter=",",skiprows=1)
R6 = np.loadtxt(open("./data/heatmap6.csv","rb"),delimiter=",",skiprows=1)
R7 = np.loadtxt(open("./data/heatmap7.csv","rb"),delimiter=",",skiprows=1)
R8 = np.loadtxt(open("./data/heatmap8.csv","rb"),delimiter=",",skiprows=1)

R1 = np.log2(R1 + 1)
R2 = np.log2(R2 + 1)
R3 = np.log2(R3 + 1)
R4 = np.log2(R4 + 1)
R5 = np.log2(R5 + 1)
R6 = np.log2(R6 + 1)
R7 = np.log2(R7 + 1)
R8 = np.log2(R8 + 1)

fig = plt.figure(figsize=(12, 5.3))

# change font
my_font = fm.FontProperties(fname="./fonts/Hel.ttf", size=9)
sub_font = fm.FontProperties(fname="./fonts/Hel.ttf", size=9)
plt.legend(loc='best', prop=my_font)

# plt.subplots_adjust(hspace=0.5, wspace=0.3)

plt.subplot(241)
sns_plot1 = sns.heatmap(R1, xticklabels=2, yticklabels=2, vmax=7, cmap="YlGnBu", square=True)
for xitem in sns_plot1.get_xticklabels():
    xitem.set_rotation(90)
    xitem.set_fontsize(7)
for yitem in sns_plot1.get_yticklabels():
    yitem.set_rotation(0)
    yitem.set_fontsize(7)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('(a) BT', fontproperties=my_font, y=-0.1)


plt.subplot(242)
sns_plot2 = sns.heatmap(R2, xticklabels=2, yticklabels=2, vmax=7, cmap="YlGnBu", square=True)
for xitem in sns_plot2.get_xticklabels():
    xitem.set_rotation(90)
    xitem.set_fontsize(7)
for yitem in sns_plot2.get_yticklabels():
    yitem.set_rotation(0)
    yitem.set_fontsize(7)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('(b) CG', fontproperties=my_font)


plt.subplot(243)
sns_plot3 = sns.heatmap(R3, xticklabels=2, yticklabels=2, vmax=7, cmap="YlGnBu", square=True)
for xitem in sns_plot3.get_xticklabels():
    xitem.set_rotation(90)
    xitem.set_fontsize(7)
for yitem in sns_plot3.get_yticklabels():
    yitem.set_rotation(0)
    yitem.set_fontsize(7)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('(c) EP', fontproperties=my_font)


plt.subplot(244)
sns_plot4 = sns.heatmap(R4, xticklabels=2, yticklabels=2, vmax=7, cmap="YlGnBu", square=True)
for xitem in sns_plot4.get_xticklabels():
    xitem.set_rotation(90)
    xitem.set_fontsize(7)
for yitem in sns_plot4.get_yticklabels():
    yitem.set_rotation(0)
    yitem.set_fontsize(7)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('(d) MG', fontproperties=my_font)


plt.subplot(245)
sns_plot5 = sns.heatmap(R5, xticklabels=2, yticklabels=2, vmax=7, cmap="YlGnBu", square=True)
for xitem in sns_plot5.get_xticklabels():
    xitem.set_rotation(90)
    xitem.set_fontsize(7)
for yitem in sns_plot5.get_yticklabels():
    yitem.set_rotation(0)
    yitem.set_fontsize(7)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('(e) SP', fontproperties=my_font)


plt.subplot(246)
sns_plot6 = sns.heatmap(R6, xticklabels=2, yticklabels=2, vmax=7, cmap="YlGnBu", square=True)
for xitem in sns_plot6.get_xticklabels():
    xitem.set_rotation(90)
    xitem.set_fontsize(7)
for yitem in sns_plot6.get_yticklabels():
    yitem.set_rotation(0)
    yitem.set_fontsize(7)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('(f) FT', fontproperties=my_font)


plt.subplot(247)
sns_plot7 = sns.heatmap(R7, xticklabels=2, yticklabels=2, vmax=7, cmap="YlGnBu", square=True)
for xitem in sns_plot7.get_xticklabels():
    xitem.set_rotation(90)
    xitem.set_fontsize(7)
for yitem in sns_plot7.get_yticklabels():
    yitem.set_rotation(0)
    yitem.set_fontsize(7)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('(g) IS', fontproperties=my_font)


plt.subplot(248)
sns_plot8 = sns.heatmap(R8, xticklabels=2, yticklabels=2, vmax=7, cmap="YlGnBu", square=True)
for xitem in sns_plot8.get_xticklabels():
    xitem.set_rotation(90)
    xitem.set_fontsize(7)
for yitem in sns_plot8.get_yticklabels():
    yitem.set_rotation(0)
    yitem.set_fontsize(7)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('(h) Sysbench', fontproperties=my_font)


fig.savefig("heatmapv3.pdf", bbox_inches='tight') # 减少边缘空白
plt.show()