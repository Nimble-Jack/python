'''
Finding The Smallest Interval Of K Sorted Lists
This interesting and difficult problem was asked by Google recently.

Given K sorted lists of integers, return the smallest interval (inclusive) that contains at least
one element from each list.
If there are multiple intervals of the same size, return the one that starts at the smallest number.

For example, given:

[[0, 1, 4, 17, 20, 25, 31],
 [5, 6, 10],
 [0, 3, 7, 8, 12]]
The smallest range here is [3, 5], since it contains 4 from the first list, 5 from the second list,
and 3 from the third list.

Answer: https://www.dailycodingproblem.com/blog/smallest-interval-of-k-sorted-lists/
'''
#%%
def find_range(list_of_lists):
    sub_list_count = len(list_of_lists)
    for sub_list in range(sub_list_count):
        #get the max/min of each list
        #store it somehow min_list?

        for num in list_of_lists[sub_list]:
             print(num)




m = [[0, 1, 4, 17, 20, 25, 31], [5, 6, 10], [0, 3, 7, 8, 12]]
#%%
find_range(m)