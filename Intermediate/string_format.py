# ---------------#
# //* String.format() --> Optional method that gives user more control when displaying output


first_name = input("Enter your first name\n-->")
middle_name = input("Enter your middle name\n-->")
last_name = input("Enter your last name\n-->")


# print(f"Hello,{First_name}{middle_name}{last_name}")  # This is basic way
# print("Hello,{} {} {}".format(First_name, middle_name, last_name))  # This is formatting method
# print("Hello,{0}{1}{2}".format(First_name, middle_name, last_name))  # This is positional argument
print(
    "Hello,{first_name}{middle_name}{last_name}".format(
        first_name=first_name, middle_name=middle_name, last_name=last_name
    )
)  # keyword argument

txt = "hello {} {} {}"
print(txt.format(first_name, middle_name, last_name))
print("Have a good day!!!")
