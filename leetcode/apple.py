#%%
from collections import Counter
def uniqueWordCount():
    #text = myfile.read()
    text = "the dog runs fast. the dog is brown"
    mlist = [x for x in text.split()]
    '''
    d = dict()
    for word in mlist:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    '''

    return Counter(mlist)
#%%
uniqueWordCount()

# %%
