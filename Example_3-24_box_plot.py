# Box Plot using Matplotlib. See:
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html
# for details and examples

# There are only a few data points so we will enter them manualy. For larger
# data sets, it is better to read data in from a separate file (CSV, etc.)

import matplotlib.pyplot as plt

data = [85, 80, 88, 95, 115, 110, 105, 104, 89, 97, 96, 140, 75, 79, 99]

plt.figure()
plt.title('Box Plot for Example 3.24')
plt.ylabel('sound level (dB)')
plt.boxplot(data)