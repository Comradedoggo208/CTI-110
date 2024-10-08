# using python built in library

# get datetime library to use it in the program
import datetime

# assign currecnt date and time to a variable
time = datetime.datetime.now()
month = time.month
month_word = time.strftime("%B")
today = datetime.datetime.today()
weekday = today.weekday()

# display date/time
print(f"The current date and time is {time}")
print(f"The current Month is {month}")
print(f"The current Month is {month_word}")
print(f"today is {today}")
print(f"the day of the week is {weekday}")

print(type(weekday))
'''
weekday = int(input("enter an integer 0-6 as the day of the week: "))
'''
# if-else statements to determine the day of the week
if weekday == 0:
    weekday_word = "Monday"
elif weekday == 1:
    weekday_word = "Tuesday"
elif weekday == 2:
    weekday_word = "Wednesday"
elif weekday == 3:
    weekday_word = "Thursday"
elif weekday == 4:
    weekday_word = "Friday"

else:
    print("invalid day of week!!!")
    weekday_word = "INVALID"
print()
print(f"the day of the week is {weekday_word}")
