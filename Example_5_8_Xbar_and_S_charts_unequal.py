import csv # Import Comma-Separated Variable library
import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import plotting library
verbose = True

colnames=['Column_2', 'Column_3', 'Column_4', 'Column_5', 'Column_6',
         'Column_7', 'Column_8', 'Column_9', 'Column_10', 'Column_11', ]
# Initialize data arrays
Samplenum=[] # Sample Number
NumObs=[]
Obs = []

with open('Table5.6.csv', newline='') as csvfile: # Open data file
    reader = csv.DictReader(csvfile) # Create reader object
    i = 0 #Counter
    for row in reader: # Read each row
        Obs.append([])
        NumObs.append(int(row['Column_1']))
        for k in range (NumObs[i]):
            Obs[i].append(float(row[colnames[k]]))
        i+=1

n = i # Find total number of samples from length of array
print('Read in ' + str(n) + ' samples from data file')

samplenum=np.arange(0, n, 1)

Xi = []
Si = []
Sbarsq = 0
TotalObs = sum(NumObs)
for i in range(0,n):
    Xi.append(np.mean(Obs[i]))
    Si.append(np.std(Obs[i],ddof=1))
    Sbarsq += ((NumObs[i]-1)*(Si[i]**2))/(TotalObs-n)

Sbar=np.sqrt(Sbarsq)
Xbarbar = np.mean(Xi)

print('Xbar-bar: ' + str(Xbarbar))
print('Sbar: ' + str(Sbar))

# Parameters from table of Control Chart Factors, n
A3 = 1.6281
B3 = 0
B4 = 2.2660

XbUCL=[0]*n
XbLCL=[0]*n
SbUCL=[0]*n
SbLCL=[0]*n
for i in range(n):
    XbUCL[i] = Xbarbar + A3 * Si[i]
    XbLCL[i] = Xbarbar - A3 * Si[i]
    SbUCL[i] = Sbar + B4 * Si[i]
    SbLCL[i] = Sbar - B3 * Si[i]
starts = np.arange(0,n,1)
stops = starts + np.ones(n)

plt.figure(1)
plt.title("X-bar chart")
plt.xlabel("Sample")
plt.ylabel("Sample Mean")
plt.plot(samplenum, Xi, 'black') # Plot the data
plt.plot(samplenum, [Xbarbar for i in range(n)], 'green') # Plot the CL
plt.hlines(XbUCL,starts,stops, colors='red') # Plot the UCL
plt.hlines(XbLCL,starts,stops, colors='red') # Plot the LCL
        
plt.show()

plt.figure(2)
plt.title("S chart")
plt.xlabel("Sample")
plt.ylabel("Sample Range")
plt.plot(samplenum, Si, 'black') # Plot the data
plt.plot(samplenum, [Sbar for i in range(n)], 'green') # Plot the CL
plt.hlines(SbUCL,starts,stops, 'red') # Plot the UCL
plt.hlines(SbLCL,starts,stops, 'red') # Plot the LCL
plt.show()
