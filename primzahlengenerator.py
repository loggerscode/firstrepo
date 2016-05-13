import sys


def main(obergrenze):

    zahlen = [True]*(obergrenze+1)
    zahlen[0] = False
    zahlen[1] = False

    i = 2
    x= 0

    while i*i <= obergrenze:
        if zahlen[i] == True:
              for k in range(i*i,obergrenze+1,i):
                  zahlen[k] = False

        i = i+1

    for i, v in enumerate(zahlen):
         if v == True:
              print ('%d ist prim.' %i)
              x = x+i

    return x

if __name__ == ('__main__'):
    obergrenze = int(sys.argv[1])
    print(main(obergrenze))
