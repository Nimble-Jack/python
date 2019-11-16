#%%
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    p = [char for char in s if char.isalnum()]
    return p == p[::-1]

#%%
isPalindrome('A man, a plan, a canal: Panama')

#%%
isPalindrome("A man, a plan, a canal: Panama")

#%%
