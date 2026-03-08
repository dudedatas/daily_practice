import random
import math

numbers = []

for i in range(1000000):
    i = random.randrange(-1000,100)
    numbers.append(i)

x_bar = sum(numbers) / len(numbers)

residual = []
for i in numbers:
    i = (i - x_bar)**2
    residual.append(i)

residual_sum = sum(residual)
no_bessel = round(residual_sum / len(numbers), 4)
bessel = round(residual_sum / (len(numbers) - 1), 4)
print(f"Bessel: {bessel} | No Bessel: {no_bessel}")

mini_set = []
for i in range(10):
    i = random.choice(numbers)
    mini_set.append(i)

mini_xbar = sum(mini_set) / len(mini_set)

mini_residual = []
for i in mini_set:
    i = (i - mini_xbar)**2
    mini_residual.append(i)

mini_sum = sum(mini_residual)

mini_no_bessel = round( mini_sum/ len(mini_set), 4)
mini_bessel = round(mini_sum/ (len(mini_set) - 1), 4)

print(f"Mini Bessel: {mini_bessel} | Mini No Bessel: {mini_no_bessel}")



