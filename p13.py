from functools import reduce

# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() with lambda: square of each number
squares = list(map(lambda x: x * x, numbers))
print("Squares using map():", squares)

# filter() with lambda: select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)

# reduce() with lambda: sum of all numbers
total_sum = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce():", total_sum)
