def ace_value(a_list):
    for index, item in enumerate(a_list):
        if 'A' in a_list[index] and item[1] == 11:
            item[1] = 1
            break
    return a_list


def points(a_list):
    value = 0
    for index, item in enumerate(a_list):
        value += a_list[index][1]
    return value


ace_count = 0
a = [['A', 1], ['A', 11], ['J', 3], ['A', 11]]

my_points = points(a)
points(a)

while my_points > 21:
    a = ace_value(a)
    print(a)
    my_points = points(a)
    print(my_points)
#%%
def points_v2(cards):
    enumerate_points = 0
    for index, card in enumerate(cards):
        print(cards[index][1])

    for_points = 0
    for card in cards:
        print(cards[0][1])

points_v2([['A', 1], ['A', 11], ['J', 3], ['A', 11]])

#%%
