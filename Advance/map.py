# --------------#
# //* map function --> syntax - map(function, iteration) ,returns an iteration that applies function to every time of iterable


# Return double of n
def calculation(x):
    return x * x


# We double all numbers using map()
number = [1, 2, 3, 4, 5]
result = map(calculation, number)
print(list(result))

# map() with lambda expressions
number = (1, 2, 3, 4, 5)
result = map(lambda x: x * x, number)
print(list(result))  # output will be same


# if Statement with map()
def even(num):
    if num % 2 == 0:
        return num
    else:
        return num + 1


try:
    # getting user input
    user_input = input('Enter a series of numbers "separated by spaces"\n--> ')

    # Convert the input string into a list of integers
    numbers = list(map(int, user_input.split()))

    # Process the numbers to ensure they are all even
    result = map(even, numbers)
    print(list(result))  # return as a list

except ValueError:
    print("input is not matched.pls give numerical value")
