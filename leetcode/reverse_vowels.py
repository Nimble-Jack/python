#%%
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowel_order = []
    vowels = ['a','e','i','o','u']

    s = [val for val in s]

    for index,char in enumerate(s):
        if char.lower() in vowels:
            vowel_order.append([index,char])

    for pair in vowel_order.copy():
        s[pair[0]] = vowel_order[-1][1]
        vowel_order.pop(-1)

    return ''.join(s)

#%%
reverseVowels('aA')



#%%
