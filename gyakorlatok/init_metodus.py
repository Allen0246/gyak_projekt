#classes and the object orinted programing - osztályok és az objektum orientált programozás
#user defined types -felhasználó általá definiált típusok

#az __init__ metodus, más nyelvekben ez a konstruktor metódus

class személy:
    def __init__(self, nev, kor, neme, nemzetiség, vallas='hindu'):
        self.nev = nev
        self.kor = kor
        self.neme = neme
        self.nemzetiség =nemzetiség
        self.vallás= vallas
    
    def hello(self):
        print('hello ' +self.nev)

#object insatnce - objektum példány

Ildi=személy('Ildiko', 32,'nő' , 'Magyar', 'keresztény')
Laci=személy('László', 47, 'férfi', 'Kínai')


#print(Ildi.vallás)
#print(Laci.vallás)

Ildi.hello()
Laci.hello()

print(type(Ildi))
print(type(Laci))