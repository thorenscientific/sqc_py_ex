import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

# Initialize data arrays
Obs = []
sampsize = []

with open('Table6.4.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile, fieldnames=['num', 'defectives']) # Create reader object
    i = 0 #Counter
    for row in reader: # Read each row
        Obs.append(float(row['defectives']))
        i+=1

n = i # Find total number of obserrvations from length of array
print('Read in ' + str(n) + ' samples from data file')

cbar = np.average(Obs)
print('cbar: ' + str(cbar))

CUCL = cbar + 3.0*np.sqrt(cbar)
CLCL = cbar - 3.0*np.sqrt(cbar)

samplenum=np.arange(0, n, 1)
plt.figure(1)
plt.title("C control chart")
plt.xlabel("Sample")
plt.ylabel("Defectives")
plt.plot(samplenum, Obs, 'black') # Plot the data
plt.plot(samplenum, [cbar for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, [CUCL for i in range(n)], 'red') # Plot the UCL
plt.plot(samplenum, [CLCL for i in range(n)], 'red') # Plot the LCL

plt.show()


