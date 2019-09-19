#%%
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print('Letters cannot be ^2')

#%%
try:
    x = 5
    y = 0
    z = x/y
    print(z)
except ZeroDivisionError:
    print('Can\'t divide by zero')
finally:
    print('No more tries for you!')

#%%
def ask():
    while True:
        try:
            num = int(raw_input('Please input an integer: '))
            if num < num**2:
                break
        except ValueError:
            print('Oops that isn\'t an integer.')
    print('You\'r number squared is: %i ' % num**2)

ask()