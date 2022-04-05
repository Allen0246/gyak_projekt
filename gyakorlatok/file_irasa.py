# 'r' = read (olvasás)
# 'w' = write (írás)
# 'a' = append (hozzáfűzés,mellekel)

#with open('mondasok.txt', 'r', encoding='utf-8') as infile:
    #with open('out.txt', 'w', encoding='utf-8') as outfile:
       
       #sor = infile.readline()
       #while sor:
            #outfile.write(sor)
            #sor = infile.readline()
with open('out.txt', 'a', encoding='utf-8') as file:
    ujsor = '\nNem akarásnak nyögés a vége.'
    file.write(ujsor)