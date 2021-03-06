#number típus
from re import X
from sqlite3 import paramstyle


number= 12
print(f" Integer: {number}, memory address: {id(number)}")
print(type(number))

#float típus
number= 12.1
print(f" FLoat: {number}, memory address: {id(number)}")
print(type(number))

#complex típus
number= 12j
print(f" complex: {number}, memory address: {id(number)}")
print(type(number))

#string típus
number=' string'
print(type(number))

#maradékos osztás
a=8
b=3
print(8%3)

#többet meglehet határozni
a, b, c ,d = 8 , 3 ,"Hello" , [1,2,4,5]
print(type(c))

 #hatványozás
szam = pow(2, 3)
print(szam)

#darabolás
szoveg= 'Darabolás!' #minden 2. karaktert ír ki a 6. karakterig
print(szoveg[1:6:2])
print(szoveg[-1:-4:-1])

#tükör ??

szöveg= 'indul a görög aludni'
szöveg=szöveg.replace(' ', '')
mirror =szöveg[::-1]

print(szöveg)

if szöveg==mirror:
    print('palindrom')
else:
    print('nem jó!')


#lista reverse
lista = [1,2,3,4,5]
print(lista)

print(lista[::-1]) #visszafelé lista

lista.reverse() #visszafelé lista
print(lista)


# A 8. pozíciótol indul
print(szöveg.find("görög"))

#2db "ö" betű van benne
print(szöveg.count('ö'))

#nagybetűs
print(szöveg.upper())
#kisbetűs
print(szöveg.lower())

#split listába
lista= szöveg.split()
print(lista)

#print dri, print help

print(dir(str))
print(help(str.count))

lista = [10,20,30,40,50,60,70,80,90,100]

uj_lista = []
for elem in lista:
    if elem > 30:
        uj_lista.append(elem)
print(uj_lista)

l = [
    elem #select
    for elem in lista #from
    if elem>30 #feltétel
]
print(l)
""" lista.append('szoveg')
print(lista) """

utolso_elem = lista.pop() #leveszi az utolsó elemet
print (utolso_elem)
print (lista)


for index, elem in enumerate(lista): #kiírja indexek mellé az elemket is
    print(f"{index} {elem}")

for x in range(1,20,2): #kiírja a számokat 20 ig, 2 esével lépeget felfelé
    print(x)

#break szemléltetése
for x in range(10):
    print(x)
    if x == 11:
        break
else:
    print("Ha végig futott a ciklus ez az ág lefut")

#addig printeli ki míg el nem éri a 9 et
x=0
while x < 10:
    print(x)
    x+=1

#tuple nevek
nevek =  'Peter', 'Andrea', 'David', 'Bálint'

nev1, nev2, nev3, nev4 = nevek
print (nev1, nev2, nev3, nev4)
print(nev1)

#tupple össze hasonlítása
nevek =  'Peter', 'Andrea',['Dezső', 'András',2], 'David', 'Bálint',[1,2,3]
nevek2 =  'Peter', 'Andrea',['Dezső', 'András',2], 'David', 'Bálint', [1,2,3]

if nevek==nevek2:
    print("egyforma")
else:
    print("nem egyforma")

#zipelés
szamok ='1 2 3 4 5 6 7 8 9'.split()
szam_nevek ='egy kettő három négy öt hat hét nyolc kilenc'.split()

print(szamok)
result = zip(szamok, szam_nevek)
print(dict(result))

#zip össze mergel, két listát, tuple-t ... mérte különbözet nem számít

egyforma = True

for nevek, nevek2 in zip(nevek, nevek2):
    if nevek !=nevek2:
        egyforma = False
        break
print(egyforma)

#def függvény , +none
def fuggveny(nev,becenev=None):
    if  not becenev:
        print(f"Hello {nev}!")
    else:
        print(f"Hello {becenev}")
fuggveny("Peter", becenev='Peti')

from enum import Enum

class Muvelet(Enum):
    Összedás = 1
    Szorzás = 2

#szamologép
def szorzas (szamok):
    result = 1
    for _ in szamok:
        result*=_
    return result

parameter=15,5
print(szorzas(parameter))

def szamologep(*args, muvelet=Muvelet.Szorzás):
    if muvelet == Muvelet.Összedás:
        print(sum(args))
    if muvelet==Muvelet.Szorzás:
        print(szorzas(args))

szamologep(2,3,8,9,muvelet= Muvelet.Szorzás)


def adatok(**kwargs):
    print(kwargs)

adatok(nev= 'Peter', kedvenc_turborago_automarkaja= 'Tesla' , eletkor= 12)

x= 'Globális változó'

def parameter_scope():
    # global x
    x ="belső változó"
    print(x)
    def belso():
        x =' legbelsőbb'
        print(x)
    belso()

parameter_scope()
print(x)


if __name__ =="main":
    parameter_scope()
    print(X)
    print(sum((1, 2, 3, 4, 5)))

    adatok(nev= 'Peter', kedvenc_turborago_automarkaja= 'Tesla' , eletkor= 12)
    szamologep(2,3,8,9,muvelet= Muvelet.Szorzás)
