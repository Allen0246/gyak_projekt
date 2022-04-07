#"in" membership operator - tagsági oprátor

mondas = 'Bagoly mondja verébnek, hogy nagyfejű'

#if('Bagoly' in mondas):
#    print('találat')

nevek_lista = ['Betti', 'Evi', 'Ildi', 'Andi']
if "Klári" not in nevek_lista:
    print('nincs találat')

nevek_szotar = {"Betti":28, "Evi":32, "Ildi":31, "Zsuzsi":40, 'Andi':34}
if "Klári" not in nevek_szotar:
    print("nincs találat!")

szamok1=[1,2,3,4,5,6,7]
szamok2=[0,2,6,8,7]

azonos_szamok=[]
egyedi_szamok=[]

for szam in szamok1:
    if szam not in szamok2:
        egyedi_szamok.append(szam)

""" for szam in szamok1:
    if szam in szamok2:
        azonos_szamok.append(szam)
    else:
        egyedi_szamok.append(szam) """

#print(azonos_szamok)
print(egyedi_szamok)