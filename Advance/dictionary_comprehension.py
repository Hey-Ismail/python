# -----------------#
# //* Dictionary comprehension --> Create a dictionaries using an expression
# //* Syntaxes --> {key: (expression) for (key,value) in iterable if conditional}
# //*          --> {key: (if/else) for (key,value) in iterable}
# //*          --> {key : function(value) for (key,value) in iterable}

students = {
    "Zayan": 85,
    "Salman": 92,
    "Shahzain": 75,
    "Ali Hossain": 51,
    "Zain Khan": 55,
    "Nizamuddin": 65,
    "Abdul Ahad": 71,
    "Ubaidullah": 49,
    "Habibullah": 95,
    "Nasiruddin": 59,
}

passed_students = {key: value for (key, value) in students.items() if value >= 80}
# print(f"passed students are\n-->{passed_students}")

print("Passed students are.")
for i in passed_students.items():
    print(i)


# defining a function to avoid conflict
def check(value):
    if value >= 70:
        return "passed"
    else:
        return "failed"


# result = {
#     key: ("Passed" if value >= 70 else "Failed") for (key, value) in students.items()
# }

result = {key: check(value) for (key, value) in students.items()}
for i in result.items():
    print(i)
