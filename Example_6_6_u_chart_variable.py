import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

# Initialize data arrays
Obs = []
sampsize = []

with open('Table6.6.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile, fieldnames=['num', 'sampsize', 'nonconformities']) # Create reader object
    i = 0 #Counter
    for row in reader: # Read each row
        Obs.append(float(row['nonconformities']))
        sampsize.append(float(row['sampsize']))
        i+=1

n = i # Find total number of obserrvations from length of array
print('Read in ' + str(n) + ' samples from data file')

ui = [0]*n
for i in range(n):
    ui[i] = Obs[i] / sampsize[i]

ubar = np.sum(Obs) / np.sum(sampsize)
print('ubar: ' + str(ubar))

uUCL = [0]*n
uLCL = [0]*n

for i in range(n):
    uUCL[i] = ubar + 3.0*np.sqrt(ubar/sampsize[i])
    uLCL[i] = ubar - 3.0*np.sqrt(ubar/sampsize[i])

starts = np.arange(0,n,1)
stops = starts + np.ones(n)
samplenum=np.arange(0, n, 1)

plt.figure(1)
plt.title("u control chart")
plt.xlabel("Sample")
plt.ylabel("Defectives")
plt.plot(samplenum, ui, 'black') # Plot the data
plt.plot(samplenum, [ubar for i in range(n)], 'green') # Plot the CL
plt.hlines(uUCL,starts,stops, 'red') # Plot the UCL
plt.hlines(uLCL,starts,stops, 'red') # Plot the LCL

plt.show()


