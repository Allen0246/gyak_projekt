

jelszo = 'neaddki'

bemenet = input('Mi a jelszo? ')

proba = 0 


while bemenet !=jelszo:
    proba +=1
    if proba == 3:
        print('Rendszer lezarva')
        break
    print('Rossz jelszo, problad ujra ')
    bemenet = input('Mi a jelszo? ')

if bemenet == jelszo:
    print('Hozzaferes megadva. ')

    #commitolás