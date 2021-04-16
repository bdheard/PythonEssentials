#
# Calendars
#

#import the calendar module
import calendar

# create a plain test calendar
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2021, 1, 0, 0)
print(st)

# create an HTML formatted calendar
c2 = calendar.HTMLCalendar(calendar.MONDAY)
html = c2.formatmonth(2021, 1, 0)
print(html)

# loop the days of a month
# zeroes mean that the day of the week is an overlapping month
for day in c.itermonthdays(2021, 2):
    print(day)

# The calendar module provides useful utilities for the given locale, 
# such as the names of days and months in both full and abbreviated forms
for month in calendar.month_name:
    print(month)

# calculated the days based on a rule
# Example: First Friday of the month.
print("Team meetings will be on:")
for month in range(1,13):
    cal = calendar.monthcalendar(2021, month)
    week_one = cal[0]
    week_two = cal[1]

    if week_one[calendar.FRIDAY] != 0:
        meet_day = week_one[calendar.FRIDAY]
    else:
        meet_day = week_two[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[month], meet_day))


