#exception handling

""" lista =[1,2,3]



try:
    #print(bla)
    #print(lista[5])
    print(1 / 0)
except NameError as e:
    print(e, ' - Nem létező változó!')
except IndexError as e:
    print(e, ' - Tartományon kívüli index!')
except ZeroDivisionError as e:
    print(e, ' - Nullával való osztás!')
print('A program vége!') """

from tkinter import E


lista = ['1','2','3', None, '4', '', '5', 'True', 'Bözsi', '12.64']
for i in lista:
    try:
        print (int(i)*2)
    except:
        continue

print(True == 1)

try:
    print('bal')
except:
    print('nem jó változó név')
""" else:
    pass
finally:
    print('try vége') """
## nem nagyon használtak