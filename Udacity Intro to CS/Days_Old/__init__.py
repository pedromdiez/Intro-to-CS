# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

daysofmonths = [ 0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year):
    leap_day = 366
    common_day = 365
    if year % 4 != 0:
        return common_day
    elif year % 100 != 0:
        return leap_day
    elif year % 400 !=0:
        return common_day
    else:
        return leap_day
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    #code for same year
    if year1 == year2:
        if month1 == month2:
            return day2 - day1
        days = daysofmonths[month1] - day1 
        month1 = month1 + 1
        while month1 < month2: 
            if leap_year(year1) == 366:
                daysofmonths[2] = 29 
            days = days + daysofmonths[month1] 
            month1 = month1 + 1
        return days + day2
  ################################################
    days = daysofmonths[month1] - day1
    month1 = month1 + 1
    while month1 <= 12:
        if leap_year(year1) == 366:
            daysofmonths[2] = 29
        days = days  + daysofmonths[month1] 
        month1 = month1 + 1
    #print days 
    year1 = year1 + 1 
    ###########################################################
    days = days + day2 
    month2 = month2 - 1 
    while month2 >= 1:
        if leap_year(year2) == 366:
            daysofmonths[2] = 29
        days = days + daysofmonths[month2] 
        month2 = month2 - 1
    #print days
    year2 = year2 - 1 
    ###########################################################
    while year1 <= year2:
        days = days + leap_year(year1)
        year1 = year1 + 1
    return days 


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()