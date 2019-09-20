'''
Given a list of numbers and a number `k`
return whether any two number from the list add up to `k`

ex: [10,15,3,7] and `k` = 17 return true since 10 + 7  = 17
'''
#realized `my_list[index]+my_list[index+1]` assuming [a,b,c,d]
#was only a+b, b+c, c+d and thought that if I could solve it
#using those three integers it would be easier than iterating over
#the other combinations
#tl;dr - had a hunch and wrote out three examples that all worked so i then coded it
#%%
def add_to_k(my_list, k):
    for index, num in enumerate(my_list):
        #handles out of range
        if index == len(my_list)-1:
            break
        #see comment above function
        if sum(my_list)-(my_list[index]+my_list[index+1]) == k:
            print('%i-(%i+%i) = %i'% (sum(my_list),my_list[index],my_list[index+1],k))
            return True
    return False

add_to_k([19,19805,453,-2],17)

#%%
def iterate_list(my_list, k):
    for num in my_list:
        for num2 in my_list:
            if num != num2 and num + num2 == k:
                print('%i + %i = %i' % (num,num2,k))
                return True
    return False

iterate_list([19,19805,453,-2],17)