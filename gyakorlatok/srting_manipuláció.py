# stringek - karakterláncok
#concatenation - összefűzés
#slicing - szeletelés
#indexing - indexelés
#len() - string hossza, karakterek száma

szoveg = "Ez az én szövegem."
print(szoveg)

szoveg = szoveg.replace("szövegem" , "mondatunk").replace('én' , 'mi').replace('az', 'a') +"Lehetne kérdő is."
print(szoveg)

print(szoveg.index('mondatunk'))
print(len(szoveg))
print(szoveg.startswith('Ez'))
print(szoveg.endswith('is.'))

print(szoveg[13:13+8])
print(szoveg[-3:])

szoveg2= '                Ma este iszom egy korsó sört              '
print(szoveg2)
print(szoveg2.lstrip())
print(szoveg2.rstrip())
print(szoveg2.strip())


adatok1= '0,2,3,4,5,6,7,8,9'
adatok1 = adatok1.split(',')
print(adatok1)

adatok2 ='Eni;Zsoka;Andi;Reka;Zsuzsi'
adatok2 =adatok2.split(';')
print(adatok2)