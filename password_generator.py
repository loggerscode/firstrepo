#!/usr/bin/python3


#Problem Nr. 16
#http://www.practicepython.org



import sys
import random
import urllib.request


def generate_integer_password(count):
    return random.randint(10**(count-1),(10**count)-1)

def get_wordlist():
    ret_list = []
    with urllib.request.urlopen("http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt") as wlist:
        for l in wlist.readlines():
            ret_list.append(l.decode('UTF-8').strip())
    return ret_list

def get_words_from_count(wordlist, length):
    ret_list = []
    for word in wordlist:
        if len(word) == length:
            ret_list.append(word)
    return ret_list

def get_random_word(wordlist):
    return wordlist[random.randint(0, len(wordlist) - 1)]

def get_random_word_with_length(wordlist, length):
    wlist = get_words_from_count(wordlist, length)
    return get_random_word(wlist)


password_question = ""

while not password_question == "yes":
    password_question = input("Do you want to create a password? yes/no ").casefold()
    if password_question == "no":
        sys.exit(0)


is_integer = True
password_length = 0
while password_length < 1 or not is_integer:
    try:
        password_length = int(input("How long is the pw? "))
        is_integer = True
    except ValueError as e:
        is_integer = False

print(generate_integer_password(password_length))

allwords = get_wordlist()
word = get_random_word_with_length(allwords, password_length)
print("First Version: %s" %word)

def randomupper(c):
    if random.random() > 0.5:
        return c.upper()
    return c.lower()

word =''.join(map(randomupper, word))

print ("Second Version: %s" %word)

def randomglyphs(b):
    mapping = {
            "a": "4",
            "b": "8",
            "c": "(",
            "d": "|)",
            "e": "3",
            "f": "f",
            "g": "9",
            "h": "h",
            "i": "!",
            "j": "1",
            "k": "|>",
            "l": "|",
            "m": "m",
            "n": "n",
            "o": "()",
            "p": "6",
            "q": "q",
            "r": "|*",
            "s": "5",
            "t": "7",
            "u": "u",
            "v": "v",
            "w": "w",
            "x": "x",
            "y": "y",
            "z": "z"}

    word1 = ""
    for i in b:
        word1 += mapping[i.lower()]
    print (word1)

randomglyphs(word)
