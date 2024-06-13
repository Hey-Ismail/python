# --------------------#
# //* Sort() -->  the sort() function is a method that belongs to the list .
# sort() is a built-in method used to sort elements in a list in ascending order.
# It modifies the original list in place, meaning it reorders the elements directly within the list without creating a new list.
# The sort() method does not return any value; it simply sorts the list and updates it.


# list = [9, 7, 3, 2, 5, 67, 3, 8, 2, 7, 23, 12, 72, 1]
# tuple = (9, 7, 3, 2, 5, 67, 3, 8, 2, 7, 23, 12, 72, 1)

# list.sort()
# print(f"Sorted list :{list}")  # Ascending order

# sorted_tuple = sorted(tuple, reverse=True)  # descending order``
# print(f"Sorted tuple :{sorted_tuple}")

# words = ["Ismail", "Hossain", "Fahim"]
# words.sort()
# print(words)

# //*Sort with Custom Function Using Key
# List of student entries
students = (
    ("Ismail Hossain Fahim", "B+", 81),
    ("Sarah Ahmed", "A+", 92),
    ("John Doe", "B", 75),
    ("Emily Johnson", "D+", 62),
    ("Michael Brown", "C+", 69),
)

# When we do it with list
students.sort(key=lambda name: name[0])  # column
students.sort(key=lambda grade: grade[1])  # column
students.sort(key=lambda number: number[2])  # column

# When we do it with tuple
sorted_tuple = sorted(students, key=lambda name: name[0])
for i in sorted_tuple:
    print(i)
