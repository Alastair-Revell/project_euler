# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from functools import reduce

print(reduce(lambda x, y: x*y, [1,2,3,4,5,7,9]))
