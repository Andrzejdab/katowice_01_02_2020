import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other

    def __add__(self, other):
        if isinstance(other, Vector):
            self.x = self.x + other.x
            self.y = self.y + other.y
        return Vector(self.x, self.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            self.x = self.x - other.x
            self.y = self.y - other.y
        return Vector(self.x, self.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            self.x = self.x * other.x
            self.y = self.y * other.y
        return self.x + self.y

    def __rmul__(self, other):
        self.x = self.x * other
        self.y = self.y * other
        return Vector(self.x, self.y)
    def __str__(self):
        return  F"<Vector: {self.x}, {self.y}>"

    @property
    def __len__(self):
        len = math.sqrt(self.x ** 2 + self.y ** 2)


class TestVektor:

    def test_initialization(self):
        v = Vector(1, 3)
        assert v.x == 1
        assert v.y == 3

    def test_add_vector(self):
        v1 = Vector(1, 3)
        v2 = Vector(2, 4)
        assert v1 + v2 == Vector(3, 7)

    def test_sub(self):
        v1 = Vector(1, 3)
        v2 = Vector(2, 4)
        assert v1 + v2 == Vector(-1, -1)

    def test_mul(self):
        v1 = Vector(1, 3)
        v2 = Vector(2, 4)
        assert v1 * v2 == 2 + 12

    def test_rmul(self):
        v1 = Vector(1, 3)

        assert v1 * 5 == Vector(5, 15)

    def test_len(self):
        v1 = Vector(2, 2)
        assert len(v1) == math.sqrt(8)