'''
-------------------------------------------------------------------------------
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

'''
-------------------------------------------------------------------------------
Take in an array [1,2,3,4,5,6] and then return a new array with the product of
each integer except for the number at that position in the array
'''

'''
This solution assumes that the list is sorted in ascending order and increments by 1
AKA not very good
'''
import math

def product_of_all_but_i(my_list):
    product_list = []
    for i in my_list:
        product_list.append(math.factorial(my_list[-1])/i)
    return product_list

product_of_all_but_i([1, 2, 3, 4, 5, 6])
product_of_all_but_i([6, 5, 4, 3, 2, 1])

'''
A more robust solution
'''
def product_of_list(my_list):
    total = 1
    for num in my_list:
        total *= num
    return total

def product_without_i(my_list):
    new_list = []
    total = product_of_all_but_i(my_list)
    for i in my_list:
        new_list.append(product_of_list(my_list)/i)
    return new_list

product_without_i([1, 2, 3, 4, 5, 6])
product_without_i([6, 5, 4, 3, 2, 1])

'''
----------------------------------------------------------------------------------------
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples
of both three and five print "FizzBuzz".
'''
def fizzbuzz():
    for num in range(1,101):
        if num%3 == 0 and num%5 == 0:
            print('FizzBuzz')
        elif num%5 == 0:
            print('Buzz')
        elif num%3 == 0:
            print('Fizz')
        else:
            print(num)
fizzbuzz()
