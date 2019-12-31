import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

known_mean = 15.0
known_stdev = 2.0
target = known_mean # Given. If target value is not given, use xbar 
m = 4 # Span, given

# Initialize data arrays
sample = []
boxcar = np.ones(m)/m

with open('Table7.4.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile) # Create reader object
    i = 0 #Counter
    for row in reader: # Read each row
        sample.append(float(row['Column_1']))
        i+=1

n = i # Find total number of obserrvations from length of array
print('Read in ' + str(n) + ' samples from data file')

xbar = np.average(sample)

# Perform moving average
MA = np.convolve(sample, boxcar)
MA = MA[0:n] # "trim" extra samples from the edge
for i in range(m-1): # Fix up the "edge effect"
    MA[i]*=m/(i+1)

UCL = [0]*n
LCL = [0]*n
for i in range(0,m-1):
    UCL[i] = target + 3*known_stdev/np.sqrt(i+1)
    LCL[i] = target - 3*known_stdev/np.sqrt(i+1)
for i in range(m-1,n):
    UCL[i] = target + 3*known_stdev/np.sqrt(m)
    LCL[i] = target - 3*known_stdev/np.sqrt(m)

starts = np.arange(0,n,1)
stops = starts + np.ones(n)
samplenum=np.arange(0, n, 1)

plt.figure(1)
plt.title("Moving Average control chart")
plt.xlabel("Sample")
plt.ylabel("Moving Average")
plt.plot(samplenum, [target for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, MA, 'green') # Plot the CL
plt.hlines(UCL,starts,stops, 'red') # Plot the UCL
plt.hlines(LCL,starts,stops, 'red') # Plot the LCL

plt.show()


