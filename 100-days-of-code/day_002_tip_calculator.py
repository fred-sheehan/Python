# Day 2 Project: Tip Calculator
# Greeting
print("\nWelcome to the tip calculator.\n")

# 1st input: enter total bill amount
print("What was the total bill?" + input())
total_bill = float(input())

# 2nd input: enter percentage tip to give
print("What percentage tip would you like to give? 10, 12, or 15 ?" + input())
tip_percentage = int(input())

# 3rd input: enter number of people to split the bill
print("How many people to split the bill between?" + input())
number_of_people = int(input())

# Calculate the tip
tip = total_bill * (tip_percentage / 100)

# Calculate the total bill with tip
total_bill_with_tip = total_bill + tip

# Calculate the bill per person
bill_per_person = total_bill_with_tip / number_of_people

# Round the bill per person to 2 decimal places
final_amount = round(bill_per_person, 2)

# Display the final amount
print(f"Including the tip, each person should pay ${final_amount}")
