import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

known_mean = 15.0
known_stdev = 2.0
target = known_mean # Given. If target value is not given, use xbar 
lmbda = .20 # Given
L = 2.962 # Given

# Initialize data arrays
sample = []

with open('Table7.4.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile) # Create reader object
    i = 0 #Counter
    for row in reader: # Read each row
        sample.append(float(row['Column_1']))
        i+=1

n = i # Find total number of obserrvations from length of array
print('Read in ' + str(n) + ' samples from data file')

xbar = np.average(sample)

EWMA = [0]*n
# Perform moving average
EWMA[0] = lmbda*sample[0] + (1-lmbda)*target
for i in range(1,n): # Fix up the "edge effect"
    EWMA[i] = lmbda*sample[i] + (1-lmbda)*EWMA[i-1]

UCL = [0]*n
LCL = [0]*n

def cl_factor(x):
    return np.sqrt((lmbda/(2-lmbda))*(1-(1-lmbda)**(2*x)))

for i in range(0,n):
    UCL[i] = target + L * known_stdev*cl_factor(i)
    LCL[i] = target - L * known_stdev*cl_factor(i)

starts = np.arange(0,n,1)
stops = starts + np.ones(n)
samplenum=np.arange(0, n, 1)

plt.figure(1)
plt.title("Moving Average control chart")
plt.xlabel("Sample")
plt.ylabel("Moving Average")
plt.plot(samplenum, [target for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, EWMA, 'green') # Plot the CL
plt.hlines(UCL,starts,stops, 'red') # Plot the UCL
plt.hlines(LCL,starts,stops, 'red') # Plot the LCL

plt.show()


