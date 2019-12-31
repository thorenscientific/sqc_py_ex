import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

# Initialize data arrays
Obs = []
sampsize = 900 # Given, sample size for each observation

with open('Table6.2.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile, fieldnames=['Column_1']) # Create reader object
    i = 0 #Counter
    for row in reader: # Read each row
        Obs.append(float(row['Column_1']))
        i+=1

n = i # Find total number of obserrvations from length of array
print('Read in ' + str(n) + ' samples from data file')

Pbar = np.average(Obs)/sampsize

print('Pbar: ' + str(Pbar))

PUCL=sampsize*Pbar+3.0*np.sqrt((sampsize*Pbar*(1.0-Pbar)))

PLCL=sampsize*Pbar-3.0*np.sqrt((sampsize*Pbar*(1.0-Pbar)))
if PLCL < 0.0:
    PLCL = 0.0

samplenum=np.arange(0, n, 1)
plt.figure(1)
plt.title("P control chart")
plt.xlabel("Sample")
plt.ylabel("Proportion")
plt.plot(samplenum, Obs, 'black') # Plot the data
plt.plot(samplenum, [sampsize*Pbar for i in range(n)], 'green') # Plot the CL
plt.plot(samplenum, [PUCL for i in range(n)], 'red') # Plot the UCL
plt.plot(samplenum, [PLCL for i in range(n)], 'red') # Plot the LCL

    
plt.show()


