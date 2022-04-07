#classes adn the objcet orinted programing - osztályok és az objektum orinteált programozás
# user defined types - felhasználó által definiált típusok


class személy:
    neve = ''
    kor = None
    neme = ''


sz1 = személy()
sz1.neve = 'Ildi'
sz1.kor = 28
sz1.neme = 'nő'

print(sz1.neve)
print(sz1.kor)
print(sz1.neme)

sz2 = személy()
sz2.neve = 'Laci'
sz2.kor = 64
sz2.neme = 'férfi'

print(sz2.neve)
print(sz2.kor)
print(sz2.neme)