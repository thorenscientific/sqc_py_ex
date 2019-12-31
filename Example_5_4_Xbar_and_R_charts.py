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
Ri = []

for i in range(0,len(Obs1s)):
    Xi.append(np.mean([Obs1s[i],Obs2s[i],Obs3s[i],Obs4s[i]]))
    Ri.append(np.max([Obs1s[i],Obs2s[i],Obs3s[i],Obs4s[i]]) -
              np.min([Obs1s[i],Obs2s[i],Obs3s[i],Obs4s[i]]))

Xbarbar = np.mean(Xi)
Rbar = np.mean(Ri)
print('Xbar-bar: ' + str(Xbarbar))
print('Rbar: ' + str(Rbar))

# Parameters from table of Control Chart Factors
A2 = 0.72851
D3 = 0.0 
D4 = 2.28218

XbUCL = Xbarbar + A2 * Rbar
XbLCL = Xbarbar - A2 * Rbar

RbUCL = D4 * Rbar
RbLCL = D3 * Rbar

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
plt.title("R chart")
plt.xlabel("Sample")
plt.ylabel("Sample Range")
plt.plot(samplenum, Ri, 'black') # Plot the data
plt.plot(samplenum, [Rbar for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, [RbUCL for i in range(n)], 'red') # Plot the UCL
plt.plot(samplenum, [RbLCL for i in range(n)], 'red') # Plot the LCL
plt.show()
