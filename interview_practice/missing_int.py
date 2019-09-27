'''
Given an array of integers, find the first missing positive integer in linear time and constant
space. In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''
def missing_int (my_list):
    high_number = max(my_list)
    low_number = min(my_list)

    #handles all negative integers in list
    if all(items < 0 for items in my_list) == True :
        print('No possible positive integers are in the list.')
        print('Returning integer closest to 0.')
        for y in range(high_number, low_number,-1):
            if y != 0 and y not in my_list:
                return y
        return 1

    for x in range(low_number,high_number):
        if x > 0 and x not in my_list:
            return x

    # handles no missing integer
    return high_number +1

#missing_int([3,4,-1,1])
#missing_int([ 1, 2, 0])
#missing_int([-3,-5,-1,4])
#missing_int([3,5,4])
#missing_int([-3,-5,-4])