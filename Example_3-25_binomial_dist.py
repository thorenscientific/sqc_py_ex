from scipy.stats import binom
success = binom.pmf(k=[0,1,2,3,4,5], n=5, p=0.8)
for x in range(len(success)):
    print('X=' + str(x) + ': ' + str(round(success[x], 5)))
