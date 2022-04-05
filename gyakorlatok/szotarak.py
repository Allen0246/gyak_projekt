#Dictionaries, key-value pairs - Szotarak, kulcs-ertek parosok (java hash-maps, javascript object literals)

nev_kor = {'Ili':28, 'Betti':37, 'Magdi':41, 'Ani':34}

""" nev_kor['Andi'] = 56
print(nev_kor) # hozzá adja andi : 56 

nev_kor.pop('Ili')
print(nev_kor) # kitörlni Ili -t  """

print(nev_kor.get('Ani'))

""" for key in nev_kor.keys():
    print(key)

for value in nev_kor.values():
    print (value) """
""" 
for key, value in nev_kor.items():
    print(key,value) """

dict1 = {'adat1':[1,2,3,4,5,6],'adat2':78, 'adat3':(9,8,7,5)}