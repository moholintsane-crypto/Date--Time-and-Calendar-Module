import calendar

# Option 1: Create or print a list of all full month names
print("Full Months of the Year Names:", list(calendar.month_name)[1:13])
all_months = list(calendar.month_name)[1:13]
for i in range(1, 13):
    print(f"{i}: {calendar.month_name[i]}")

# Option 2: Get a specific month name by its number from user input
month_number = int(input("\nEnter a month number (1-12): "))
if 1 <= month_number <= 12:
    print(f"The name for month {month_number} is", calendar.month_name[month_number])
else:
    print("Invalid month number!")
