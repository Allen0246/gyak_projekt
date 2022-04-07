#stringek formatozás , és f stringek



# régi mód
szoveg1 = 'A te neved %s, és %d éves vagy.' %('Andi', 37)
print(szoveg1)

# nem olyan régi mód
szoveg2 = 'A te neved {}, és {} éves vagy.'.format('Ildi',28)
print(szoveg2)

# új mód (f strings)
nev = 'Enikő'
kor = 35
szoveg3= f'A te neved {nev}, és {kor} éves vagy.'
print(szoveg3)


