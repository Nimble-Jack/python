'''
-------------------------------------------------------------------------------
Take in an array ex:[1,2,3,4,5,6] and then return a new array with
the product of each integer except for the number at that position
in the array ex:[720,360,240,180,120]
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
A more robust and easy solution
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