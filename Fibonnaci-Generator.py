fibnum = int(input("Bis zu welcher Zahl soll die Fibonnaci-Zahlenreihe generiert werden?"))
import time
time.sleep (2)
print ("Vorgang erfolgreich!")
time.sleep(1)
print("Fibonnaci-Zahlenreihe \nwird generiert..")

x = 1
y = 1
z = 0
while (x  < fibnum) and (y < fibnum) and (z < fibnum):
    z = x+y
    x = z+y
    y = x+z
    print (z,x,y)
