
# 1.Модифицируйте класс Point следующим образом:
#   -обеспечьте проверку значений координат (только числа),
#   -добавьте метод (не magic), который бы позволял сравнивать точки (если координаты точек совпадают - точки равны)
#   -создайте метод __str__ . он должен отдавать информацию в формате ("Point with coordinates [координата х] : [координата у] ")
class Point:
    _x = None
    _y = None

    def __init__(self, val1, val2):

        self.x = val1
        self.y = val2

    def __str__(self):
        return f"Point with coordinates {self.x}:{self.y}"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError
        self._y = val

    def Equal(self, val):
        if not isinstance(val, type(self)):
            raise TypeError
        elif self.x == val.x and self.y == val.y:
            print("*" * 100)
            print("Point are equal")
            return True
        else:
            print("*" * 100)
            print("Point are not equal")
            return False