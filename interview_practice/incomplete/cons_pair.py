'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
'''
#%%
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

#Implement car and cdr
def car(paired):
    pass
    #return first element

def cdr(paired):
    pass
    #return last element

#%%
my_pair = cons(1,2)
for a, b in my_pair:
    print(a,b)
#%%
