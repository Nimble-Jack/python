'''
Create a function that takes in a month and returns the days in month
account for miss spellings
account for abbreviations (first 3 letters)
account for lower case input
account for leap year in February (ever 4 years)
'''
import datetime

def days_in_month(target_month):
    month_list = [['January',31],['February',28],['March',30]]
    now = datetime.datetime.now()

    for month in month_list:
        # replaces 'January' with 'jan' and etc
        month[0] = month[0][:3].lower()
        if target_month == 'feb' and now.year%4 == 0:
            print(29)
            return
        # replaces 'target input' with 'lowercase first 3 letters' and etc
        if month[0] == target_month[:3].lower():
            print(month[1])
            return
    print('Input not valid.')
days_in_month('dfeb')
days_in_month('feb')
days_in_month('March')
