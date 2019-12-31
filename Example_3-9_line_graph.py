# Line charats are fairly simple, see:
# https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html
# for some examples.

# There are only a few data points so we will enter them manualy. For larger
# data sets, it is better to read data in from a separate file (CSV, etc.)

import numpy as np
import matplotlib.pyplot as plt

month=np.arange(1, 13, 1) # start is inclusive, end is exclusive (hence 13)
vaccines=[40, 30, 21, 10, 5, 2, 3, 5, 25, 45, 43, 48]

plt.figure(1)
plt.title('line graph for Example 3.9')
plt.plot(month, vaccines)
plt.xlabel('month')
plt.ylabel('vaccines')
plt.show()