'''
return a new sorted merged list from K sorted lists, each with size N.
ex: [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].
'''
# ~6min inclusing looking up sort()
def merge_and_sort_lists(list_of_lists):
    new_list = []
    for a_list in list_of_lists:
        for item in a_list:
            new_list.append(item)
    new_list.sort()
    return new_list

merge_and_sort_lists([[10, 15, 30], [12, 15, 20], [17, 20, 32]])