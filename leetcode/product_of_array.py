#%%
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1] * len(nums)
    #left and right pointers
    lo = 0
    hi = len(nums) - 1
    #product for left and right
    leftProduct = 1
    rightProduct = 1
    #keep going until pointers meet
    while lo < len(nums):
        print(lo, hi)
        #add running from the l/r products to these spots
        res[lo] *= leftProduct
        res[hi] *= rightProduct
        print(res[lo],res[hi])
        #multiply products by current in nums
        rightProduct *= nums[hi]
        leftProduct *= nums[lo]
        print(leftProduct, rightProduct)
        #inc/dec pointers
        lo += 1
        hi -= 1
        print('\n')
    return res

    # [H[i][0]*H[-i-1][1] for i in range(L)]

#%%
productExceptSelf([1, 2, 3, 4])

# %%
