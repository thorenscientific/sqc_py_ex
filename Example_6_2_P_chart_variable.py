import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

# Initialize data arrays
Obs = []
sampsize = []

with open('Table6.3.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile, fieldnames=['defects', 'sampsize']) # Create reader object
    i = 0 #Counter
    for row in reader: # Read each row
        Obs.append(float(row['defects']))
        sampsize.append(float(row['sampsize']))
        i+=1

n = i # Find total number of obserrvations from length of array
print('Read in ' + str(n) + ' samples from data file')

Pi = [0]*n
for i in range(0,n):
    Pi[i] = (Obs[i]/sampsize[i])
Pbar = np.average(Pi)
print('Pbar: ' + str(Pbar))

#Calculate LCL, UCL
PLCL=[0]*n
PUCL=[0]*n
for i in range(0,n):
    PUCL[i] = Pbar+3.0*np.sqrt((Pbar*(1.0-Pbar))/(sampsize[i]))
    PLCL[i] = Pbar-3.0*np.sqrt((Pbar*(1.0-Pbar))/(sampsize[i]))
    if PLCL[i] < 0.0:
        PLCL[i] = 0.0

starts = np.arange(0,n,1)
stops = starts + np.ones(n)

samplenum=np.arange(0, n, 1)
plt.figure(1)
plt.title("P control chart")
plt.xlabel("Sample")
plt.ylabel("Proportion")
plt.plot(samplenum, Pi, 'black') # Plot the data
plt.plot(samplenum, [Pbar for i in range(n)], 'green') # Plot the CL
plt.hlines(PUCL,starts,stops, colors='red') # Plot the UCL
plt.hlines(PUCL,starts,stops, colors='red') # Plot the LCL

    
plt.show()


