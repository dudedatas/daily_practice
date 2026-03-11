import random

population = [round(random.uniform(0,300), 4) for _ in range(10000)]

true_mu = sum(population) / len(population)

xbars = []


simulation_size = range(10000)

for _ in simulation_size:

    sample_size = random.choices(population, k=100)
    x_bar = round(sum(sample_size) / len(sample_size), 4)
    xbars.append(x_bar)

avg_xbars = round(sum(xbars) / len(simulation_size), 4)


print("True:", round(true_mu, 4), "\n")
print("AVGs:", avg_xbars)


