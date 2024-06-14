# -----------#
# //* Zip function --> Aggregate elements from two or more iterable(list, tuple,sets etc)
# //*                  creates a zip object with paired elements stored in  tuples fro each elements

names = [
    "Zayan",
    "Salman",
    "Shahzain",
    "Ali Hossain",
    "Zain Khan",
    "Nizamuddin",
    "Abdul Ahad",
    "Ubaidullah",
    "Habibullah",
    "Nasiruddin",
]
scores = [50, 67, 78, 85, 45, 89, 56, 56, 90, 0]

zipped = zip(names, scores)  # Converting into zip
for i in zipped:
    print(i)


# converting zip function into dictionary
zipped = {names: scores for names, scores in zip(names, scores)}
print(zipped, "\n")


# a function to check pass or fail
def check(value):
    if value >= 50:
        return "pass"
    else:
        return "fail"


# Syntax --> {key : function(value) for (key,value) in iterable}
result = {key: check(value) for (key, value) in zipped.items()}

# Printing the values
for i in result.items():
    print(list(i))
