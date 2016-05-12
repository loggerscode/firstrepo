#print("Problem Nr.15")
#eingabe = input("Gib einen Text mit mehreren Wörtern ein..")
#eingaberev = reversed(eingabe)
#print (eingabe)
#.join(eingabe.split()[::-1])

def reverseWord(w):
  return ' '.join(w.split()[::-1])
