# Functions with outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide a valid input"

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name?  "), input("What is your second name? ")))

# =================================================
# Functions with multiple outputs
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] = 29
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Please enter a month: "))
while month < 1 or month > 12:
    month = int(input("Please enter a valid month: "))

print(f"In the year {year} month {month} there are {days_in_month(year, month)} days.")
