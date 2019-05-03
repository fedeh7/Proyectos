



class Fraccion:
    def __init__(self,arriba,abajo):
        self.num = arriba
        self.den = abajo

def main():
    f = Fraccion(2,3)
    f2 = Fraccion(4,5)
    print(f, f2)
    print(f.show())

main()