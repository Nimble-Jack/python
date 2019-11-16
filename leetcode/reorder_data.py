#%%
def reorderLogFiles(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    a = [x.split() for x in logs if x.split()[1].isalpha() == True]
    n = [x.split() for x in logs if x.split()[1].isalpha() == False]

    a.sort(key=lambda x:(x[1:],x[0]))
    return a

    log = 0
    word = 1
    size = len(a)
    while log+1 < size and a[log][word] == a[log+1][word]:
        if word == len(a[log]):
            print('wwoww')
        word +=1
        log +=1
    print(a[log][word])
    return

    #a = sorted(a, key=lambda a:a[1])
    a = [' '.join(val) for val in a]
    n = [' '.join(val) for val in n]

    return a+n


#%%
reorderLogFiles(["t kvr", "r 3 1", "i 403", "7 so", "t 54"])


# %%


# %%
