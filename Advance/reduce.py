# ----------------#
# //* Reduce ()--> Returns the single value you get after combining everything in your pile using the function you provided.
# It applies the function you provided to these two items, giving you a single result.
# Then, it takes that result and combines it with the third item in your pile using the same function.
# This process continues, iteratively combining the results with the next item in the pile until there's only one item left.

# from functools import reduce
import functools

list = [1, 3, 5, 6, 7, 5, 4, 3, 2, 0]
summation = functools.reduce(lambda x, y: x + y, list)
print(f"Sum of the list is :", end="")
print(summation)

# //* reduce() vs accumulate()
# reduce() is defined in “functools” module, accumulate() in “itertools” module.
# reduce() stores the intermediate result and only returns the final summation value.
# Whereas, accumulate() returns a iterator containing the intermediate results.
# The last number of the iterator returned is summation value of the list.
# reduce(fun, seq) takes function as 1st and sequence as 2nd argument.
# In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.

import itertools  # for accumulate()
import functools  # for reduce()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result_acc = list(itertools.accumulate(numbers, lambda x, y: x + y))
result_red = functools.reduce(lambda x, y: x + y, numbers)
print(f"The summation of list using accumulate is\n-->{result_acc}", end="")
print("\n")
print(f"The summation of list using reduce is\n-->{result_red}", end="")
