class CoffeeShop:
    def __init__(self):
        self.name = 'CoffeeShop'
        self.menu = {
            'kava': 2,
            'arbata': 1,
            'buterbrodas': 4
        }
        self.oder = []
    def show(self):
        print(self.name, self.menu, self.oder)

    def add_order(self):
        obj = input("ko norit? kava, arbata, buterbrodas")
        for key, value in self.menu.items():
            if obj == key:
             print(key)
             print(value)
# reikia, kad idetu i lista ir paskaiciuotu kaina
p1 = CoffeeShop()
p1.add_order()