#%%
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    result = 1
    while result**2 < x:
        result += 1
    return result if result**2 == x else result-1

#%%
mySqrt(8)

#%%
mySqrt(36)


#%%
