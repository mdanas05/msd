import calendar
obj=calendar.calendar(firstweekday=0)
for day in obj.iterweekdays():
    print(day)