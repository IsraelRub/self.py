import calendar

date_string = input('Enter Date: ')

day = int(date_string[:2])
month = int(date_string[3:5])
year = int(date_string[6:])

weekday = calendar.weekday(year,month, day)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Shabbat', 'Sunday']
name_days= days[weekday]
print(name_days)