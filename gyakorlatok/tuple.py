# tuple - nem modosítható adathalmaz (immutable)

#modosítható adat []
lista = ['Juci','Ani','Ili','Barbi']

#nem modosítható adat ()
tup1 = ('Juci', 'Ani', 'Ili', 'Barbi')

print(tup1.index('Ili')) #megmutatja melyik helyen található
print(tup1.count('Barbi')) #megszámolja hány Barbi van


tup1 = ('Juci', 'Ani', 'Ili') # csak így lehet modosítani a tuple-t, ha újra definiáljuk

tup2 = ('Betti',)
print(tup2) #Stringnek veszi ha csak 1 db van benne.

#lista.append('Bözsi')
#print(lista)
#lista[-1] = 'Betti' #utolsó elem a -1 vagyis Bözsi , atírja Bettire.
#print(lista) 

#tup1[-1] = 'Betti' #hibát ad!

#print(tup1[1:])
 
#tup2 = tuple(lista)
#print(tup2)

#lista2= list(tup2)
#print(lista2)