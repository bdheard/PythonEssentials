#
# Date operations
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct timedelta
time_delta = timedelta(days=365, hours=5, minutes = 1)
print(time_delta)

# today's date
now = datetime.now()
print("today is: " + str(now))

# today's date plus one year
print("Today plus delta 1: " + str(now + time_delta))

time_delta = timedelta(days=2, weeks=5, minutes = 1)
print("Today plus delta 2: " + str(now + time_delta))

ime_delta = timedelta(days=2, weeks=1, minutes = 1)
print("Today minus delta: " + str(now - time_delta))

# How many there are until end of year
year_end = datetime(now.year, 12, 31)

if now < year_end:
    print("Days until year end: %d" % (year_end - now).days)
else:
    print("Today is the last day of the year")
