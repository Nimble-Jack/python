#%%
def lengthOfLongestSubstringKDistinct( s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """

    if k==1 and any(val != s[0] for val in s):
        return 1

    distinct = 0
    sub = ''
    for char in s:
        if char not in sub:
            distinct +=1
            if distinct == k :
                sub += char
                continue
            if distinct > k:
                continue
        sub += char
    print(sub)
    return len(sub)
#%%
lengthOfLongestSubstringKDistinct("aac",2)

#%%
