from scipy.stats import norm

mean = 18
stdev = 1.5
usl = 21
lsl = 15

total = norm.cdf(usl, mean, stdev) - norm.cdf(lsl, mean, stdev)
print(str(round(total * 100, 4)) + ' Percent') # Convert to percent