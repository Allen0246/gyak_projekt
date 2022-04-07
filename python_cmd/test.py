import sys

def osszeg(a, b):
    return a+b


if len(sys.argv) > 1:
    try:
        szam1 = int(sys.argv[1])
        szam2 = int(sys.argv[2])
    except:
        szam1 = 0
        szam2 = 0
    
    
    print(osszeg(szam1, szam2))