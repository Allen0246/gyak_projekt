#user difend types - felhasználó általá definuált típusok
#inheritance - öröklődés

class személy:
    def __init__(self, nev, kor, neme, nemzetiség, vallas='hindu'):
        self.nev = nev
        self.kor = kor
        self.neme = neme
        self.nemzetiség =nemzetiség
        self.vallás= vallas
        self.hello()
    
    def hello(self):
        print('hello ' +self.nev)

class Alkalmazott(személy):
    tapasztalat = 4
    megbízhatóság = 8
    vegzettség = 'konyvelo'

#object insatnce - objektum példány

Eni = Alkalmazott('Enikő', 25, 'nő', 'Magyar', 'pogány')
Kinga = Alkalmazott('Kinga', 36, 'nő', 'Magyar', 'protestáns')

print(Eni.nev)
print(Eni.vegzettség)

Kinga.vegzettség = 'ekonomus'
print(Kinga.nev)
print(Kinga.vegzettség)
print(Kinga.vallás)