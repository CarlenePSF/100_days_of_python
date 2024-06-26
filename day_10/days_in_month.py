def is_leap(input_year):
    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
# def days_in_month(input_year, input_month):
#     months = {
#         1: 31,
#         2: 28,
#         3: 31,
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31,
#         8: 31,
#         9: 30,
#         10: 31,
#         11: 30,
#         12: 31,
#     }
#     if is_leap(input_year):
#         if input_month == 2:
#             return 29
#         else:
#             return months[input_month]
#     else:
#         return months[input_month]
def days_in_month(input_year, input_month):
    """

    :param input_year:
    :param input_month:
    :return:
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if input_month == 2 and is_leap(input_year):
        return 29
    else:
        return month_days[input_month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
