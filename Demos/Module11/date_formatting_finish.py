#
# Date Formatting
#

from datetime import datetime

def main():

    # Format time and dates with predefine string control codes
    now = datetime.now()

    # %y / %Y -> Year
    # %a / %A -> Weekday
    # %b / %B -> Month
    # %d      -> Day of Month
    print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

    # %I / %H -> 12/24
    # %M      -> Minute
    # %S      -> second
    # %p      -> locale's am pm
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-Hour time: %H:%M"))

    # date localization
    from pytz import timezone 
    cst = timezone('US/Central')
    cst_time = cst.localize(now)
    cst_time = now.astimezone(cst)
    print(now.strftime("Locale date and time: %X"))
    print(cst_time.strftime("Locale date and time: %X"))
   






if __name__ == "__main__":
    main()