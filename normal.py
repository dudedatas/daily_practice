import random

population = [round(random.uniform(0,300), 4) for _ in range(10000)]

true_mu =  round(sum(population) / len(population), 4)

xbars = []


sample_size = range(1000)

for i in sample_size:

    sample = random.choices(population, k=100)
    x_bar = round(sum(sample) / len(sample), 4)
    xbars.append(x_bar)

avg_xbars = round(sum(xbars) / len(sample_size), 4)




print(true_mu, "\n")
print(avg_xbars)


