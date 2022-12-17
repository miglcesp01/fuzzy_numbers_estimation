import numpy as np
import skfuzzy as fuzz
from typing import Tuple, List

lines = [line for line in open('experimental02.csv').read().strip().split('\n')][1:]

from_values = [float((line.split(','))[6]) for line in lines]
to_values = [float((line.split(','))[7]) for line in lines]
precision = [float((line.split(','))[8]) for line in lines]

def create_fuzzy_number(lower: float, central: float, upper: float) -> Tuple[float, float, float]:
    return (lower, central, upper)

fuzzy_numbers = []
for i in range(len(to_values)):
    lower = from_values[i]
    central = to_values[i]
    upper = precision[i]
    fuzzy_number = create_fuzzy_number(lower, central, upper)
    fuzzy_numbers.append(fuzzy_number)

def mean2(fuzzy_numbers: List[Tuple[float, float, float]]) -> float:
    total = 0
    count = 0
    for fuzzy_number in fuzzy_numbers:
        total += fuzzy_number[1]  # add the central value of the fuzzy number
        count += 1
    return total / count
mean_value = mean2(fuzzy_numbers)
print(mean_value)

expected_value = 750
error_percentage = abs(mean_value - expected_value) / expected_value * 100
print(mean_value)
print(error_percentage)


