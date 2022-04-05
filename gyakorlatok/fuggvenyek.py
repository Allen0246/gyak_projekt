nevek1 = ['Béla', 'Józsi', 'János', 'Károly', 10, True]
nevek2 = ['Ancsa', 'Juli', 'Edina']

def nev_printer(nev_lista):
    for nev in nev_lista:
        if isinstance(nev,str):
            print(nev.upper())
        else:
            print('Nem string típus: ' + str(type(nev)))

nev_printer(nevek1)
nev_printer(nevek2)