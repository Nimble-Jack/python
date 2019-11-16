#%%
def reverse1(x):
    """
    :type x: int
    :rtype: int
    """
    a = list(str(x))
    b = a[::-1]

    if x < 0:
        neg = b.pop()
        c = int(neg+''.join(b))
    else:
        c = int(''.join(b))

    if -2**31 <= c <= 2**31-1:
        return c
    else:
        return 0
#%%
reverse1(-123000)


x = -2
x = -x
print(x)

# %%
