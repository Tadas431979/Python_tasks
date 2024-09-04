class Calc:

    def __init(self, a, b, oper):
        self.a: int = a
        self.b: int = b
        if oper =='plus':
            print(a+b)
       # self.plus = print(a + b)
        #self.minus = a - b
        #self.daug = a * b
        #self.dal = a / b


a = int(input("pirmas skaicius"))
b = int(input("antras skaicius"))
oper = input("iveskite plus, minus daug, dal")

veiksmas = Calc()
veiksmas(a, b, oper)
