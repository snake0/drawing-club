import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from color import *

diff_length_file_names = ["../diff_length/apache.txt",
    "../diff_length/build-gcc.txt", "../diff_length/openssl.txt",
    "../diff_length/Blowfish.txt", "../diff_length/MD5.txt",
    "../diff_length/povray.txt", "../diff_length/7zip.txt",
    "../diff_length/redis.txt",
    "../diff_length/phpbench.txt"]
diff_length_names = ["apache", "build", "openssl", "Blowfish",
    "MD5", "povray", "7zip", "redis", "php"]
diff_length_markers = ["s", "P", "", "", "", "", "", "", ""]
diff_length_color = [color_red, color_blue, color_green, color_indigo,
        color_dark_blue, color_yellow, color_purple, color_skyblue, color_pink]
bytes_sum_list = []

def parse_input(file_names):
    # Balabala {xxx}B:{yyy}
    diff_length_dict_list = []
    for n in file_names:
        # Bytes:number
        d = {}
        bytes_sum = 0
        with open(n) as fp:
            text = fp.read()
            text = text.split()
            for w in text:
                idx = w.find(":")
                if (idx > 0):
                    key = int(w[:idx-1])
                    value = int(w[idx+1:])
                    if (key in d.keys()):
                        d[key] = d[key] + value
                    else:
                        d[key] = value
                    bytes_sum += value
        diff_length_dict_list.append(d)
        bytes_sum_list.append(bytes_sum)
    return diff_length_dict_list

diff_length_dict_list = parse_input(diff_length_file_names)
# Data for plotting
# 0 cannot be depicted in a log-xscale plot
font_size = 35
font = {'size': font_size, 'family': 'HelveticaNeue', 'weight': 'medium'}
plt.rc('font', family='HelveticaNeue', weight='medium', size=font_size)
number_of_bytes = np.arange(1, 4098, 1)
fig, ax = plt.subplots()
fig.subplots_adjust(top=.95,bottom=.15,right=.95,left=.15)
fig.set_size_inches(10, 7.85)
lines = []
for i in range(len(diff_length_names)):
    number = []
    accum = 0
    for j in range(0, 4097):
        if (j in diff_length_dict_list[i].keys()):
            accum += diff_length_dict_list[i][j]
        number.append(accum * 1.0 / bytes_sum_list[i])
    lines.append(ax.plot(number_of_bytes,number,label=diff_length_names[i],
            color=diff_length_color[i]))

first_legend = ax.legend(handles=[l[0] for l in lines[:7]],loc="lower right",
        bbox_to_anchor=(1.02,-.012))
plt.gca().add_artist(first_legend)
ax.legend(handles=[l[0] for l in lines[7:]],loc="lower center",
        bbox_to_anchor=((.35,-.012)))

ax.set_xlabel('Number of distinguished bytes',fontdict=font)
ax.set_ylabel('CDF',fontdict=font)
ax.set_xscale("log")

ax.grid()

fig.savefig("../../imgs/diff_length.pdf")
