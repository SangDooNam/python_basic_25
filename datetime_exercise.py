import datetime as dt

# current_datetime = dt.datetime.now()


"""Task 1. Using the variable called current_datetime, subtract 15 days from the current time.

Hint: use .strftime() method to reformat the time"""


# fifteenago = current_datetime - dt.timedelta(days = 15)

# reform = fifteenago.strftime('%Y-%m-%d')

# print(reform)



"""Task 2. Using the variable called current_datetime, add 7 days to your current day.

Your result should look like this, if today is 8/07/2021:"""

# afterseven = current_datetime + dt.timedelta(days= 7)

# reform = afterseven.strftime('%Y-%m-%d')

# print(reform)


"""Task 3. 

Your task is to write a reminder message for a customer 
that is being sent out on 2020-01-01 to please pay in 25 days. 
Create a string that stores a message to a customer called Friedrich, 
print out the message to the terminal.

Steps:

Start by creating a datetime of the current date, January 1st, 
2020: current_date = datetime(year=2020, month=1, day=1)

Do your calculations to add 25 days to current_date. 
Create a string and print it out. Your result should look like this:"""


current_date = dt.datetime(year= 2020, month=1, day=1)
# hello_date = dt.date(3000, 9, 20)

# print(current_date)

reminderdate = current_date + dt.timedelta(days = 25)

reform = reminderdate.strftime("%d %B, %Y")

print(f'Hello Friedrich, your rent of 300 € is due on {reform}.')

