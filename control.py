import fuzzy
lines = [lines for lines in open('control.csv').read().splitlines()][1:]

control_values = [float(x.split(",")[-3]) for x in lines]
mean = sum(control_values)/len(control_values)
print(mean)
print(fuzzy.error(750, mean))