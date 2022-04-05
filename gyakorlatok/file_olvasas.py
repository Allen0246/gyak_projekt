
#file = open ('mondasok.txt', 'r', encoding='utf-8')


#sor=file.readline()
#print(sor.strip())

#sor = file.readline()

#while sor:
#    print(sor.strip())
#    sor = file.readline()



#file.close()

with open ('mondasok.txt', 'r', encoding='utf-8') as file:
#    for sor in file:
#        print(sor.strip())

    sor = file.read()
    print(sor)

   # while sor:
    #    print(sor.strip())
    #    sor = file.readline