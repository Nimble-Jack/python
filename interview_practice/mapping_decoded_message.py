'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can
be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.

~ about 60min
'''
#%%
import string

def decode_options(secret):
    #decoder = dict(zip(string.ascii_lowercase,range(1,27)))
    possible_combinations = []
    message = str(secret)

    #checks for edge case
    result = map(int, message)
    if any(values <= 0 for values in result) == True:
        return 'Not valid'
    if len(message) <= 1:
        possible_combinations.append(message)
        return(len(possible_combinations))

    #get all of the pairs
    for index,char in enumerate(message):
        individual = [val for val in message]
        #remove the two individual digits and add the pair as one number if < 27
        individual.pop(index)
        individual.pop(index)
        if int(message[index:index+2]) < 27:
            individual.insert(index,message[index:index+2])
            possible_combinations.append(individual)

        #indexing issue
        if index == len(message)-2:
            break

    #get all the individual values
    individual = [val for val in message]
    possible_combinations.append(individual)

    print(possible_combinations)
    return len(possible_combinations)

    '''
    I was going to do this(below) then realized it was silly to add then check.
    Instead check first before adding as i did above
    result = map(int,individual)
    if all(values < 27 for values in result) == True:
        possible_combinations.append(individual)
    '''
#%%
decode_options(130142)

#%%
