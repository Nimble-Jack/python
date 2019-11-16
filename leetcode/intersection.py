'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load
all elements into the memory at once?
'''
def intersect1(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if len(nums1) <= 1 or len(nums2) <= 1:
        return min(nums1, nums2, key=len)

    if len(nums1) >= len(nums2):
        smaller = nums2
        bigger = nums1
    else:
        smaller = nums1
        bigger = nums2

    in_range = []
    for num in smaller:
        if num in bigger:
            in_range.append(num)
            bigger.remove(num)

    return in_range
'''array1 = [1,2,4,5,6]
array2 = [3,4,5,8,9]
itr1 = array1[0] \\ Points at 1
itr2 = array2[0] \\ Points at 3
\\ We start check if they are the same which they are not so step with the smaller one
itr1++; \\ 2
itr1++; \\ 4 And now its bigger and still not the same so increase the other iterator
itr2++; \\ 4  The are the same so add to results and increase both
itr1++; itr2++;  \\ Both are 5 so add that too and repeat
itr1++; itr2++;  \\ 6 != 8 and 6 is at the end of its list so we know there can't be any more matches
\\ Therefore, sorted arrays mean you only loop the size of the smallest array which is awesome!
'''


#%%
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1.sort()
    nums2.sort()

    i = 0
    j = 0
    intersect = []
    while True:
        if i == len(nums1) or j == len(nums2):
            break
        itr1 = nums1[i]
        itr2 = nums2[j]
        print(itr1,itr2)
        if itr1 == itr2:
            intersect.append(itr1)
            i += 1
            j += 1
        else:
            if itr1 < itr2:
                i +=1
            else:
                j +=1

    return intersect


#%%
intersect([1,2,2,1], [2,2])
#%%
intersect([2, 4, 5, 6], [4, 6, 7, 8])

#%%
#intersect([4, 3, 9, 3, 1, 9, 7, 6, 9, 7], [5,0,8])