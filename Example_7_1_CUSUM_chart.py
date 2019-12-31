import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

# Initialize data arrays
sample = []
sampsize = 4
known_mean = 15.0
known_stdev = 2.0
r = 1 # r is the value of the mean shift in unites of known standard deviation
target = known_mean + r * known_stdev
k = (target-known_mean)/(2*known_stdev) # reference value
h = 5 # decision interval

with open('Table7.1.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile, fieldnames=['o1', 'o2', 'o3', 'o4']) # Create reader object
    i = 0 #Counter
    for row in reader: # Read each row
        sample.append([float(row['o1']),float(row['o2']),float(row['o3']),float(row['o4'])])
        i+=1

n = i # Find total number of obserrvations from length of array
print('Read in ' + str(n) + ' samples from data file')

xbar = [0]*n
zbar = [0]*n
sp = [0]*n
sm = [0]*n
       
for i in range(0,n):
    xbar[i] = np.average(sample[i])
    zbar[i] = (xbar[i] - known_mean)/(known_stdev/np.sqrt(sampsize))
    if i != 0:
        sp[i] = max((0.0, zbar[i] - k + sp[i-1]))
        sm[i] = min((0.0, zbar[i] + k + sm[i-1]))

#Calculate LCL, UCL
LCL = -1.0*h
UCL = h

samplenum=np.arange(0, n, 1)
plt.figure(1)
plt.title("CUSUM chart")
plt.xlabel("Sample")
plt.ylabel("Cumulative Sum")
plt.plot(samplenum, sp, 'black') # Plot the data
plt.plot(samplenum, sm, 'black') # Plot the data

plt.plot(samplenum, [0.0 for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, [UCL for i in range(n)], 'red') # Plot the UCL
plt.plot(samplenum, [LCL for i in range(n)], 'red') # Plot the LCL

plt.show()

print('CUSUM table')
print('Sample Number, SI+, SI-')
for i in range(0,n):
    print(str(i) + ',' + str(sp[i]) + ',' + str(sm[i]))
