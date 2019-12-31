from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

percents = np.arange(1.0, 20.0, 1.0)
colors = ["black", "red", "blue", "green"]

def oc_curve(n, c):
    oc=[]
    for i in range(len(percents)):
        oc.append(binom.cdf(c, n, percents[i]/100.0))
    return oc

#Example 9.1(a)
ex_9_1_a_ocs = []
ns=[100, 75, 50, 25]
for n in ns:
    ex_9_1_a_ocs.append(oc_curve(n, 1))

plt.figure(1)
plt.title("OC, n=100, 75, 50, 25; c=1")
plt.xlabel("Defectives")
plt.ylabel("Prob. of Acceptance")
for curve in range(len(ex_9_1_a_ocs)):
    plt.plot(percents, ex_9_1_a_ocs[curve], color=colors[curve])
    
#Example 9.1(b)
ex_9_1_b_ocs = []
ns=[200, 100, 50]
cs=[4,2,1]
for i in range(0,3):
    ex_9_1_b_ocs.append(oc_curve(ns[i], cs[i]))

plt.figure(2)
plt.title("OC, n=200, c=4; n=100, c=2; n=50, c=1")
plt.xlabel("Defectives")
plt.ylabel("Prob. of Acceptance")
for curve in range(len(ex_9_1_b_ocs)):
    plt.plot(percents, ex_9_1_b_ocs[curve], color=colors[curve])

#Example 9.1(c)
ex_9_1_c_ocs = []
n=100
cs=[1,2,3]
for c in cs:
    ex_9_1_c_ocs.append(oc_curve(n, c))

plt.figure(3)
plt.title("OC, n=100, c=1,2,3")
plt.xlabel("Defectives")
plt.ylabel("Prob. of Acceptance")
for curve in range(len(ex_9_1_c_ocs)):
    plt.plot(percents, ex_9_1_c_ocs[curve], color=colors[curve])