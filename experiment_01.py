import functools
import numpy as np
from matplotlib import pyplot as plt
import fuzzy

lines = [line for line in open('experimental01.csv').read().strip().split('\n')][1:]

estimations = [float((line.split(','))[6]) for line in lines]
precisions = [float((line.split(','))[7]) for line in lines]

def create_fuzzy_numbers(estimations, precisions, range=40):
  fuzzy_numbers = []
  for estimation, prec in zip(estimations, precisions):
    fuzzy_numbers.append((estimation-range,estimation,estimation,estimation+range))
  return fuzzy_numbers

def sum_fuzzy_number(fn1, fn2):
  return tuple([fn1[i]+fn2[i] for i in range(len(fn1))])

def fuzzy_numbers_mean():
  fuzzy_numbers = create_fuzzy_numbers(estimations, precisions)
  sum = functools.reduce(lambda fuzzy_number, acc: sum_fuzzy_number(fuzzy_number, acc), fuzzy_numbers, (0,0,0,0))
  return [i/len(fuzzy_numbers) for i in sum]

fuzzy_mean = fuzzy_numbers_mean()
print(fuzzy_mean)
x = np.linspace(0,1000,1001,endpoint=True)
m = fuzzy.trapmf(x,fuzzy_mean)
plt.plot(x,m)
plt.savefig('Figure_4.png')

print("Si xtest=", 750, " m(x)=",fuzzy.trapmf(750,fuzzy_mean))
print("El error es de: ", fuzzy.error(750, fuzzy_mean[1]))