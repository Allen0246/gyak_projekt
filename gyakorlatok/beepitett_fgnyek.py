# abszolút értéket vesz az adott számból
print(abs(-78)) 

# megszámozza a neveket
nevek1 = ['Béla', 'Józsi', 'János', 'Károly']
for index, nev in enumerate(nevek1):
    print(index, nev)

# lebegő pontos számmá alakítja 10--> 10.0
print (float(10))

# hexadecimális számmá alakítja
print(hex(125))

# integerré alakítja csak a 24 et fogja kiírni
print(int(24.78))

# kiírja hogy mennyi nevet tartalmazz a lista
print (len(nevek1))
print (len("hello hogy vagy?"))

# a leganyobb,legkisebb értéket írja ki
print(max(7,8,112,43,98,32))
print(min(7,8,112,43,98,32))

# hatványozni
print(2**10) #kettő a tizediken
print(pow(2,10))

# range majd listát lehet gyártani belőle.
print (list(range(50,100)))

# visszafele írja ki a listát
print(list(reversed(nevek1)))

# kerekít, vessző után megadjuk mettől kerekítse
print(round(12.5212313, 4 ))

# össze adja a számokat, viszont csak a listából kellenek a [] jelek
print(sum([1,2,3,4,5,6,7,8,9]))

# vissz adja a típusát

print(type(10))
print(type(False))