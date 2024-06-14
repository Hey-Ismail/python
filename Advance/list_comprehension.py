# -----------#
# //*List Comprehension --> Syntax: newList = [ expression(element) for element in oldList if condition ]
# //*                       Syntax: newList =[ expression(element) if/else for element in oldList ]
# Parameter:
# expression: Represents the operation you want to execute on every item within the iterable.
# element: The term “variable” refers to each value taken from the iterable.
# iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
# condition: (Optional) A filter helps decide whether or not an element should be added to the new list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

square = [x**2 for x in numbers]
print("The square of the list :", square)

even = [i for i in numbers if i % 2 == 0]
print("The even of the list :", even)

# statement
students = {
    "Zayan": {"marks": 85, "grade": "B+"},
    "Salman": {"marks": 92, "grade": "A+"},
    "Shahzain": {"marks": 75, "grade": "C+"},
    "Ali Hossain": {"marks": 90, "grade": "A"},
    "Zain Khan": {"marks": 55, "grade": "D"},
    "Nizamuddin": {"marks": 65, "grade": "D+"},
    "Abdul Ahad": {"marks": 71, "grade": "C"},
    "Ubaidullah": {"marks": 79, "grade": "B"},
    "Habibullah": {"marks": 95, "grade": "A+"},
    "Nasiruddin": {"marks": 92, "grade": "A"},
}

passed_students = [
    name if info["marks"] >= 70 else "Failed" for name, info in students.items()
]
print(f"Passed students are: {passed_students}")
