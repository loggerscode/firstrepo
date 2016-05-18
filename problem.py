#Problem Nr. 18
#http://www.practicepython.org



import random
from timeit import default_timer as timer

def given_list():                           #asks the user how many numbers the list will have and generates it
    random_list = []
    length = int(input("How long should the list be? "))

    i = 0
    while i <= length:
        number = random.randint(0, length * 10)
        if number not in random_list:
            random_list.append(number)
            i = i + 1
    return sorted(random_list)

def search_number1(search_value, random_list):
    return search_value in random_list

def search_number2(search_value, random_list):
    for element in random_list:
        if element == search_value:
            return True
    return False

def search_number3(search_value, random_list):
    for element in random_list[:search_value]:
        if element == search_value:
            return True
    return False

random_list = given_list()
search_value = int(input("What number do you search? "))
start = timer()
result = search_number1(search_value, random_list)
end = timer()
if result:
    print("1 Found!")
else:
    print("1 Not found!")
print("1 time %s" % str(float(end - start)))

start = timer()
result = search_number2(search_value, random_list)
end = timer()
if result:
    print("2 Found!")
else:
    print("2 Not found!")
print("2 time %s" % str(float(end - start)))

start = timer()
result = search_number3(search_value, random_list)
end = timer()
if result:
    print("3 Found!")
else:
    print("3 Not found!")
print("3 time %s" % str(float(end - start)))
