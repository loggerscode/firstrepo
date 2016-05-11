zustand = input ("Wie geht es dir?")
print ("Enrico geht es %s, doch wie lange noch? " % zustand)


x = 1
while True:
	print ("To infinity and beyond! Were getting close, on %d now!" , %x)
x+ = 1

n = 1
rn = 0
while n < 1000:
	if n%3 == 0 or n%5 == 0:
	    rn += n
n = n + 1
print (rn)

		Liste von 1-10

		x = range(1,11)
		for elem in x:
				print (elem)

			#Website: http://www.practicepython.org/



Problem Nr.4

print ("Problem Nr.4")
print ("Hallo!")
x = 0
e = []
nummer = int(input("Gebe eine Zahl ein.."))
l = range(1,nummer-1)
for i in l:
	if nummer%i == 0:
		e.append(i)
print (e)


Problem Nr. 5

print ("Problem Nr.5")
print ("Hallo!")
a = [1,1,2,3,5,8,13,21,34,55,89]
e = []
for i in a:
    if i < 56:
        e.append(i)
print (e)



Problem Nr. 6

print ("Problem Nr.6")
print ("Hallo!")
s = input("Gebe ein Wort ein..")
s = s.casefold()
revs = reversed(s)
if list(s) == list(revs):
        print("Das ist ein Palindrom..")
else:
        print("Das ist kein Palindrom..")



Problem Nr. 7

print ("Problem Nr.7")
print ("Hallo!")
e = []
a = [1,4,9,16,25,36,49,64,81,100]       #lange Version
for i in a:
    if i%2 == 0:
        e.append(i)
print (e)

a2 = [1,4,9,16,25,36,49,64,81,100]
e2 = [i for i in a2 if i%2 == 0]        #kurze Version
print (e2)



Problem Nr. 8

print ("Problem Nr.8")
print ("Hallo!")
neuespiel = True

while neuespiel:
    zuga = input("Spieler A ist am Zug..").casefold()
    zugb = input("Spieler B ist am Zug..").casefold()                                      #lange Version
    if zuga == zugb:
            print("Unentschieden")
    if (zuga == "stein" and zugb == "schere") or (zuga == "schere" and zugb == "papier") or (zuga == "papier" and zugb == "stein"):
            print ("Spieler A gewinnt..")
    else:
            print ("Spieler B gewinnt..")

    eingabe = input("Neues Spiel beginnen? Ja/Nein")
    neuespiel = eingabe == "Ja"



Problem Nr. 9

print ("Problem Nr.9")
print ("Hallo!")
import random
x = random.randint(1,9)
eingabe = int(input("Errate die Zahl zwischen 1 & 9.."))
import time
time.sleep (3)
if eingabe < x:
    print ("Unterschätzt..")
if eingabe > x:
    print ("Überschätzt..")
if eingabe == x:
    print ("Genau richtig..")
time.sleep(1)
print (x)



Problem Nr. 10

print ("Problem Nr.10")
print ("Hallo!")
import random
spiel = True

while spiel:
    x = random.randint(1,9)
    eingabe = int(input("Errate die Zahl zwischen 1 & 9.."))
    import time
    time.sleep (3)
    if eingabe < x:
        print ("Unterschätzt..")
    if eingabe > x:
        print ("Überschätzt..")
    if eingabe == x:
        print ("Genau richtig..")
    time.sleep(1)
    print (x)
    spiel1 = input("Weiterspielen? Ja/Nein..")
    spiel = spiel1
    if spiel1 != "Ja" :
        spiel = False



Problem Nr. 11

print ("Problem Nr.11")
print ("Hallo!")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list(set(a+b))
c.sort()
print (c)



Problem Nr. 12
print ("Problem Nr.12")
a = [5,10,15,20,25]
b = []
b.append(a[0])              #lange Version
b.append(a[-1])
print(b)
