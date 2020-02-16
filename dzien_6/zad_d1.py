# Stworz klase postac która ma atrybuty: zycie, siła, zwinnosc, obrona, imie,
# przy uzyciu biblioteki Faker stwórz mechanizm tworzenia losowych postaci
#  pip install faker
from faker import Faker
fake = Faker("pl_PL")

class Polozenie:


    def __str__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def random(cls):
        return

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



class Osoba:


    def __init__(self, name):
        self.name = name
        self.zycie = fake. random.randint(1, 101)
        self.sila = fake.random.randint(1, 101)
        self.zwinnosc = fake.random.randint(1, 101)
        self.obrona = fake.random.randint(1, 101)
    @classmethod
    def with_fake_nme(cls):
        return  cls(fake.name())

    def __str__(self):
        pass

    @property
    def zyje(self):
        return True if self.zycie > 0 else False

    @staticmethod
    def walka(self):
        postac1

    def otrzymaj_obrazenia(self, moc_ciosu):
        print("otrzymuje obrażenia", moc_ciosu)
        self.zycie -= moc_ciosu

    def zadaj_obrazenia(self):
        return fake.random.randint(1,100)

class Predmiot:

    def __init__(self):
        pass




postac = Osoba
siekiera = Predmiot("Krwawa siekiera")

if postac.polozenie == siekiera.polozenie:
    print(f' znalazłes ekwipunek - '