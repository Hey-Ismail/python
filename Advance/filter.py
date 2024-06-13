# -----------------#
# //* Filter --> It goes through each item(list,tuple,set etc) and applies the rule.
# //* If the rule is true for an item, it keeps that item.
# //* If the rule is false, it discards the item.
# //* Finally, filter() gives you a new collection containing only the items that passed the test.

# Checking odd numbers
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(filter(lambda num: num % 2 != 0, number))
print(f"Odd numbers :{result}")

# Checking with statement
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

result = list(filter(lambda item: item[1]["marks"] > 80, students.items()))
result_names = [item[0] for item in result]
print(result_names)
