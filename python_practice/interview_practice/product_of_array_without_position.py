'''
-------------------------------------------------------------------------------
Take in an array ex:[1,2,3,4,5,6] and then return a new array with
the product of each integer except for the number at that position
in the array ex:[720,360,240,180,120]
'''

'''
A more robust and very easy solution
'''
def product_of_list(my_list):
    total = 1
    for num in my_list:
        total *= num
    return total

def product_without_i(my_list):
    new_list = []
    for i in my_list:
        new_list.append(product_of_list(my_list)/i)
    return new_list

product_without_i([1, 2, 3, 4, 5, 6])
product_without_i([6, 5, 4, 3, 2, 1])

'''
without division - easy pop and insert ~15m
pop current index from array
iterate through new array and multiply all together then append product to new list
put popped index,value back in array and continue looping
'''
def simple(my_list):
    new_array = []
    for index, num in enumerate(my_list):
        total = 1
        current_value = my_list.pop(index)
        for num2 in my_list:
            total *= num2
        my_list.insert(index,current_value)
        new_array.append(total)
    return new_array

simple([3,4,5])

'''
without division -hard tried to do slicing on either side of index
'''
def product_of_all_no_division(my_list):
    total = 1
    new_list = []
    for index, num in enumerate(my_list):
        first_slice = my_list[:index]
        if len(first_slice) == 0:
            first_slice.append(1)
        second_slice = my_list[index+1:]
        if len(second_slice) == 0:
            second_slice.append(1)
        first = 1
        for num in first_slice:
            first *= num
        second = 1
        for num in second_slice:
            second *= num
        total = first * second
        new_list.append(total)
    return new_list

product_of_all_no_division([3,4,5])

'''
This solution assumes that the list is sorted in ascending order and increments by 1
factorial
AKA not good at all
'''
import math

def product_using_factorial(my_list):
    product_list = []
    for i in my_list:
        product_list.append(math.factorial(my_list[-1])/i)
    return product_list

product_using_factorial([1, 2, 3, 4, 5, 6])
product_using_factorial([6, 5, 4, 3, 2, 1])