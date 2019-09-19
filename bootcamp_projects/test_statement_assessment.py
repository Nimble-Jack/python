#%%
#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower == 's':
        #continue
        print(word)


# Use range() to print all the even numbers from 0 to 10.
# Better answer: for num in list(range(0,11,2)) step through 0-10 by 2
for num in range(0,11):
    if num % 2 == 0:
        #continue
        print(num)


#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
num_list = [num for num in range(1,51) if num % 3 == 0 ]
#print(num_list)


#Go through the string below and if the length of a word is even print "even!"
st2 = 'Print every word in this sentence that has an even number of letters'
for word in st2.split():
    if len(word) % 2 == 0:
        continue
        print(str(len(word)) + " " + word)


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
#instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples
#of both three and five print "FizzBuzz".
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        continue
        #print("FizzBuzz")
    elif num % 3 == 0:
        continue
        #print("Fizz")
    elif num % 5 == 0:
        continue
        #print("Buzz")
    else:
        continue
        #print(num)


#Use List Comprehension to create a list of the first letters of every word in the string below:
st3 = 'Create a list of the first letters of every word in this string'
my_letters = [ letter[0] for letter in st3.split() ]
#print(my_letters)

#%%
print('h')
