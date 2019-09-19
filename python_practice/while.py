
#%%
def ace_value(a_list):
    for index, item in enumerate(a_list):
        #print('%i : %s' % (index, item))
        if 'A' in a_list[index] and item[1] == 11:
            print(index, item)
            item[1] = 1
            print(index, item)
    return a_list


def points(a_list):
    value = 0
    for index, item in enumerate(a_list):
        value += a_list[index][1]
    return value


#%%
ace_count = 0
a = [['A', 1], ['A', 11], ['J', 3], ['A', 2]]

#%%
my_points = points(a)
points(a)

#%%
while my_points > 21:
    a = ace_value(a)
    print(a)
    my_points = points(a)
    print(my_points)

#%%
