def vol(radius):
    volume = (4.0/3.0*3.14)*radius**3
    print(volume)
    return volume
#vol(2)

def ran_check(num, low, high):
    if num in range(low, high+1):
        print("%s is between %s and %s" % (num, low, high))
    return
#ran_check(5,2,5)

def ran_bool(num, low, high):
    return num in range(low,high+1)
#ran_bool(5,2,7)

def up_low(my_string):
    upper_count = 0
    lower_count = 0
    for char in my_string:
        if char.isupper():
            upper_count +=1
        if char.islower():
            lower_count +=1
    print("Number of uppercase letters: %i" % upper_count)
    print("Number of lowercase letters: %i" % lower_count)
#up_low(my_string='Hello Mr. Rogers, how are you this fine Tuesday?')

def unique_list(my_list):
    my_set = set()
    for val in my_list:
        my_set.add(val)
    unique_list_from_set = list(my_set)
    print (type(unique_list_from_set))
    print(unique_list_from_set)
#unique_list(my_list=[1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])

def multiply_all(my_list):
    total = 1
    for num in my_list:
        total = total * num
    print(total)
#multiply_all(my_list=[1, 2, 3, -4])

def palindrome(word):
    return word == word[::-1]
#palindrome(word='wow')

import string
def is_pangram(sentence, alphabet=string.ascii_lowercase):
    for letter in alphabet:
        if letter not in sentence.lower():
            if letter == ' ':
                continue
            print(letter)
            print("The provided string is not a pangram")
            return False
    print("The provided string is a pangram")
#is_pangram(sentence="The quick brown fox jumps over the lazy dog")
## the trick for this one was to check that every letter in the alphabet
## was in the `sentence` not that ever letter in the the sentence was in the
## alphabet; because of course the letters are in the alphabet just not
## necessarily every letter