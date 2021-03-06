class ElectricCar:
    NEXT_ID = 1

    def __init__(self, max_range):
        self.max_range = max_range
        self.traveled = 0
        self.id = self.NEXT_ID
        ElectricCar.NEXT_ID += 1

    def drive(self, range):
        if self.traveled + range < self.max_range:
            self.traveled += range
            return range
        to_travel = self.max_range - self.traveled
        self.traveled = self.max_range
        return to_travel

    def charge(self):
        self.traveled = 0


class TestElectricCar:
    def test_init(self):
        car = ElectricCar(100)
        assert car

    def test_drive(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(10) == 10
        assert car.drive(30) == 20
        assert car.drive(30) == 0

    def test_charge(self):
        car = ElectricCar(150)
        assert car.drive(150) == 150
        assert car.drive(150) == 0
        car.charge()
        assert car.drive(150) == 150

    def test_id(self):
        ElectricCar.NEXT_ID = 1
        car = ElectricCar(150)
        assert car.id == 1
        car = ElectricCar(150)
        assert car.id == 2
        car = ElectricCar(150)
        assert car.id == 3
