#%%
def merge(nums1, m, nums2, n):
    nums1[m:] = nums2
    if m == 0:
        return nums1
    size = m + n
    for index, _ in enumerate(nums1):
        if index == 0 and nums1[m] < nums1[0]:
            nums1.insert(0, nums1[m])
            del nums1[m+1]
            m += 1
        if m < size and nums1[index] <= nums1[m] <= nums1[index+1]:
            nums1.insert(index+1,nums1[m])
            del nums1[m+1]

            m +=1
        print('\n')

    return nums1


#%%
merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6,[1, 2, 2],3)
#%%
merge([1, 2, 3,0,0,0], 3, [2, 5, 6],3)
#%%
merge([4,0,0,0,0,0],1,[1,2,3,5,6],5)
#%%
merge([2,5,6, 0, 0, 0], 3, [1,2,3], 3)

'''
This was my first approach and so ugly
    if n == 0:
        return nums1

    if m == 0:
        nums1[:] = nums2
        return nums1

    ugh = abs(len(nums1) - len(nums2))
    if len(nums1) > len(nums2):
        for x in range(ugh):
            nums1.pop()
    else:
        for x in range(ugh):
            nums2.pop()

    i = j = 0
    while j < n:
        if
        p1 = nums1[i]
        p1n = nums1[i+1]
        p2 = nums2[j]
        if p2 < p1:
            print(p1)
            nums1.insert(i, p2)
            m = len(nums1)-1
            j += 1
        elif p1 <= p2 <= p1n:
            nums1.insert(i+1, p2)
            m = len(nums1)-1
            j +=1
        else:
            i += 1
        if i == m:
            for x in range(j, n):
                nums1.append(nums2[x])
            break
        '''