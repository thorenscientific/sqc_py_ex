from scipy.stats import hypergeom

# Note that the symbols for M, n, N are not universally standardized.
# scipy's hypergeom uses:
# M for total population
# n for sample size
# N for sub-population of interest

defectives = hypergeom.pmf(k=[0,1,2,3,4,5], M=20, n=10, N=5)
for x in range(len(defectives)):
    print('X=' + str(x) + ': ' + str(round(defectives[x], 5)))
