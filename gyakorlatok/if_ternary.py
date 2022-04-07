# if ternary operator

lang = 'HUN'

#print('Jó estét!') if lang == 'HUN' else print('Good evening!' if lang == ENG else print('Bueana noches!'))

if lang == 'HUN':
    print('Jó estét!')
elif lang == 'ENG':
    print('Good evening!')
elif lang == 'ESP':
    print('Buena noches!')