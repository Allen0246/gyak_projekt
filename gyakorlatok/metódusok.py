    
class személy:
    #member variables/fields - tag valtozók/mezők
    neve = ''
    kor = None
    neme = ''
    
    # methods - metódusok
    def set_kor(self, value):
        self.kor = value

    def set_nev(self, value):
        self.neve =value

    def set_neme(self,value):
        self.neme=value

#object instance - objektum példány
Ili = személy()
Ili.set_kor(21)
Ili.set_nev('Lilla')
Ili.set_neme('nő')

print(Ili.kor)
print(Ili.neve)
print(Ili.neme)

Laci = személy()
Laci.set_kor(25)
Laci.set_nev('Laci')
Laci.set_neme('Férfi')


print(Laci.kor)
print(Laci.neme)
print(Laci.neve)