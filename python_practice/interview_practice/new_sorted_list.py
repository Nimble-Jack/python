'''
return a new sorted merged list from K sorted lists, each with size N.
ex: [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].
'''
#%%
def merge_lists(list_of_lists):
    merged_list = []
    for a_list in list_of_lists:
        for item in a_list:
            merged_list.append(item)
    merged_list.sort()
    return merged_list

#%%
merge_lists([[10, 15, 30], [12, 15, 20], [17, 20, 32]])

#%%
