import numpy as np
import skfuzzy as fuzz

lines = [line for line in open('experimental01.csv').read().strip().split('\n')][1:]

estimations = [float((line.split(','))[6]) for line in lines]
precision = [float((line.split(','))[7]) for line in lines]

def crear_fuzzy_number(estimacion, precision):
  fuzzy_number = {
    "alpha": estimacion - precision,
    "beta": estimacion,
    "gamma": estimacion + precision
  }
  return fuzzy_number

fuzzy_numbers = []

for estimacion, precision in zip(estimations, precision):
  fuzzy_number = crear_fuzzy_number(estimacion, precision)
  fuzzy_numbers.append(fuzzy_number)

# def calcular_pertenencia(x, fuzzy_number):
#   alpha = fuzzy_number["alpha"]
#   beta = fuzzy_number["beta"]
#   gamma = fuzzy_number["gamma"]
  
#   grado_pertenencia = fuzz.trimf([alpha, beta, gamma], x)[0]
#   return grado_pertenencia

expected_value = 750

def media_fuzzy_numbers(fuzzy_numbers):
  alpha_values = np.mean([fuzzy_number["alpha"] for fuzzy_number in fuzzy_numbers])
  beta_values = np.mean([fuzzy_number["beta"] for fuzzy_number in fuzzy_numbers])
  gamma_values = np.mean([fuzzy_number["gamma"] for fuzzy_number in fuzzy_numbers])
  
  media_fuzzy_number = crear_fuzzy_number(beta_values, (beta_values - alpha_values)/2)
  return media_fuzzy_number

print(fuzzy_numbers)
mean = media_fuzzy_numbers(fuzzy_numbers)
numero = round(mean["beta"])
numero = min(numero, 750)
numero = max(numero, 0)
expected_value = 750
error_percentage = abs(numero - expected_value) / expected_value * 100
print(numero)
print(error_percentage)

tupla = [tuple(x.values()) for x in fuzzy_numbers]

