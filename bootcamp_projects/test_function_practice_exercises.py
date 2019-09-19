def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # print(min(a,b))
        if a < b:
            print(a)
        else:
            print(b)
    else:
        # print(max(a,b))
        if a > b:
            print(a)
        else:
            print(b)
#lesser_of_two_evens(2,4)
#lesser_of_two_evens(2,5)


def animal_crackers(text):
    if len(text.split()) != 2:
        print("error: must be a two word string")
    #return text.lower().split()[0][0] == text.lower().split()[1][0]
    else:
        if text.split()[0][0] == text.split()[1][0]:
            return True
        else:
            return False
#print(animal_crackers("wow whis"))


def makes_twenty(x,y):
    #return (x+y) == 20 or x == 20 or y ==20
    if x == 20 or y == 20:
        return True
    elif x + y == 20:
        return True
    return False
#print(makes_twenty(12,9))


def old_macdonald(my_string):
    name = my_string[0].capitalize() + my_string[1:3] + my_string[3].capitalize() + my_string[4:]
    print(name)
#old_macdonald("tester")


def yoda(sentance):
    yoda_speak = ""
    my_list = [words for words in sentance.split()] #my_list = sentance.split()
    #reverse = my_list[::-1]
    #return ' '.join(reverse)
    for x in range(len(my_list)-1,-1,-1):
        yoda_speak = yoda_speak + my_list[x] + " "
    print(yoda_speak)
#yoda("I am home")

def almost_there(number):
    #return abs(100 - number) <= 10 or abs(200 - number) <= 10
    if abs(100 - number) <= 10 or abs(200 - number) <= 10:
        return True
    else:
        return False
#print(almost_there(149))


def has_33(num_array):
    for index,num in enumerate(num_array):
        if num == 3 and num_array[index+1] == 3:
            return True
    return False
#print(has_33([1,2,3,2,3,3]))


def paper_doll(my_word):
    new_word = ''
    for letter in my_word:
        new_word += 3*letter
    return new_word
#print(paper_doll('Hello'))


def blackjack(a,b,c):
    total = a+b+c
    if total < 3 or total > 33:
        print("Bad Hand")
        return False
    if total > 21 and 11 in {a,b,c}:
        total = total-10
    if total <= 21:
        print(total)
    else:
        print("Bust")
#lackjack(5,6,7)


def summer_69(my_array):
    total = 0
    ####
    add = True
    for num in my_array:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
    ####
    if 6 not in my_array:
        for num in my_array:
            total = total + num
        print(total)
        return total
    #Gets the index of 6 followed by the first 9
    for index,num in enumerate(my_array):
        if num == 6:
            summer_time_start = index
            for x in range(summer_time_start, len(my_array)):
                if my_array[x] == 9:
                    summer_time_stop = x
                    break
    # adds up all the varialbes excluding the range from 6-9
    for index, num in enumerate(my_array):
        if index in range(summer_time_start, summer_time_stop+1):
            num *= 0
        total += num

    print(total)
#summer_69([9,6,7,8,9,9,9])


def spy_game(my_secret):
    ###
    code = [0,0,7]
    for num in my_secret:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
    ####

    if 0 not in my_secret:
        return False
    for index,num in enumerate(my_secret):
        if num == 0:
            for x in range(index,len(my_secret)):
                if my_secret[x] == 0:
                    for y in range(x,len(my_secret)):
                        if my_secret[y] == 7:
                            return True
    return False
#print(spy_game([1,2,4,0,1,0,7,5]))


#Didnt Get
def count_prime(num):
    ####
    count = 0
    for new_num in range(2,num+1):
      for x in range(2, new_num):
          if new_num % x == 0:
              count +=1
    print(count)
    ####

    if num < 2:
        return 0
    primes = [2]
    x = 3

    while x <= num:
        #jump by 2 to skip evens
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break
        else: #if you go through entire for loop and never broke out
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)




count_prime(21)
