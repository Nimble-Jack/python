'''
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
#%%
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if s == '':
        return True
    if len(s)%2 != 0:
        return False

#loop through this and keep removing the substring until len > 2
    while len(s) > 1:
        if s.find('[]') != -1:
            location = s.find('[]')
        elif s.find('()') != -1:
            location = s.find('()')
        elif s.find('{}') != -1:
            location = s.find('{}')
        else:
            return False
        s = s[:location]+s[location+2:]

    return True
#%%
isValid('(([{]){})')

#%%
'''
def check_sets(ss):
    if ss == '()':
        return True
    if ss == '[]':
        return True
    if ss == '{}':
        return True
    return False

while len(s) > 2:
        middle = int(len(s)/2)
        print('middle:', s[middle])
        if s[middle] in open_p:
            if check_sets(s[middle:middle+2]) == True:
                s = s[:middle]+s[middle+2:]
                print(s)
                continue
            return False

        elif s[middle] in close_p:
            if check_sets(s[middle-1:middle+1]) == True:
                s = s[:middle-1]+s[middle+1:]
                print(s)
                continue
            return False

    if len(s) == 2:
        return check_sets(s)

    return s
'''