# Based on Matplotlib example:
# https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html

# There are only a few data points so we will enter them manualy. For larger
# data sets, it is better to read data in from a separate file (CSV, etc.)

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x=[72, 88, 65, 68, 68, 75, 87, 79, 89, 79,
   65, 76, 81, 84, 67, 82, 61, 89, 85, 90,
   67, 68, 82, 85, 79, 65, 79, 74, 81, 82]

mu = np.average(x)
sigma = np.std(x)

bins = 6 # Experiment with the number of bins for best visualization
# the histogram of the data
n, bins, patches = plt.hist(x, bins, normed=0, facecolor='green', alpha=0.75)
# Set normed to 1 to normalize to construct a relative frequency histogram.

plt.xlabel('Number of Fuel Pumps')
plt.ylabel('Frequency')
plt.title('Histogram for the Data in Example 3.8')

plt.axis([60, 95, 0, 10])
plt.grid(True)

plt.show()