import datetime as dt

"""Task 1:

Write a Python script to display the various Date Time formats."""


# current_time = dt.datetime.today()

# year, week_number, week_day = current_time.isocalendar()
# month_name = current_time.strftime('%B')
# day_name = current_time.strftime('%A')
# tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = current_time.timetuple()

# print(f'Current date and time: {current_time}')
# print(f'Current year: {current_time.year}')
# print(f'Month of year: {month_name}')
# print(f'Week number of the year: {week_number}')
# print(f'Weekday of the week: {week_day}')
# print(f'Day of year: {tm_yday}')
# print(f'Day of the month: {tm_mday}')
# print(f'Day of week: {day_name}')
# print(current_time.isocalendar())
# print(current_time.timetuple())
"""Task 2 :

Write a Python program to print the dates of yesterday, today, tomorrow.
Your result could look like this :"""


# current_time = dt.datetime.today()

# yesterday = current_time - dt.timedelta(days=1)
# reform_yesterday = yesterday.strftime('%Y-%m-%d')
# reform_today = current_time.strftime('%Y-%m-%d')
# tommorrow = current_time + dt.timedelta(days=1)
# reform_tommorow = tommorrow.strftime('%Y-%m-%d')

# print(f'Yesterday : {reform_yesterday}\nToday : {reform_today}\nTomorrow : {reform_tommorow}')

"""Task 3: Write a Python program to add 5 seconds to the current time.

Hint: you can use timedelta to solve the task.
Your result could look like this :"""

# current_time = dt.datetime.today()

# plus_five_sec = current_time + dt.timedelta(seconds = 5 )

# reform1 = current_time.time()
# reform2 = plus_five_sec.time()

# print(f'Current time: {reform1}')
# print(f'After adding 5 seconds: {reform2}')


"""Task 4: Write a Python program to print the next 5 days starting today.

Hint: you can use timedelta and for loop to solve the task."""

# current_time = dt.datetime.today()

# print(f'Today: {current_time}')
# print('Next 5 days:')

# for i in range(1, 6):
    
#     counting = current_time + dt.timedelta(days= i)
    
#     print(counting)

"""Task 5:

Write a Python program to convert Year/Month/Day to Day of Year using datetime module.
"""

# current_time = dt.datetime.today()

# tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = current_time.timetuple()

# print(f'Today: {current_time}')
# print(f'Day of the year: {tm_yday}')


"""Task 6:

Write a Python program to find the date of the first Monday of a given week.
"""
import re
from datetime import datetime as dt, timedelta as td

# def monday_finder(date):
    
#     date = dt.strptime(date, '%Y-%m-%d')
#     monday = date - td(days= date.weekday())
    
#     return f'The monday of this week: {monday.strftime("%B-%d")}'
    

# date = input('Enter any date to find Monday of given week (yyyy-mm-dd): ')

# pattern = r'(^[0-9]{4})-(1[0-2]|[0-9]+)-(3[01]|[0-2]?[0-9]+$)'

# match = re.match(pattern, date)

# loop_turn_off = True

# while loop_turn_off == True:
    
#     if match:

#         print(monday_finder(date))
#         loop_turn_off = False
#     else:
#         print('Invalid date. Please try again.')
#         date = input('Enter any date to find Monday of given week (yyyy-mm-dd): ')
#         continue




# def monday_finder():


# current_date = dt.datetime.today()

# start_day = current_date - dt.timedelta(days= current_date.weekday())

# days_container = []

# for i in range(7):
    
    
#     if start_day.weekday() == 0:
        
#         reform = start_day.strftime("%Y-%m-%d")
#         days_container.append(reform)
        
#         start_day += dt.timedelta(days= 1)
# days_container = "".join(days_container)

# print(f'The first Monday of this week was: {days_container}')


#------------------------------------------------

# current_week = dt.datetime.

# def monday_finder():

#     current_time = dt.datetime.today()
    
#     first_day_of_month = dt.datetime(current_time.year, current_time.month, 1)
    
#     if current_time.month == 12:
        
#         first_day_next_month = dt.datetime(current_time.year +1, 1, 1)
        
#     else: 
        
#         first_day_next_month = dt.datetime(current_time.year, current_time.month + 1, 1)
        
#     mondays_of_current_month = []
#     current_day = first_day_of_month
    
#     while current_day < first_day_next_month:
        
#         year, week, weekday = current_day.isocalendar()
    
#         if weekday % 7 == 1:
            
#             mondays_of_current_month.append(current_day.date())
        
#         current_day += dt.timedelta(days=1)
    
#     for monday in mondays_of_current_month:
#         print(monday)


# monday_finder()

#------------------------------------------------

# def sunday_finder(year):
    
#     # current_date = dt.datetime.today()
    
#     first_day_of_year = dt.datetime(year, 1, 1)
    
#     last_day_of_year = dt.datetime(year, 12, 31)
    
#     sundays_of_the_year = []
    
    
#     while first_day_of_year <= last_day_of_year:
        
#         year, week, weekday = first_day_of_year.isocalendar()
        
#         if weekday % 7 == 0:
            
#             reform = first_day_of_year.strftime('%Y-%m-%d')
            
#             sundays_of_the_year.append(reform)
            
#         first_day_of_year += dt.timedelta(days = 1)
        
#     sundays_of_the_year = "\n".join(sundays_of_the_year)
    
#     return f'Output:\n{sundays_of_the_year}'



# year = int(input('Please enter a year(yyyy) to determine the number of Sundays in that year: '))

# print(sunday_finder(year))

#--------------------------------------------------------
# def sunday_finder(year):
    
#     current_date = dt.datetime.today()
    
#     first_day_of_year = dt.datetime(current_date.year, 1, 1)
    
#     last_day_of_year = dt.datetime(current_date.year, 12, 31)
    
#     sundays_of_the_year = []
    
    
#     while first_day_of_year <= last_day_of_year:
        
#         year, week, weekday = first_day_of_year.isocalendar()
        
#         if weekday % 7 == 0:
            
#             reform = first_day_of_year.strftime('%Y-%m-%d')
            
#             sundays_of_the_year.append(reform)
            
#         first_day_of_year += dt.timedelta(days = 1)
        
#     sundays_of_the_year = "\n".join(sundays_of_the_year)
    
#     return f'Output:\n{sundays_of_the_year}'

# print(sunday_finder())



def sunday_finder(year):
    
    year_look_for = dt(year,1, 1)
    
    end_of_year = dt(year, 12, 31)
    
    sunday = []
    
    while year_look_for < end_of_year:
        
        if year_look_for.weekday() == 6:
            
            print(year_look_for.strftime('%Y-%B-%d'))
    #         reform = year_look_for.strftime('%Y-%B-%d')
            
    #         sunday.append(reform)
        year_look_for += td(days=1)
    
    # sunday = "\n".join(sunday)
        
    # return year_look_for
    
year = int(input('Enter any year to find Sundays of year (yyyy): '))    


sunday_finder(year)
# print(sunday_finder(year))