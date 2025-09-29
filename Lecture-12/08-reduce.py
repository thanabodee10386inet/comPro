from functools import reduce

nubers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, nubers)
print(sum_of_numbers)