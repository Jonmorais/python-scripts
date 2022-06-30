# number = int(input("Type the number and I will return his factorial!\n"))
# result = 1
# for n in range(1, number + 1):
#   result *= n
  
# print(result)

# Using library and list comprehension

import math

number = int(input("Type the number and I will return a list with every factorial until your given number!!\n"))

factor = [math.factorial(n) for n in range(1, number + 1)]

print(f'\n{list(enumerate(factor, start=1))}\n')
