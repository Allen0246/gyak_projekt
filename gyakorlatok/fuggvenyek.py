nevek1 = ['Béla', 'Józsi', 'János', 'Károly', 10, True]
nevek2 = ['Ancsa', 'Juli', 'Edina']

def nev_printer(nev_lista):
    for nev in nev_lista:
        if isinstance(nev,str):
            print(nev.upper())
        else:
            print('Nem string típus: ' + str(type(nev)))

nev_printer(nevek1)
nev_printer(nevek2)

#commit , majd push 1. része

a = 10
b = 20

def osszeadas1():
    print(a+b)

def osszeadas2(a,b, c=4):
    return a+b+c 

def osszeadas3(*barmi):
    return sum(barmi) #célszerű args ot használni a bármi helyett.

def udvozlesek(*args):
    koszones = 'Ennyi féle köszönés létezik: '
    for k in args:
        koszones += k
        koszones += ', '
    print(koszones[0:len(koszones)-2])

udvozlesek('szia', 'szervusz', 'hello','szevasz')

osszeadas1()
osszeg =  osszeadas2(45, 25)
print(osszeg)

print (osszeadas3(10,20,30,40,50,60,70,80,90,100))