def hello():
    print(f'Hello {__name__} modulból!')

szam= 10

class személy:
    def __init__(self,név,kor):
        self.név = név
        self.kor = kor
    
    def show_fields(self):
        print(self.név, self.kor)



if __name__ == '__main__':
    hello()
    print(szam)
    Juli = személy('Juliska',25)
    Juli.show_fields()