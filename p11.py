def total_sum(*args):
    total = 0
    for num in args:
        total += num
    print("Total of given numbers:", total)

# Function call with different number of arguments
total_sum(10, 20, 30)
total_sum(5, 15)
total_sum(1, 2, 3, 4, 5)
