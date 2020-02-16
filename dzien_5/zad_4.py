class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Basket:
    def __init__(self):
        self.products=[]


    def add_product(self, product, amount):
        self.products.append(BasketEntry(product, amount))

    def count_total_price(self):
        total_price = 0
        for be in self.products:
            total_price += be.product.price * be.amount
        return total_price


class BasketEntry:
    def __init__(self,product, amount):
        self.product = product
        self.amount = amount





class TestProduct:
    def test_init(self):
        product = Product(1, "Woda", 10)
        assert product.id == 1
        assert product.name == "Woda"
        assert product.price == 10

class Testbasket:
    def test_basket(self):
        basket = Basket()
        assert basket


    def test_add_product(self):
        basket = Basket()
        product = Product(1, "Woda", 10)
        basket.add_product(product, 3)
        assert len(basket.products) == 1
        assert  basket.products[0].amount == 5
        product2 = Product(2, "Chleb", 5)
        basket.add_product(product2, 5)
        assert len(basket.products) == 2
        assert basket.products[1].amount == 2
        assert basket.products[1].product == product2

    def test_count_total_price(self):
        basket = Basket()
        product = Product(1, "Woda", 10)
        basket.add_product(product, 2)
        product2 = Product(2, "Chleb", 3)
        basket.add_product(product2, 3)
        basket.count_total_price() == 29