class OperasBas:

    #declaración de propiedades
    num1 = 9
    um2 = 0
    res = 0

    #declaración del constructor this
    def __init__(self):
        self.num1=0
        self.um2=0

    #declaración de metodos de clase
    def suma(self, a):
        self.num1=a
        self.res=self.num1+self.um2
        print("La suma es: {}". format(self.res))

    def resta(self):
        self.res=self.num1-self.um2
        print("La resta es: {}".format(self.res))

def main():
    obj=OperasBas()
    obj.suma(5)
    obj.resta=()


if __name__ == "__main__":
    main()