#!/usr/bin/python3

#Problem Nr. 17
#http://www.practicepython.org

import random
import sys



def read_input(max_length):
    print("Cows and Bulls..")
    first_run = False
    if max_length == None:
        first_run = True
        count_str = ""
    else:
        count_str = str(max_length) + " "

    str_input = ""
    while len(str_input) != max_length:
        str_input = str(input("Gib Zahlen %sein " % count_str))
        return_list = []
        for char in str_input:
            return_list.append(int(char))
        if first_run:
            break

    return return_list

def cows_bulls_gen(length):
    gen = []
    for i in range(length):
        gen.append(random.randint(0, 9))
    return gen

def print_num(pc, user):
    print(pc)
    print(user)

def srch_cow_bull(generated_list, input_list):
    i = 0
    cows = 0
    bulls = 0
    for element in input_list:
        if element == generated_list[i]:
            cows = cows + 1
        if element in generated_list:
            bulls = bulls + 1
        i = i + 1
    bulls = bulls - cows

    return cows, bulls

def equals(gen, user):
    for i in range(4):
        if gen[i] != user[i]:
            return False
    return True



guess = read_input(max_length=None)
gen = cows_bulls_gen(len(guess))
#print_num(gen, guess)                  #uncomment if you want to see the both the generated and the user input list

cows = 0
while cows != len(gen):
    cows, bulls = srch_cow_bull(gen, guess)
    print("cows: %d, bulls: %d" % (cows, bulls))

    if cows == len(gen):
        print("Richtig geraten..")
        sys.exit()
    else:
        print("noch ein versuch!")
    guess = read_input(max_length=len(gen))
