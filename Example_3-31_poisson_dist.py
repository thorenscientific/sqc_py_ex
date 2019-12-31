from scipy.stats import poisson
accident_prob = poisson.pmf(5, 2)
print('Accident Probability: ' + str(round(accident_prob, 5)))