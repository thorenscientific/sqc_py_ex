import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

# Initialize data arrays
Samplenum=[] # Sample Number
Obs1s=[] # First observation for each sample
Obs2s=[] # Second observation for each sample
Obs3s=[] # Third observation for each sample
Obs4s=[] # Fourth observation for each sample


with open('Table5.4.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile) # Create reader object
    for row in reader: # Read each row
        if verbose == True:
            print(row['Column_1'], row['Column_2'], row['Column_3'], row['Column_4'])
#        Samplenum.append(float(row['Sample'])) # Append elements to data array
        Obs1s.append(float(row['Column_1']))
        Obs2s.append(float(row['Column_2']))
        Obs3s.append(float(row['Column_3']))
        Obs4s.append(float(row['Column_4']))

n = len(Obs1s) # Find total number of samples from length of array
print('Read in ' + str(n) + 'samples from data file')

samplenum=np.arange(1, n+1, 1)

Xi = []
Si = []

for i in range(0,len(Obs1s)):
    Xi.append(np.mean([Obs1s[i],Obs2s[i],Obs3s[i],Obs4s[i]]))
    Si.append(np.std([Obs1s[i],Obs2s[i],Obs3s[i],Obs4s[i]]))

Xbarbar = np.mean(Xi)
Sbar = np.mean(Si)
print('Xbar-bar: ' + str(Xbarbar))
print('Sbar: ' + str(Sbar))

# Parameters from table of Control Chart Factors

A3 = 1.6281
B3 = 0
B4 = 2.2660


XbUCL = Xbarbar + A3 * Sbar
XbLCL = Xbarbar - A3 * Sbar

RbUCL = B4 * Sbar
RbLCL = B3 * Sbar

plt.figure(1)
plt.title("X-bar chart")
plt.xlabel("Sample")
plt.ylabel("Sample Mean")
plt.plot(samplenum, Xi, 'black') # Plot the data
plt.plot(samplenum, [Xbarbar for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, [XbUCL for i in range(n)], 'red') # Plot the UCL
plt.plot(samplenum, [XbLCL for i in range(n)], 'red') # Plot the LCL
        
plt.show()

plt.figure(2)
plt.title("S chart")
plt.xlabel("Sample")
plt.ylabel("Sample Range")
plt.plot(samplenum, Si, 'black') # Plot the data
plt.plot(samplenum, [Sbar for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, [RbUCL for i in range(n)], 'red') # Plot the UCL
plt.plot(samplenum, [RbLCL for i in range(n)], 'red') # Plot the LCL
plt.show()
