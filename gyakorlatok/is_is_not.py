#'is 'is not' Identity operator -Azonossagi operator

from operator import truediv


szam1= 4
szam2= 4

print(szam1 == szam2)

szam= 8

if type(szam) is int:
    print('int tipus!')

if type(szam) is not str:
    print('Nem string típus!')

igaz = True

print(type(igaz) is not bool)

class személy:
    pass
sz1= személy()
sz2 = személy()

if type(sz1) is személy:
    print('Személy típus!')
else:
    print(type(sz1))