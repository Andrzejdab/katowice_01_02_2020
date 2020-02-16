class Product:
    def __init__(self, id : int, nazwa : str,cena : float):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena
        self.lang = "pl"

    # def __str__(self):
    #     return "<Product : ({}) {}: {}>".format(self.id, self.nazwa, self.cena)

    def print_info(self):
        if self.lang =="pl":
            print(f"Product:\" {self.id}\", id:  {self.nazwa}, cena: {self.cena}")
        elif self.lang =="en":
            print(f"Product:\" {self.id}\", id:  {self.nazwa}, price: {self.cena}")

product = Product(1, "Woda", 10.99)
product.lang = "en"
product.print_info()