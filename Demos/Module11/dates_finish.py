#
# Dates
#
from datetime import date
from datetime import time
from datetime import datetime

def main():

    # today's date
    today = date.today()
    print("Today's date is ", today)

    # select date's components
    print("Date componets: ", today.day, today.month, today.year)

    # weekday (0 = Monday, 6 = Sunday)
    print("Day of week:", today.weekday())
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print("Which is a: ", days[today.weekday()])

    # DateTime objects
    today = datetime.now()

    print("The current date and time is ", today)

    print("The time is: ", datetime.time(today))



if __name__ == "__main__":
    main()