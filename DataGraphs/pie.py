import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'size': 20, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig = plt.figure()
fig.set_size_inches(4, 3.14)

fraction = [1.06, 0.97, 35.44, 43.75, 18.89]
labels = ["Router", "QEMU", "GuestOS", "DSM", "Others"]
explode = (0, 0, 0, 0.05, 0)
title = "Perf Result"
colors = ["#00BFBF", "#0000FF", "#BF00BF"]

pies = plt.pie(fraction, explode=explode, labels=labels,
               autopct='%1.1f%%', shadow=False, startangle=0,pctdistance=1.3)
for pie_wedge in pies[0]:
    pie_wedge.set_edgecolor('white')
plt.axis('equal') 
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
plt.gca().add_artist(centre_circle)
plt.title(title)
plt.tight_layout()
plt.savefig('perf-pie.pdf', dpi=300)
plt.show()
