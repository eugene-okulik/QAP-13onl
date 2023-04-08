import random
import statistics

array = []
for i in range(1, 16):
    number = random.random()
    array.append(number)
print('List of the generated numbers:', array)
print('The greatest generated number:', max(array))
print('The smaller generated number:', min(array))
print('The sum of the numbers in the array:', sum(array))
print('The average of the array:', statistics.mean(array))
