# ------------------------#
# //*Lambda --> lambda functions are anonymous functions means that the function is without a name.
# There is a difference  between normal def function and lambda function


# Normal Function
# A normal  function is defined using the def keyword.
# It can contain multiple expressions and statements.
# It can als o have a name, which makes it reusable.
def calculation(x, y):
    return x * y


print(f"Result : {calculation(5,5)}")

# Lambda Function
# A lambda function is a small, anonymous function defined using the lambda keyword.
# It can take any number of arguments but can only have one expression.
# The result of this expression is automatically returned.

calculation = lambda x, y: x * y  # THIS IS  LAMBDA EXPRESSION
print("Result :", calculation(6, 9))
