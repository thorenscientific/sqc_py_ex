# Based on Matplotlib example:
# https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html

# There are only a few data points so we will enter them manualy. For larger
# data sets, it is better to read data in from a separate file (CSV, etc.)

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['A', 'B', 'C', 'D', 'E']
plant_i = [14, 13, 9, 7, 7]
plant_ii = [12, 18, 12, 5, 8]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, plant_i, width, label='Plant I')
rects2 = ax.bar(x + width/2, plant_ii, width, label='Plant II')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Defects')
ax.set_xlabel('Defect Type')
ax.set_title('Defect Type by Plant')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()