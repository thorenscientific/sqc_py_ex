# Scatter plots are fairly simple, see:
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
# for details.

# There are only a few data points so we will enter them manualy. For larger
# data sets, it is better to read data in from a separate file (CSV, etc.)

import matplotlib.pyplot as plt

cholesterol=[195, 180, 220, 160, 200, 220, 200, 183, 139, 155,
             153, 164, 171, 143, 159, 167, 162, 165, 178, 145,
             245, 198, 156, 175, 171, 167, 142, 187, 158, 142]

systolic=[130, 128, 138, 122, 140, 148, 142, 127, 116, 123,
          119, 130, 128, 120, 121, 124, 118, 121, 124, 115,
          145, 126, 122, 124, 117, 122, 112, 131, 122, 120]

plt.figure(1)
plt.title('Scatter Plot for Example 3.10')
plt.scatter(cholesterol, systolic)
plt.xlabel('Cholesterol')
plt.ylabel('Systolic Pressure')
plt.show()