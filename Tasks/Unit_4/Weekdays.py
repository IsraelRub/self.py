from datetime import datetime
import calendar


date_string = input('Enter Date: ')
format = '%d/%m/%Y'
date_object = datetime.strptime(date_string, format)
year = date_object.year
month = date_object.month
day = date_object.day

weekday = calendar.weekday(year,month, day)

if weekday == 0:
    print('Monday')
elif weekday == 1:
    print('Tuesday')
elif weekday == 2:
    print('Wednesday')
elif weekday == 3:
    print('Thursday')
elif weekday == 4:
    print('Friday')
elif weekday == 5:
    print('Shabbat')
elif weekday == 6:
    print('Sunday')
else:
    print('Invalid Date')