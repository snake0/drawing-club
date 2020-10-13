import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font_size=28
font = {'size': font_size,}
plt.rc('font', family='Helvetica Neue', weight='medium')

# font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
# plt.rc('font', family='Helvetica Neue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(10, 7.85)
plt.subplots_adjust(top=0.95, right=0.95)
x = ["Word Count", "Inverted Index"]

xrange = np.arange(len(x))
giantvm = [24.313, 26.083]
inverted_index = [60 + 25.134, 60 + 16.020]

title = "Text-Processing"
colors = ["#bcdfba", "#3b7cb1"]
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['///', '\\\\\\', '----', '//////',
           '++++', 'xxxxxx', '\\\\\\\\\\\\', '----']

bar_width = 0.25
bar_interval = 0.1
bar_zoom = 0.8
linewidth = 4

ax.set_title(title,fontdict=font)

plt.xticks(xrange, x)
ax.set_ylabel("Time (s)", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=font_size)
ax.set_ylim([0, 100])
#ax.set_xlabel("Program", fontdict=font)

for i in xrange:
    giantvm_bar = ax.bar(i - bar_interval, giantvm[i], width=bar_width * bar_zoom,
                          bottom=0, color=colors[0], edgecolor="black",
                          label="GiantVM")
    spark_bar = ax.bar(i + bar_interval, inverted_index[i], width=bar_width * bar_zoom,
                       bottom=0, color=colors[1], edgecolor="black",
                       label="Spark")

ax.legend((giantvm_bar, spark_bar),
          ("GiantVM", "Spark"),
          loc=0, prop={'size': font_size}, frameon=False)

plt.grid(False)
#plt.tight_layout()
plt.savefig('spark-app.pdf', dpi=300)
plt.show()
