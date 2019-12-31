# Based on Matplotlib example:
# https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/bar_stacked.html

# There are only a few data points so we will enter them manualy. For larger
# data sets, it is better to read data in from a separate file (CSV, etc.)

import numpy as np
import matplotlib.pyplot as plt

N = 6
newhires = (128, 245, 130, 154, 152, 165)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, newhires, width)

plt.ylabel('Hires')
plt.xlabel('Year')
plt.title('New Hires, 2014 to 2019')
plt.xticks(ind, ('2014', '2015', '2016', '2017', '2018', '2019'))
plt.yticks(np.arange(100, 300, 50))

plt.show()