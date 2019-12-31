import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

# Initialize data arrays
Obs = []
sampsize = 5

with open('Table6.5.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile, fieldnames=['num', 'nonconformities']) # Create reader object
    i = 0 #Counter
    for row in reader: # Read each row
        Obs.append(float(row['nonconformities']))
        i+=1

n = i # Find total number of obserrvations from length of array
print('Read in ' + str(n) + ' samples from data file')

cibar = [0]*n
for i in range(n):
    cibar[i] = Obs[i] / sampsize

ubar = np.average(cibar)
print('ubar: ' + str(ubar))

uUCL = ubar + 3.0*np.sqrt(ubar/sampsize)
uLCL = ubar - 3.0*np.sqrt(ubar/sampsize)

samplenum=np.arange(0, n, 1)
plt.figure(1)
plt.title("u control chart")
plt.xlabel("Sample")
plt.ylabel("Defectives")
plt.plot(samplenum, cibar, 'black') # Plot the data
plt.plot(samplenum, [ubar for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, [uUCL for i in range(n)], 'red') # Plot the UCL
plt.plot(samplenum, [uLCL for i in range(n)], 'red') # Plot the LCL

plt.show()


