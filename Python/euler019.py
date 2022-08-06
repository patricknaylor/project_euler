###########################################
#
#Project Euler Problem 19
#
#You are given the following information, but you may prefer to do some research for yourself.
#
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
###########################################

#I'm sure this can be done with python's datetime functionality, but that's no fun.

#for us, days will be a list with three entries; [year, month, day, day of the week (0 through 7)]
#thus, time begins at [1900,1,1,0]

#make a dictionary for days in the month (normal year)
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

#start by checking if it's a leap year. there are 365 days usually, 366 in a leap year
#remember: leap years are the ones divisible by 4; unless they're divisible by 100; but they are leap years if divisible by 400
def check_leap_year(date):
    if date[0]%400 == 0:
        return True
    if date[0]%4 == 0 and date[0]%100 != 0:
        return True
    else:
        return False

#we need to be able to compute the next day
def next_day(date):
    year, month, day, week = date[0], date[1], date[2], date[3]

    week = (week + 1)%7 #this is the easy one, since this always happens

    is_leap_year = check_leap_year(date)

    if month == 12 and day == 31: #this is the next easiest-- if its dec 31, then the next day is the first day of the next year
        year += 1
        month = 1
        day = 1

    #otherwise, the year won't change. in this case, if it's the last day of the month, update the month

    elif day == days_in_month[month] and month != 12 and not is_leap_year:
        day = 1
        month += 1
    elif day == days_in_month[month] and month != 12 and is_leap_year and month !=2:
        day = 1
        month += 1
    elif is_leap_year and (month, day) == (2,28):
        day = 29
    elif is_leap_year and (month, day) == (2,29):
        day = 1
        month = 3
    
    #otherwise, it's not the last day of a month so just update the day
    else:
        day += 1
        
    return [year, month, day, week]


def count_sundays():
    count = 0
    date = [1900,1,1,0]
    
    while date[0] < 2001:
        if date[0] > 1900 and date[0] < 2001 and (date[2],date[3]) == (1,6):
            count +=1
        date = next_day(date)

    return count


count = count_sundays()
print("There are {} Sundays on the first of a month in the twentieth century.".format(count))

#Answer is 171. 



    
