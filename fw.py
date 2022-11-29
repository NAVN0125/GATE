import datetime
from datetime import date

date_entry = input('Enter birthday date in DD-MM-YYYY format: ')
day, month, year = map(int, date_entry.split('-'))
date1 = datetime.datetime(year, month, day)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


print(calculate_age(date1))
