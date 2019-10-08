'''
----------------------------------------------------------------------------------------
What is the output?
'''
#%%
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)            # 0,1
f(3,[3,2,1])    #3,2,1,0,1,4
f(3)            #0,1,4
'''
f(3) uses the same default list as f(2) which is why it has 0,1 a
the start

f(3,[3,2,1]) passes its own list which doesn't use the default l=[]
'''