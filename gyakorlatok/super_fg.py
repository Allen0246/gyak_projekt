#super() function - super() függvény

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
    def __init__(self,  nev, kor, neme, nemzetiség, vallas, tapasztalat, megbízhatóság, vegzettség):
        super().__init__(nev, kor, neme, nemzetiség, vallas)
        self.tapasztalat = tapasztalat
        self.megbizhatóság = megbízhatóság
        self.vegzettség = vegzettség


#object insatnce - objektum példány

Eni = Alkalmazott('Enikő', 25, 'nő', 'Magyar', 'pogány', 8, 8, 'könyvelő')
Kinga = Alkalmazott('Kinga', 36, 'nő', 'Magyar', 'protestáns', 8 ,8 ,'ekonómus')

print(Eni.nev)
print(Eni.vegzettség)
print(Eni.vallás)

print(Kinga.nev)
print(Kinga.vegzettség)
print(Kinga.vallás)