'''
You are given the following information, but you may prefer
to do some research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
'''

'''
I will attempt this by counting the number of days elapsed
by the start of each month and then seeing if it is divisible by 7
(which shows it is a Sunday)
'''

import utility.factors as factors

def get_days_in_month(month, year):
    '''Return the number of days in a given month in a given year
    (the year part matters for February)
    
    Month should be a number from 1-12
    '''
    
    #September, April, June, November
    if month in [9, 4, 6, 11]:
        return 30
    elif month == 2: #February
        #Is leap year?
        if factors.is_factor(4, year):
            if(factors.is_factor(100, year) and 
            not factors.is_factor(400, year)):
                return 28
            else:
                return 29
        else:
            return 28
    else:
        return 31
    

if __name__ == '__main__':
    #===========================================================================
    # def testl(year):
    #    print(year, get_days_in_month(2, year))
    # testl(1900)
    # testl(1904)
    # testl(2000)
    # testl(1950)
    # testl(2300)
    # testl(2400)
    #===========================================================================
    day_number = 1 #January 1st 1900 (monday, not a sunday so we ignore)
    day_number = 2 #January 1st 1901 (Tuesday)
    sunday_fell = 0
    for year in range(1901, 2001): #excludes 2001
        for month in range(1, 13): #excludes 13
            if year == 2000 and month == 12:
                #This is the last December
                #We do not want to add these days on
                continue
            
            #Day number that next month starts on
            day_number += get_days_in_month(month, year)
            
            
            if factors.is_factor(7, day_number):
                sunday_fell += 1
                #print(year, month+1, day_number, "sunday")
            #else:
                #print(year, month+1, day_number)
    
    print(sunday_fell)
