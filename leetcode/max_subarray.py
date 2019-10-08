'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
#%%
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total = sum(nums)

    #start from nums[0] and build the sum from nums[-1] -> num[0]
    # and check if it's > total
    #move to nums[1] and repeat to num[1]
    for pos_front in range(0,len(nums)):
        for pos_back in range(len(nums),pos_front,-1):
            print(nums[pos_front:pos_back])
            if sum(nums[pos_front:pos_back]) > total:
                total = sum(nums[pos_front:pos_back])

    return total
#%%
#maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

maxSubArray([-2,1])

#%%
