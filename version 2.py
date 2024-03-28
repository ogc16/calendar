import calendar

def print_year_calendar(year):
    for month in range(1, 13):
        # Print the month and year as a header
        print(calendar.month_name[month], year)

        # Print the days of the week
        print("Mo Tu We Th Fr Sa Su")

        # Get the calendar matrix for the given month
        cal = calendar.monthcalendar(year, month)

        # Iterate over each week in the calendar
        for week in cal:
            # Iterate over each day in the week
            for day in week:
                if day == 0:
                    print("  ", end=" ")
                else:
                    # Print the day with proper formatting
                    print(f"{day:2d}", end=" ")
            # Move to the next line after printing all the days in the week

year = int(input("Enter the year: "))
print_year_calendar(year)
