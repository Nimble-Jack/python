#%%
def rotateString(a,b):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    if a == b:
        return True
    size = len(a)
    index = 0
    while index < size:
        a = a[1:]+a[0]
        if a == b:
            return True
        index +=1
    return False

#%%
rotateString('abcde', 'cdeab')


#%%
