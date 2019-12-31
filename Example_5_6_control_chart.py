import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

# Initialize data arrays
Samplenum=[] # Sample Number
Observations=[] # First observation for each sample
MRk=[]


with open('Table5.5.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile) # Create reader object
    for row in reader: # Read each row
        if verbose == True:
            print(row['Column_1'])
        Observations.append(float(row['Column_1']))

n = len(Observations) # Find total number of samples from length of array
print('Read in ' + str(n) + 'samples from data file')

samplenum=np.arange(1, n+1, 1)

for i in range(1, n):
    MRk.append(abs(Observations[i-1] - Observations[i]))



Xbar = np.mean(Observations)
Rbar = np.mean(MRk)
print('Xbar: ' + str(Xbar))
print('Rbar: ' + str(Rbar))

# Parameters from table of Control Chart Factors
D2 = 1.128
D3 = 0.0 
D4 = 3.26862

XbUCL = Xbar + (3.0/D2) * Rbar
XbLCL = Xbar - (3.0/D2) * Rbar

RbUCL = D4 * Rbar
RbLCL = D3 * Rbar

plt.figure(1)
plt.title("X chart")
plt.xlabel("Observation")
plt.ylabel("Individual Value")
plt.plot(samplenum, Observations, 'black') # Plot the data
plt.plot(samplenum, [Xbar for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, [XbUCL for i in range(n)], 'red') # Plot the UCL
plt.plot(samplenum, [XbLCL for i in range(n)], 'red') # Plot the LCL
        
plt.show()

plt.figure(2)
plt.title("MR chart")
plt.xlabel("Observation")
plt.ylabel("Moving Range")
plt.plot(samplenum[1:], MRk, 'black') # Plot the data
plt.plot(samplenum[1:], [Rbar for i in range(n-1)], 'green') # Plot the CL
plt.plot(samplenum[1:], [RbUCL for i in range(n-1)], 'red') # Plot the UCL
plt.plot(samplenum[1:], [RbLCL for i in range(n-1)], 'red') # Plot the LCL
plt.show()
