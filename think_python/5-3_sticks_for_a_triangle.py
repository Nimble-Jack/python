'''
Given 3 sticks, create a program that return true or false if those 3 sticks can create a triangle
If a stick is greater than the SUM of the other two then you cannot form a triangle, otherwise yes
If the sum of two equals the third then it is a "degenerate" triangle
'''
#%%
def is_triangle(my_list):
    max_stick = max(my_list)
    my_list.remove(max_stick)
    stick_sum = sum(my_list)
    if max_stick == stick_sum:
        print('Degenerate Triangle')
    if max_stick > stick_sum:
        return False
    else:
        return True

is_triangle([1,2,5])


