"""
Function with output

def my_function():
    # do this
    # do that
    return


def my_function():
    return 3*2


def format_name(first_name, last_name):
    name = first_name.title() + " " + last_name.title()
    return name


print(my_function())
print(format_name("John", "Doe"))
print(format_name("john", "doe"))
print(format_name("JOHN", "DOE"))

"""

# functions with more than onde return


def format_name(first_name: str, last_name: str):
    """
    Takes first name and last name and returns a formatted name in the title case version
    :param first_name:
    :param last_name:
    :return: name
    """
    if first_name == "" or last_name == "":
        return "Your name is empty."
    name = first_name.title() + " " + last_name.title()
    return name


print(format_name(input("What id your first name? "), input("What is your last name? ")))
