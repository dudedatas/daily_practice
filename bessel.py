import random

#population
population = [random.randrange(-1000,1000) for _ in range(100000)]

#true mean/variance

mu = sum(population) / len(population)
vars = sum(((x - mu)**2 for x in population))
true_variance = round(vars / len(population), 4)


no_bessel_total = 0
bessel_total = 0

for _ in range(1000):

    sample = random.choices(population, k=100)
    xbar = sum(sample) / len(sample)
    s = sum(((x - xbar)**2 for x in sample ))
    sample_var = s / len(sample)

    no_bessel_total += sample_var / len(sample)
    bessel_total += sample_var / (len(sample) - 1)

average_bessel = bessel_total / 100
average_no_bessel = no_bessel_total / 100


print("True variance:", round(true_variance, 4))
print("Average variance without Correction (divide by n): ", round(average_no_bessel, 4))
print("Average variance wirh Correction (divide by n-1): ", round(average_bessel, 4))