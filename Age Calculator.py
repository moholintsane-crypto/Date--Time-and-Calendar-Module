from datetime import date

def calculate_age(birth_date):
    today = date.today()
    
    # Calculate difference in years
    years = today.year - birth_date.year
    
    # Check if the birthday has passed this year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        years -= 1
        
    # Calculate months and days
    months = today.month - birth_date.month
    if months < 0:
        months += 12
        
    days = today.day - birth_date.day
    if days < 0:
        # Get days in previous month
        prev_month = today.month - 1
        if prev_month == 0:
            prev_month = 12
        # Use year before current for month-day correction
        check_year = today.year if today.month > 1 else today.year - 1
        
        # Determine number of days in the previous month
        import calendar
        _, days_in_prev_month = calendar.monthrange(check_year, prev_month)
        days += days_in_prev_month
        
    return years, months, days

def main():
    print("=== Python Age Calculator ===")
    try:
        birth_year = int(input("Enter your birth year (YYYY): "))
        birth_month = int(input("Enter your birth month (MM): "))
        birth_day = int(input("Enter your birth day (DD): "))
        
        user_birthdate = date(birth_year, birth_month, birth_day)
        
        if user_birthdate > date.today():
            print("Error: Birth date cannot be in the future.")
        else:
            y, m, d = calculate_age(user_birthdate)
            print(f"\nYou are exactly {y} years, {m} months, and {d} days old.")
            
    except ValueError:
        print("Invalid input! Please enter valid numbers for date formats.")

if __name__ == "__main__":
    main()