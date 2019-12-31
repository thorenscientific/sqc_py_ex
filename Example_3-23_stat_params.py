# Statistical parameters using NumPy and SciPy's stats module

# There are only a few data points so we will enter them manualy. For larger
# data sets, it is better to read data in from a separate file (CSV, etc.)

import numpy as np
from scipy import stats

salaries=[58, 63, 65, 68, 64, 66, 68, 72, 73, 79, 82, 83, 86, 88, 89]

mean=np.mean(salaries)
median=np.median(salaries)
mode=stats.mode(salaries)[0][0]
variance=np.var(salaries)
stdev=np.std(salaries)
# First quartile (Q1) 
q1 = np.percentile(salaries, 25, interpolation = 'midpoint') 
# Third quartile (Q3) 
q3 = np.percentile(salaries, 75, interpolation = 'midpoint') 
# Interquaritle range (IQR) 
iqr = q3 - q1

print("Salaries: " + str(salaries))
print("mean: " + str(mean))
print("median: " + str(median))
print("mode: " + str(mode))
print("variance: " + str(variance))
print("Standard Deviation: " + str(stdev))
print("Interquartile Range: " + str(iqr))